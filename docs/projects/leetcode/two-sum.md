---
tags:
  - topic/arrays
  - method/hashmap
---
# Two Sum

🔗 [LeetCode](https://leetcode.com/problems/two-sum/) · **Easy** · Arrays / Hashmap

## Prompt (in my own words)

Given an array of integers and a target, return the **indices** of the two
numbers that add up to the target. Assume exactly one solution, and you can't
use the same index twice.

## Clarifying questions

- Is the array sorted? *(No — so a two-pointer scan would need a sort first,
  which loses the original indices.)*
- Exactly one valid pair, or could there be none or several?
- Can I reuse the same element? *(No.)*
- Any negatives or duplicates? *(Yes to both — the approach has to survive them.)*

??? question "Try it before you scroll"
    You get one pass. What would let you answer "have I already seen the number
    that completes this pair?" in $O(1)$?

## Approach

??? example "Brute force — O(n²)"
    Check every pair `(i, j)` with two nested loops. Correct, but quadratic.

??? success "Optimal — O(n) with a hashmap"
    Walk the array once, keeping a map of `value → index` for everything seen so
    far. For each `n`, the number that completes the pair is `target - n`. If
    that complement is already in the map, you've found the answer; otherwise
    record `n` and move on.

!!! tip "The one thing to remember"
    A hashmap turns "have I seen the complement?" into an $O(1)$ lookup. That's
    the core move behind almost every pair-sum problem.

## Complexity

| Approach | Time | Space |
|---|---|---|
| Brute force | $O(n^2)$ | $O(1)$ |
| Hashmap | $O(n)$ | $O(n)$ |

## Solution

```python
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}  # value -> index
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []
```

??? example "Tests — run to check"
    ```python
    cases = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6),       [1, 2]),
        (([3, 3], 6),          [0, 1]),
    ]
    for args, expected in cases:
        got = two_sum(*args)
        print(f"{'✅' if got == expected else '❌'} two_sum{args} = {got}  (expected {expected})")
    ```

## Dry run

`nums = [2, 7, 11, 15]`, `target = 9`:

- `i=0, n=2` → need `7`, not in map → `seen = {2: 0}`
- `i=1, n=7` → need `2`, it's in the map → return `[0, 1]` ✓

## Follow-ups

??? question "What if the array were already sorted?"
    Two pointers from both ends: sum too big → move the right pointer in, too
    small → move the left pointer out. $O(1)$ space. Catch: you'd lose the
    original indices, so you'd sort `(value, index)` pairs first.

??? question "What about 3-sum?"
    Fix one element and run this two-sum on the rest → $O(n^2)$ overall. Sorting
    first makes it easy to skip duplicates.

## Retro

??? warning "What tripped me up"
    Recording `seen[n] = i` has to come **after** the complement check. Do it
    before, and an element can pair with itself.

**Flashcard** — Q: pair-sum in one pass? → A: hashmap `value → index`, check the
complement *before* inserting. *(→ DSA deck)*
