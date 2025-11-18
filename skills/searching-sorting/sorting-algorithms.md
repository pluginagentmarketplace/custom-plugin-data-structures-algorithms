---
name: sorting-algorithms
description: Compare sorting algorithms. Merge sort, quick sort, heap sort. Understand trade-offs: stability, in-place, comparison-based.
---

# Sorting Algorithms

## Merge Sort
- Time: O(n log n) guaranteed
- Space: O(n)
- Stable: Yes
- Use: When stability required

## Quick Sort
- Time: O(n log n) avg, O(n²) worst
- Space: O(log n)
- Stable: No
- Use: General purpose, in-place

## Heap Sort
- Time: O(n log n) guaranteed
- Space: O(1)
- Stable: No
- Use: When guaranteed O(n log n) needed

## Counting Sort
- Time: O(n+k)
- Space: O(k)
- Only for integers
- Use: Small range integers

## Key Decision
- Stability matters? → Merge sort
- Space limited? → Heap sort or in-place quick sort
- General use? → Quick sort
- Integers only? → Counting/Radix sort
