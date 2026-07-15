"""Tests for sync_vault.py.

Fixtures are copied from the real defect lines in the vaults, not invented —
each one corresponds to something that actually broke.

Run:  python3 -m unittest discover scripts
"""

import re
import unittest
from pathlib import Path

import sync_vault as sv


class TestSlugify(unittest.TestCase):
    def test_keeps_numeric_prefix_so_alpha_order_is_intended_order(self):
        self.assertEqual(sv.slugify("06 Giant Component"), "06-giant-component")

    def test_ampersand_becomes_and(self):
        self.assertEqual(sv.slugify("02 MLE & MAP"), "02-mle-and-map")

    def test_parens_and_underscores(self):
        self.assertEqual(sv.slugify("Union-Find (Disjoint Set)"), "union-find-disjoint-set")
        self.assertEqual(sv.slugify("Red_Black Trees"), "red-black-trees")


class TestFrontmatter(unittest.TestCase):
    def test_faceted_tag_list(self):
        fm, body = sv.split_frontmatter(
            "---\ntags:\n  - area/random-graphs\n  - method/bfs-exploration\n---\n\n## 1. What\n"
        )
        self.assertEqual(fm["tags"], ["area/random-graphs", "method/bfs-exploration"])
        self.assertTrue(body.startswith("## 1."))

    def test_no_frontmatter_passes_through(self):
        fm, body = sv.split_frontmatter("# Title\n\ntext\n")
        self.assertEqual(fm, {})
        self.assertTrue(body.startswith("# Title"))


class TestCallouts(unittest.TestCase):
    def setUp(self):
        self.rep = sv.Report()

    def conv(self, s):
        return sv.convert_callouts(s, self.rep, "t.md")

    def test_collapsed_dash_becomes_question_mark_triple(self):
        # This is the flashcard rule: the trailing `-` is load-bearing.
        out = self.conv("> [!question]- Why divide by √d_k?\n> Because variance grows.\n")
        self.assertIn('??? question "Why divide by √d_k?"', out)
        self.assertNotIn("???+", out)
        self.assertIn("    Because variance grows.", out)

    def test_plus_becomes_open_collapsible(self):
        out = self.conv("> [!tip]+ Open\n> body\n")
        self.assertIn('???+ tip "Open"', out)

    def test_no_fold_is_static(self):
        out = self.conv("> [!warning] Key subtlety\n> body\n")
        self.assertIn('!!! warning "Key subtlety"', out)

    def test_goal_maps_to_success_with_default_title(self):
        out = self.conv("> [!goal]\n> ship it\n")
        self.assertIn('!!! success "Goal"', out)

    def test_faq_and_important_map_to_native_types(self):
        self.assertIn("!!! question", self.conv("> [!faq] Q\n> a\n"))
        self.assertIn("!!! tip", self.conv("> [!important] I\n> a\n"))

    def test_unknown_type_degrades_to_note_and_warns(self):
        out = self.conv("> [!bogus] Hi\n> a\n")
        self.assertIn("!!! note", out)
        self.assertTrue(any("bogus" in w for w in self.rep.warnings))

    def test_callout_inside_code_fence_is_left_alone(self):
        src = "```md\n> [!note] literal\n```\n"
        self.assertIn("> [!note] literal", self.conv(src))


class TestStripHeadings(unittest.TestCase):
    def test_section_7_removed_but_section_8_survives(self):
        src = (
            "## 6. Lemmas\nkeep me\n\n"
            "## 7. Homework examples\n- HW7 P2: the proof\n\n"
            "## 8. Common mistakes\nkeep me too\n"
        )
        out = sv.strip_headings(src, ["## 7. Homework examples"])
        self.assertIn("## 6. Lemmas", out)
        self.assertIn("## 8. Common mistakes", out)
        self.assertNotIn("HW7 P2", out)
        self.assertNotIn("Homework examples", out)

    def test_exam_slots_go_and_the_learning_slots_stay(self):
        # The manifest strips three of the template's ten sections at once.
        src = (
            "## 2. Core objects / definitions\nkeep\n\n"
            "## 3. Main question types\n1. count the thing\n\n"
            "## 4. How to recognize this topic in a problem\n1. BFS smell\n\n"
            "## 5. Standard proof moves\nkeep\n\n"
            "## 9. What I should try first on an exam\n1. write the recursion\n\n"
            "## 10. Quick memory hooks\nkeep\n"
        )
        out = sv.strip_headings(
            src,
            [
                "## 3. Main question types",
                "## 4. How to recognize this topic in a problem",
                "## 9. What I should try first on an exam",
            ],
        )
        self.assertIn("## 2. Core objects / definitions", out)
        self.assertIn("## 5. Standard proof moves", out)
        self.assertIn("## 10. Quick memory hooks", out)
        self.assertNotIn("Main question types", out)
        self.assertNotIn("BFS smell", out)
        self.assertNotIn("on an exam", out)
        self.assertNotIn("write the recursion", out)

    def test_same_number_different_title_is_not_collateral(self):
        # 11 Small World numbers "Common mistakes" as 9, which is the exam slot's
        # number everywhere else. Exact-line matching is the only thing keeping it.
        src = (
            "## 9. Common mistakes\nkeep me\n\n"
            "## 10. Quick memory hooks\nkeep me too\n"
        )
        out = sv.strip_headings(src, ["## 9. What I should try first on an exam"])
        self.assertIn("## 9. Common mistakes", out)
        self.assertIn("keep me", out)

    def test_unnumbered_variant_strips_too(self):
        # Six notes never took the numbered template.
        src = "## Recognition signals\n- looks like a BP\n\n## Pitfalls\nkeep\n"
        out = sv.strip_headings(src, ["## Recognition signals"])
        self.assertIn("## Pitfalls", out)
        self.assertNotIn("looks like a BP", out)

    def test_pattern_matching_a_non_heading_is_an_error_not_a_swallowed_note(self):
        # A prefix without hashes used to reach re.match(...).group(1) on None and
        # die with a bare AttributeError; the section it "matched" has no level to
        # bound, so the rest of the note would go with it.
        src = "intro\nHW mentioned in passing\nmore body\n"
        with self.assertRaises(SystemExit):
            sv.strip_headings(src, [], ["HW"])


class TestRenumber(unittest.TestCase):
    def test_gap_left_by_stripped_section_is_closed(self):
        # After "## 7. Homework examples" is stripped the doc reads 1..6, 8, 9,
        # which advertises that something was taken out.
        src = "## 1. What\na\n\n## 6. Lemmas\nb\n\n## 8. Mistakes\nc\n"
        out = sv.renumber_headings(src)
        self.assertIn("## 1. What", out)
        self.assertIn("## 2. Lemmas", out)
        self.assertIn("## 3. Mistakes", out)
        self.assertNotIn("## 8.", out)

    def test_headings_inside_a_fence_are_not_renumbered(self):
        src = "## 1. Real\n```\n## 9. not a heading\n```\n## 5. Next\n"
        out = sv.renumber_headings(src)
        self.assertIn("## 9. not a heading", out)
        self.assertIn("## 2. Next", out)

    def test_unnumbered_headings_untouched(self):
        src = "## Setup\na\n\n## Theorem 1\nb\n"
        self.assertEqual(sv.renumber_headings(src), src)


class TestTableTransforms(unittest.TestCase):
    def test_display_math_in_cell_becomes_inline(self):
        # Asymptotic.md: $$..$$ in a table cell doesn't render under arithmatex.
        src = "| a | $$\\text{Total} = N + 1$$ |"
        out = sv.convert_table_math(src)
        self.assertIn("$\\text{Total} = N + 1$", out)
        self.assertNotIn("$$", out)

    def test_display_math_outside_table_untouched(self):
        src = "$$f(x) = 1 - e^{-cx} - x$$"
        self.assertEqual(sv.convert_table_math(src), src)

    def test_drop_named_column(self):
        src = (
            "| Method | HW | Trap |\n|---|---|---|\n"
            "| Chernov | HW7 P1 | additive vs multiplicative |\n"
        )
        out = sv.drop_table_column(src, "HW")
        self.assertNotIn("HW7 P1", out)
        self.assertIn("Chernov", out)
        self.assertIn("additive vs multiplicative", out)


class TestDefects(unittest.TestCase):
    def setUp(self):
        self.rep = sv.Report()

    def test_glued_embed_gets_separated(self):
        # Heap.md:13 — `4. parent(k) = k/2![[Heap array.png]]`
        out = sv.fix_defects("4. parent(k) = k/2![[Heap array.png]]\n", self.rep, "t.md")
        self.assertIn("k/2 ![[Heap array.png]]", out)

    def test_empty_mermaid_block_dropped(self):
        # Optimization.md:9 renders as an error box.
        out = sv.fix_defects("before\n```mermaid\ngraph TD\n```\nafter\n", self.rep, "t.md")
        self.assertNotIn("mermaid", out)
        self.assertIn("before", out)
        self.assertIn("after", out)

    def test_real_mermaid_block_survives(self):
        src = "```mermaid\nflowchart LR\n  A --> B\n```\n"
        self.assertIn("flowchart LR", sv.fix_defects(src, self.rep, "t.md"))

    def test_unicode_minus_fixed_inside_math_only(self):
        out = sv.fix_defects("$y \\in {−1, 1}$ and a dash − in prose\n", self.rep, "t.md")
        self.assertIn("$y \\in {-1, 1}$", out)
        self.assertIn("dash − in prose", out)

    def test_unterminated_fence_closed(self):
        out = sv.fix_defects("text\n```python\nimport logging\n", self.rep, "t.md")
        self.assertEqual(out.count("```"), 2)


class TestDebox(unittest.TestCase):
    def test_checkbox_content_becomes_plain_bullet(self):
        # The ML notes' Subtopics are content wearing a checklist costume.
        src = "- [ ] `Attention(Q,K,V) = softmax(QKᵀ/√d_k) V`\n- [x] done\n"
        out = sv.debox_tasks(src)
        self.assertIn("- `Attention(Q,K,V)", out)
        self.assertNotIn("[ ]", out)
        self.assertNotIn("[x]", out)


class TestParentChildren(unittest.TestCase):
    def test_lifts_both_and_accepts_single_bracket(self):
        # Counting-based sort.md:1 has the malformed `Children: [RadixSort]`.
        body, rels = sv.lift_parent_children(
            "Parent: [[Trees]]\nChildren: [RadixSort]\n\n## Body\n", "t.md"
        )
        self.assertEqual(rels, [("Parent", "Trees"), ("Children", "RadixSort")])
        self.assertTrue(body.startswith("## Body"))

    def test_semicolon_separated_children(self):
        _, rels = sv.lift_parent_children("Children: [[Interface]]; [[Class]]\n", "t.md")
        self.assertEqual([t for _, t in rels], ["Interface", "Class"])


class TestTitles(unittest.TestCase):
    def test_synthesises_title_when_no_h1(self):
        # All 18 networks notes open with frontmatter then `## 1.`.
        n = sv.Note(src=Path("/v/06 Giant Component.md"), rel="06 Giant Component.md",
                    section=None, body="## 1. What this topic is about\n")
        fm, body = sv.ensure_title({}, n)
        self.assertEqual(fm["title"], "Giant Component")
        # and an H1 is synthesised, so the page doesn't start at h2
        self.assertTrue(body.startswith("# Giant Component"))

    def test_existing_h1_wins_but_loses_its_numeric_prefix(self):
        # Otherwise nav reads "Giant Component" beside "09 Transformers & Attention".
        n = sv.Note(src=Path("/v/09 Transformers & Attention.md"), rel="ml/09 t.md",
                    section=None, body="# 09 Transformers & Attention\n\nbody\n")
        fm, body = sv.ensure_title({}, n)
        self.assertEqual(fm["title"], "Transformers & Attention")
        self.assertIn("# Transformers & Attention", body)
        self.assertNotIn("# 09 Transformers", body)


class TestPolicyGate(unittest.TestCase):
    """The two tests that must never be skipped."""

    def setUp(self):
        cfg = sv.load_manifest(sv.MANIFEST)
        self.patterns = [re.compile(p, re.I) for p in cfg["denylist"]["fail_patterns"]]
        self.deny = cfg["denylist"]["paths"]

    def test_pii_in_body_raises(self):
        for probe in ["call 510-499-0090", "ruoxi_wu@berkeley.edu",
                      "Shixiang Tech", "see HW7 P2", "from your red notes"]:
            with self.subTest(probe=probe):
                with self.assertRaises(sv.PolicyViolation):
                    sv.assert_publishable(f"# Note\n{probe}\n", "t.md", self.patterns)

    def test_clean_body_passes(self):
        sv.assert_publishable("# Giant Component\n\n$$f(x) = 1 - e^{-cx} - x$$\n",
                              "t.md", self.patterns)

    def test_violation_message_never_echoes_the_secret(self):
        try:
            sv.assert_publishable("call 510-499-0090\n", "t.md", self.patterns)
        except sv.PolicyViolation as e:
            # The whole point: enough to find it, not enough to leak it.
            self.assertNotIn("0090", str(e))
            self.assertNotIn("510-499", str(e))
            self.assertIn("t.md", str(e))
            self.assertIn("line 1", str(e))
        else:
            self.fail("expected PolicyViolation")

    def test_denylisted_paths_are_denied(self):
        for p in ["spring2026 copy/networks/midterm-solutions.pdf",
                  "spring2026 copy/networks/hw/HW3 Study Notes.md",
                  "python copy/application_plan/resume.tex",
                  "python copy/pdf/cs188.pdf",
                  "Computer Science copy/Screenshot/OOP eg answer.png",
                  "spring2026 copy/machine_learning/hw4_written_student.tex"]:
            with self.subTest(path=p):
                self.assertTrue(sv.is_denied(sv.REPO / p, self.deny), f"{p} should be denied")

    def test_published_paths_are_not_denied(self):
        for p in ["spring2026 copy/networks/topics/06 Giant Component.md",
                  "python copy/ml/09 Transformers & Attention.md",
                  "Computer Science copy/cs61b/QuickSort.md"]:
            with self.subTest(path=p):
                self.assertFalse(sv.is_denied(sv.REPO / p, self.deny), f"{p} should publish")


class TestRender(unittest.TestCase):
    def test_frontmatter_is_the_very_first_thing_in_the_file(self):
        """Regression: the marker used to sit above the frontmatter.

        YAML frontmatter only counts if it opens the file. With the comment
        first, MkDocs parsed the whole block as body text -- every page printed
        "tags: - area/random-graphs ... title: Giant Component" as visible
        content, ignored `title:` (so the H1 fell back to the lowercased
        filename, "06 giant component"), and indexed zero tags. `mkdocs build
        --strict` stayed green throughout: the output was valid markdown, just
        wrong. Only reading the rendered HTML caught it.
        """
        n = sv.Note(src=Path("/v/x.md"), rel="networks/topics/06 Giant Component.md",
                    section=None, frontmatter={"title": "Giant Component",
                                               "tags": ["area/random-graphs"]},
                    body="## 1. What\n")
        out = sv.render(n)
        self.assertTrue(out.startswith("---\n"), "frontmatter must open the file")
        self.assertLess(out.index("title: Giant Component"), out.index(sv.MARKER_PREFIX))

    def test_marker_present_and_frontmatter_filtered(self):
        n = sv.Note(src=Path("/v/x.md"), rel="ml/09 x.md", section=None,
                    frontmatter={"title": "T", "tags": ["area/x"], "status": "draft",
                                 "source": "cs189 §9"},
                    body="body\n")
        out = sv.render(n)
        self.assertIn(sv.MARKER_PREFIX, out)
        self.assertIn("title: T", out)
        self.assertIn("  - area/x", out)
        # Authoring metadata is not site content.
        self.assertNotIn("status", out)
        self.assertNotIn("cs189", out)


if __name__ == "__main__":
    unittest.main()
