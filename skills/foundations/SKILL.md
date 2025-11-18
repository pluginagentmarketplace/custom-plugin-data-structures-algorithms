---
name: foundations
description: Master Big O notation, asymptotic analysis, time/space complexity calculation, and algorithm efficiency fundamentals. Use when analyzing algorithm performance, comparing approaches, or studying complexity analysis.
---

# Foundations & Complexity Analysis

## Quick Start

Understanding Big O notation is essential for algorithmic thinking. Use this skill when you need to analyze any algorithm's efficiency.

### Big O Classes Ranking
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

### Quick Estimation by Input Size
- **n = 10**: Can handle O(n³) or even O(n⁴)
- **n = 100**: O(n²) is acceptable, O(n³) risky
- **n = 1,000**: Need O(n log n) or better
- **n = 10,000**: Must be O(n log n) or O(n)
- **n = 100,000**: Only O(n) or O(log n)
- **n = 1,000,000**: Extreme optimization needed

## Core Concepts

### Time Complexity Analysis
1. Count basic operations (assignments, comparisons, arithmetic)
2. Identify loops and nested loops
3. Find dominant term(s)
4. Ignore lower-order terms and constants

### Space Complexity Analysis
1. Data structure space (arrays, objects)
2. Recursion call stack depth
3. Temporary variables and buffers
4. Auxiliary data structures

## Examples

### O(1) - Constant Time
```python
def get_first_element(arr):
    return arr[0]  # Always one operation
```

### O(n) - Linear Time
```python
def linear_search(arr, target):
    for elem in arr:  # Loop through all n elements
        if elem == target:
            return True
    return False
```

### O(n²) - Quadratic Time
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Outer loop: n times
        for j in range(n-1):  # Inner loop: n times
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

### O(log n) - Logarithmic Time
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:  # Divides search space by 2 each iteration
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
```

### O(n log n) - Linearithmic Time
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # O(log n) depth
    right = merge_sort(arr[mid:]) # O(log n) depth
    return merge(left, right)  # O(n) merge at each level
    # Total: O(n log n)
```

## Complexity Comparison Table

| Complexity | Operations at n=1000 | Operations at n=1M | Verdict |
|------------|----------------------|-------------------|---------|
| O(1) | 1 | 1 | Excellent |
| O(log n) | 10 | 20 | Excellent |
| O(n) | 1,000 | 1,000,000 | Great |
| O(n log n) | 10,000 | 20,000,000 | Good |
| O(n²) | 1,000,000 | 10¹² | Poor for large n |
| O(2ⁿ) | 2¹⁰⁰⁰ | Impossible | Only for small n |

## Best/Average/Worst Case

### Example: Linear Search
- **Best Case**: O(1) - Element at first position
- **Average Case**: O(n) - Element somewhere in middle
- **Worst Case**: O(n) - Element at end or not found

### Example: Quick Sort
- **Best Case**: O(n log n) - Balanced pivot partition
- **Average Case**: O(n log n) - Random pivots
- **Worst Case**: O(n²) - Pivot always at edge (sorted array)

## Space Complexity

### Stack Space from Recursion
```python
def recursive_sum(arr, index=0):
    if index >= len(arr):
        return 0
    return arr[index] + recursive_sum(arr, index + 1)
    # Space: O(n) due to call stack depth
```

### Auxiliary Space
```python
def merge_sort(arr):
    # Creates temporary arrays during merge
    # Total auxiliary space: O(n)
    ...
```

## Practice Problems

1. **Calculate the time complexity of nested loops**
2. **Identify whether binary search applies**
3. **Compare algorithm choices for given constraints**
4. **Optimize algorithm from O(n²) to O(n log n)**
5. **Analyze recursive function complexity**

## Key Takeaways

✓ Big O describes algorithm behavior as input grows
✓ Ignore constants and lower-order terms
✓ Consider best, average, and worst cases
✓ Match algorithm complexity to input size constraints
✓ Space complexity matters in memory-limited systems
✓ Practical testing sometimes reveals surprises
