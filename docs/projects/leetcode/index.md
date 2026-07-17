# LeetCode

Every problem here is worked as a **mock interview**, not a dumped solution:
clarify the question, think out loud from brute force to optimal, state the
complexity, write clean code, dry-run it, then handle the follow-ups. The
approach and the solution hide behind toggles, so the page works as a self-test
— try each one before you reveal it.
{: .gx-lede }

## How I grade myself

The code passing isn't the bar — the *interview* is. After each problem I check:

| Signal | What "good" looks like |
|---|---|
| Communication | I said the plan out loud before typing |
| Clarifying | I asked about constraints and edge cases first |
| Brute → optimal | I named the naive version and why I moved off it |
| Complexity | I stated time and space *before* coding |
| Correctness | Clean run, edge cases handled |
| Follow-ups | I could extend it when the interviewer pushed |

Result legend, same as my tracker: ✅ solved clean · ⚠️ solved with hints ·
❌ couldn't do it — and every ❌ becomes a flashcard.

## Problems

| Date | Problem | Pattern | Difficulty | Result |
|---|---|---|---|---|
| 2026-07-16 | [Two Sum](two-sum.md) | Hashmap | Easy | ✅ |
| 2026-07-16 | [Remove Element](remove-element.md) | Two pointers | Easy | ✅ |

## Patterns cheat-sheet

- **Two pointers** — sorted array, pair sums, in-place dedup / overwrite.
- **Sliding window** — longest / shortest substring under a constraint.
- **Hashmap** — seen-before, frequency counts, complement lookup.
- **BFS** — shortest path / level order · **DFS** — all paths, connectivity.
- **DP** — "count ways / min cost / can we?" with overlapping subproblems.
- **Backtracking** — permutations, combinations, subsets, board placement.

## Pattern drills

??? question "When should a hashmap be your first instinct?"
    When the problem asks "have I seen this before?", needs frequency counts, or
    wants a complement / pair lookup in $O(1)$. Two Sum is the archetype.

??? question "What signals a sliding window?"
    A contiguous subarray or substring, plus a constraint to keep satisfied
    ("longest with ≤ k distinct", "smallest sum ≥ target"). Grow the right edge,
    shrink the left when the constraint breaks.

??? question "BFS vs DFS — how do I pick?"
    Shortest path / fewest steps / level-by-level → BFS with a queue. Enumerate
    all paths, test connectivity, or recurse over structure → DFS with a stack or
    recursion.

---

**Adding a problem:** copy `_template.md`, fill it in, and add one line under
`Projects → LeetCode` in `mkdocs.yml`.
{: .gx-fine }
