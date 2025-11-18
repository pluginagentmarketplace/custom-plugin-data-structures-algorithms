---
name: complexity-basics
description: Learn Big O notation fundamentals, understand O(1), O(n), O(log n), and O(n²) complexity with intuitive examples. Perfect for beginners. Use when first learning complexity analysis or need quick reference for basic notation.
---

# Complexity Basics

## Quick Start: The Essentials

Big O notation describes **how algorithm time/space grows** as input size increases. Think of it as "worst-case performance."

### The Five Essential Classes

**O(1) - Constant Time**
- Example: Accessing array element by index
- Time: Always same, no matter input size
- Real example: `arr[5]` always takes same time

**O(n) - Linear Time**
- Example: Finding element in unsorted array
- Time: Grows proportionally with input size
- Real example: Loop through n items once

**O(log n) - Logarithmic Time**
- Example: Binary search in sorted array
- Time: Grows very slowly (halving problem each step)
- Real example: Searching 1 million items in ~20 steps

**O(n²) - Quadratic Time**
- Example: Bubble sort, nested loops
- Time: Grows rapidly with input size
- Real example: Checking all pairs of items

**O(n log n) - Linearithmic Time**
- Example: Most efficient general sorting (merge sort, quick sort)
- Time: Between linear and quadratic
- Real example: Divide and conquer sorting

## Understanding the Notation

### Why We Use Big O
- **Ignore constants**: 2n, 100n, 1000n all → O(n)
- **Ignore lower terms**: n² + 2n + 5 → O(n²)
- **Focus on growth rate**: What matters at scale

### Reading Big O
- O(n) = "Oh of n" or "Big O n"
- Describes worst-case behavior
- Ignores constants and lower-order terms

## Code Examples

### O(1) - Constant
```python
def get_first(arr):
    return arr[0]  # Always one operation
```

### O(n) - Linear
```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:  # Loop runs n times
        if num > max_val:
            max_val = num
    return max_val
```

### O(log n) - Logarithmic
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Cut search space in half
        else:
            right = mid - 1  # Cut search space in half
    return -1
```

### O(n²) - Quadratic
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Loop n times
        for j in range(n - 1):  # Loop n times
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

### O(n log n) - Linearithmic
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Recursive: log n depth
    right = merge_sort(arr[mid:])  # Recursive: log n depth

    return merge(left, right)  # Merge: n operations
```

## Practical Complexity Guide

### Input Size Impact
- n = 10: Most algorithms work
- n = 100: Still fast
- n = 1,000: Needs O(n) or O(n log n)
- n = 1,000,000: Must be O(1), O(log n), or O(n)
- n = 1,000,000,000: Only O(1) or O(log n)

### Time Estimates (10⁸ operations/second)
| Complexity | n=10 | n=100 | n=1K | n=10K | n=100K | n=1M |
|---|---|---|---|---|---|---|
| O(1) | 1 ns | 1 ns | 1 ns | 1 ns | 1 ns | 1 ns |
| O(log n) | 3 ns | 7 ns | 10 ns | 13 ns | 17 ns | 20 ns |
| O(n) | 100 ns | 1 μs | 10 μs | 100 μs | 1 ms | 10 ms |
| O(n log n) | 30 ns | 700 ns | 100 μs | 1.3 ms | 17 ms | 200 ms |
| O(n²) | 1 μs | 100 μs | 10 ms | 1 sec | 100 sec | Too slow |

## Key Insights

✓ **Ignore constants early**: Premature optimization is evil
✓ **Focus on growth rate**: 1000n grows same as n for Big O
✓ **Understand trade-offs**: More space for less time, or vice versa
✓ **Test assumptions**: Real hardware != theory always
✓ **Consider input size**: Your constraints matter

## Common Mistakes

❌ "O(2n) is different from O(n)"
✅ Both are O(n) - constants ignored

❌ "O(n log n) is always better than O(n²)"
✅ For large n yes, but O(n²) with small constants may be faster for small inputs

❌ "I only care about time complexity"
✅ Space matters too - you might run out of memory

## Practice Problems

1. What's the complexity of `for i in range(n): for j in range(i): pass`?
2. What's the complexity of binary search?
3. Is accessing element i in linked list O(1)?
4. What's the complexity of `" ".join([str(i) for i in range(n)])`?

## Next Steps

→ Move to `loop-analysis` for nested loop mastery
→ Move to `recursion-fundamentals` for recursive complexity
→ Combine all in real problem solving
