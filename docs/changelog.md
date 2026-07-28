---
title: Changelog
summary: Dated record of what changed — the difference between a living notebook and an article graveyard.
---

# Changelog

Most sites publish and never touch the page again. This one is supposed to
change, so the changes are the record.

Entries are newest first, and specific: which note, which section, what changed.
"Various improvements" tells a reader nothing about whether the thing they read
last month is still what it says.

---

## 2026-07-28

Cut the home page back to one argument.

- Removed the **Featured projects** block — three cards competing with the
  capability map for the same attention. The capability map is the claim this
  site is making, so it gets the space.
- Removed the **Blog** and **Build Logs / Postmortems** cards from *Also here*,
  leaving Learn and Labs. All four pages still exist and stay in the nav.
- Left the home page's **Reference** section blank pending a decision about what
  it should say. The 57 generated pages are unaffected and still reachable from
  the nav.
- Corrected a repeated miscount: the Reference section holds **57** generated
  pages, not 79. The wrong number had propagated into four files and onto this
  page.
- Deleted the **AI Research Assistant** project page. It documented a project
  that does not exist — a plan wearing a project page's clothes. Nine notes had
  it in their `projects:` frontmatter, so the status strip was advertising it on
  pages across the site; those references are cleared. The idea is not dead, it
  just gets a page when there is something to put on it.

This supersedes the 2026-07-26 entry below: projects and blog no longer lead the
home page, and no longer appear on it at all. That entry stays as written —
a changelog that gets edited to agree with the present is not a changelog.

## 2026-07-27

Restructured the site around engineering capability instead of course.

- Added the capability map: Foundations, Frontend, Backend, Data Systems, AI
  Engineering, Production — each with a landing page saying what it covers and
  what is still missing.
- Added five [Learn paths](learn/index.md) as reading orders that cross those
  folders, including one (AI Infrastructure) that is honestly empty.
- Seeded the twelve first notes as stubs, each with a real problem statement and
  a `What Breaks` list, all at `status: seed`.
- Added Labs, Build Logs, Postmortems, Now and this page.
- Added the note status system — `seed` / `working` / `stable` /
  `production-tested` — rendered from frontmatter at the top of every note.
- Moved the seventy-nine course notes under **Reference**. No URLs changed, and
  none of their content was touched.

## 2026-07-26

Repositioned the home page: projects and blog lead, notes became reference
material rather than the point of the site.

## Earlier

Before this file existed: the Networks landing page shipped after sitting
unpublished since May; the exam scaffolding was stripped out of the notes once
the course ended; the frontend was redesigned with the tag facets and LaTeX
handling fixed; the vault converter and its privacy policy were built, and the
first seventy-nine notes published through it.

Reconstructed from the commit history rather than written at the time, which is
exactly the gap this page now closes.
