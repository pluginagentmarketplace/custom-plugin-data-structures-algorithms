---
name: searching-sorting
description: Master searching and sorting algorithms. Learn binary search, comparison sorts, and non-comparison sorts. Use when optimizing search/sort performance or solving coding interview problems.
---

# Searching & Sorting Algorithms

## Quick Start

Know when to use which algorithm. Understand trade-offs between approaches.

### Algorithm Selection Guide

**For Searching:**
- **Unsorted data**: Linear search O(n)
- **Sorted data, random access**: Binary search O(log n)
- **Key-value pairs**: Hash table O(1) average

**For Sorting:**
- **Small n (<50)**: Insertion sort O(n²)
- **General purpose**: Quick sort or Merge sort O(n log n)
- **Must be stable**: Merge sort O(n log n)
- **Limited memory**: Heap sort O(n log n) in-place
- **Integer range limited**: Counting/Radix sort O(n+k)

## Searching

### Binary Search
```python
def binary_search(arr, target):
    """Find target in sorted array: O(log n)"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found
```

### Binary Search Variations

#### Find First Occurrence
```python
def find_first(arr, target):
    """Find leftmost occurrence"""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

#### Search in Rotated Array
```python
def search_rotated(arr, target):
    """Search in rotated sorted array: O(log n)"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        # Determine which side is sorted
        if arr[left] <= arr[mid]:  # Left side sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right side sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

## Sorting Algorithms

### O(n²) Sorts

#### Insertion Sort
```python
def insertion_sort(arr):
    """Best for small arrays and nearly sorted data"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
    # Time: O(n²), Space: O(1), Stable: Yes
```

#### Bubble Sort
```python
def bubble_sort(arr):
    """Simple but inefficient"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
    # Time: O(n²), Space: O(1), Stable: Yes
```

### O(n log n) Sorts

#### Merge Sort
```python
def merge_sort(arr):
    """Stable, predictable, requires O(n) space"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays: O(n)"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
    # Time: O(n log n), Space: O(n), Stable: Yes
```

#### Quick Sort
```python
def quick_sort(arr):
    """Fast in practice, in-place, cache-friendly"""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
    # Time: O(n log n) avg, O(n²) worst, Space: O(log n)
```

#### Heap Sort
```python
def heap_sort(arr):
    """In-place, guaranteed O(n log n)"""
    import heapq

    heapq.heapify(arr)  # Build min-heap: O(n)
    return [heapq.heappop(arr) for _ in range(len(arr))]
    # Time: O(n log n), Space: O(1), Stable: No
```

### Non-Comparison Sorts

#### Counting Sort
```python
def counting_sort(arr, max_value):
    """For non-negative integers with limited range"""
    count = [0] * (max_value + 1)

    # Count occurrences
    for num in arr:
        count[num] += 1

    # Build sorted array
    result = []
    for i in range(max_value + 1):
        result.extend([i] * count[i])

    return result
    # Time: O(n + k), Space: O(k), Stable: Yes
```

#### Radix Sort
```python
def radix_sort(arr):
    """Sort integers by individual digits"""
    if not arr:
        return arr

    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr
    # Time: O(nk), Space: O(n), Stable: Yes
```

## Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable | Use |
|-----------|------|---------|-------|-------|--------|-----|
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Small n |
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Educational |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Stable needed |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No | General purpose |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Guaranteed O(n log n) |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes | Integer range |
| Radix | O(nk) | O(nk) | O(nk) | O(n+k) | Yes | Multi-digit |

## Key Insights

### Why Quick Sort is Faster
- Better cache locality
- Fewer data movements
- Lower constant factors despite O(n²) worst case

### Stability Matters
- Preserves relative order of equal elements
- Important for multi-key sorting
- Merge sort is stable, Quick sort is not

### In-Place Preference
- Heap sort: in-place, O(n log n), unstable
- Merge sort: stable, O(n log n), requires extra space

## Practice Problems

1. **Binary search with edge cases**
2. **Merge sorted arrays**
3. **Sort by custom comparator**
4. **K-th largest element**
5. **Merge K sorted lists**
6. **Meeting rooms scheduling**
7. **Valid parentheses ordering**

## Key Takeaways

✓ Binary search: O(log n), requires sorted array
✓ Merge sort: Stable, predictable, O(n log n)
✓ Quick sort: Fast in practice, usually better choice
✓ Insertion sort: Best for small or nearly sorted data
✓ Counting/Radix sort: O(n) possible with integers
✓ Choose algorithm based on data and constraints
