---
tags:
  - topic/arrays
  - method/two-pointers
---
# Remove Element

🔗 [LeetCode](https://leetcode.com/problems/remove-element/) · **Easy** · Arrays / Two Pointers

## Prompt (in my own words)

Given an array `nums` and a value `val`, remove every occurrence of `val`
**in place** and return the new length `k`. The first `k` slots of `nums` must
hold the kept elements (any order); whatever sits past `k` doesn't matter.

## Clarifying questions

- Does the order of the kept elements matter? *(No — that's what makes the
  overwrite trick legal.)*
- Do I shrink the array, or just report `k`? *(Just `k`; the grader reads the
  first `k` slots.)*
- Could every element be `val`, or none of them? *(Yes to both — `k` may be `0`
  or `len(nums)`.)*
- Extra memory allowed? *(Aim for $O(1)$ — that's the point of "in place".)*

??? question "Try it before you scroll"
    Keep a write pointer. As a read pointer sweeps the array, what's the rule for
    when the write pointer advances?

## Approach

??? example "Brute force — O(n) time, O(n) space"
    Build a new list of everything that isn't `val`, then copy it back. Works,
    but it allocates a second array — it ignores the "in place" ask.

??? success "Optimal — two pointers, O(1) space"
    A slow write pointer `k` and a fast read pointer `i`. Sweep with `i`; each
    time `nums[i] != val`, copy it to `nums[k]` and advance `k`. Elements equal
    to `val` are skipped, so they get overwritten. At the end, `k` is the new
    length.

!!! tip "The one thing to remember"
    "Remove in place, order doesn't matter" = a **write pointer** that only
    advances on keepers. The read pointer never waits.

## Complexity

| Approach | Time | Space |
|---|---|---|
| Copy to new list | $O(n)$ | $O(n)$ |
| Two pointers | $O(n)$ | $O(1)$ |

## Solution

```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0                       # write pointer: next slot for a keeper
        for i in range(len(nums)):  # read pointer
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
```

??? example "Tests — run to check"
    ```python
    def check(nums, val):
        k = Solution().removeElement(nums, val)
        print(f"k={k}, kept={sorted(nums[:k])}")

    check([3, 2, 2, 3], 3)               # k=2, kept=[2, 2]
    check([0, 1, 2, 2, 3, 0, 4, 2], 2)   # k=5
    check([2, 2, 2], 2)                  # k=0
    ```

## Dry run

`nums = [3, 2, 2, 3]`, `val = 3`:

- `i=0` → `3 == val` → skip, `k=0`
- `i=1` → `2 != val` → `nums[0]=2`, `k=1`
- `i=2` → `2 != val` → `nums[1]=2`, `k=2`
- `i=3` → `3 == val` → skip
- return `k=2`; the first two slots are `[2, 2]` ✓

## Follow-ups

??? question "What if you also had to minimise writes?"
    Swap the element at `i` with the one at the end and shrink the range, instead
    of copying forward. Fewer writes when `val` is rare, since you only touch
    elements you actually move.

??? question "How is this the same as 'Remove Duplicates from Sorted Array'?"
    Same write-pointer skeleton — only the *keep* condition changes (there it's
    `nums[i] != nums[k-1]`).

## Retro

??? warning "What tripped me up"
    Don't mutate the list's length while scanning. The write pointer overwrites
    in place; you never delete, you just report `k`.

**Flashcard** — Q: remove-in-place when order is free? → A: a write pointer that
advances only on keepers. *(→ DSA deck)*
