---
name: binary-search
description: Master binary search. Variations, edge cases, and applications. O(log n) searching in sorted data.
---

# Binary Search

## Standard Pattern
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## Variations
- First occurrence
- Last occurrence
- Rotated array
- Peak finding
- Range searching

## Complexity
- Time: O(log n)
- Space: O(1)

## Requirements
- Input must be sorted
- Works with integers, strings, custom objects

## Key Insight
Divide search space in half each iteration
