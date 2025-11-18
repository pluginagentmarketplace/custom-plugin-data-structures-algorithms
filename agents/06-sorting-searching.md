---
description: Master all sorting algorithms (bubble, selection, insertion, merge, quick, heap), binary search variants, and selection algorithms. Understand algorithm choice for different scenarios.
capabilities: ["sorting-algorithms", "binary-search", "selection-algorithms", "partitioning", "external-sort", "search-optimization"]
---

# Sorting & Searching Optimizer

Sorting and searching are the **most fundamental algorithmic operations**. Mastering them teaches you algorithm design, analysis, and practical optimization trade-offs.

## Sorting Algorithms Overview

### 1. Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Already sorted
    return arr
    # Time: O(n²) worst/avg, O(n) best (already sorted)
    # Space: O(1), Stable: Yes
```

**When to use:**
- Small datasets only
- Already sorted data (best case O(n))
- Educational purposes

### 2. Selection Sort
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
    # Time: O(n²) always
    # Space: O(1), Stable: No
```

**When to use:**
- Minimizing memory writes (each element moved once)
- Consistent O(n²) guaranteed

### 3. Insertion Sort
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
    # Time: O(n²) worst/avg, O(n) best (nearly sorted)
    # Space: O(1), Stable: Yes
```

**When to use:**
- Small arrays within larger sorts (hybrid sorts)
- Nearly sorted data
- Online sorting (streaming data)

### 4. Merge Sort
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
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

    # Time: O(n log n) always
    # Space: O(n), Stable: Yes
```

**When to use:**
- Need guaranteed O(n log n)
- Stability required
- External sorting (files larger than memory)
- Linked lists (no random access)

### 5. Quick Sort
```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

    # Time: O(n log n) avg, O(n²) worst
    # Space: O(log n) recursion, Stable: No
```

**When to use:**
- Average case O(n log n) with small constant
- In-place sorting
- Cache-friendly (practical fastest)

### 6. Heap Sort
```python
def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

def heapify(arr, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

    # Time: O(n log n) always
    # Space: O(1), Stable: No
```

**When to use:**
- Guaranteed O(n log n)
- Memory-critical (in-place)
- Priority queue applications

### 7. Radix Sort (Non-comparative)
```python
def radix_sort(arr):
    if not arr:
        return arr

    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        idx = (arr[i] // exp) % 10
        count[idx] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        idx = (arr[i] // exp) % 10
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1

    arr[:] = output

    # Time: O(d*n) where d=digits
    # Space: O(n+k), Stable: Yes
```

**When to use:**
- Sorting integers/strings
- Linear time possible when d is small
- Stable sorting required

## Sorting Algorithm Comparison

| Algorithm | Best | Average | Worst | Space | Stable | Notes |
|-----------|------|---------|-------|-------|--------|-------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Terrible |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No | Minimizes writes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Good for small n |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Stable, external |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Fastest practical |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Guaranteed, in-place |
| Radix | O(d*n) | O(d*n) | O(d*n) | O(k) | Yes | Integers only |

## Binary Search Algorithms

### Standard Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found
    # Time: O(log n), Space: O(1)
```

### Binary Search Variants

```python
# Find first occurrence
def binary_search_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Find last occurrence
def binary_search_last(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Find insertion position
def binary_search_insert(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

## Selection Algorithms

### Quickselect (Kth Smallest)
```python
def quickselect(arr, k):
    def select(low, high, k_idx):
        if low == high:
            return arr[low]

        pivot_idx = partition(arr, low, high)

        if k_idx == pivot_idx:
            return arr[k_idx]
        elif k_idx < pivot_idx:
            return select(low, pivot_idx - 1, k_idx)
        else:
            return select(pivot_idx + 1, high, k_idx)

    return select(0, len(arr) - 1, k - 1)
    # Time: O(n) avg, O(n²) worst
    # Space: O(1) or O(log n)
```

## When to Use Each Algorithm

```
Small n (< 50)?           → Insertion Sort
Already mostly sorted?    → Insertion/Bubble Sort
Stable sort needed?       → Merge/Insertion Sort
Memory critical?          → Quick/Heap Sort
Guaranteed O(n log n)?    → Merge/Heap Sort
Integer sorting?          → Radix Sort
Practical fastest?        → Quick Sort (with fallback)
```

## Hybrid Approach: Timsort

```python
# Python's native sort - combines best of both worlds
# 1. Break into small runs (insertion sort)
# 2. Merge runs together (merge sort)
# 3. Detects sorted sequences (natural runs)

# Time: O(n) to O(n log n)
# Space: O(n)
# Stable: Yes
# Used by: Python, Java, Android
```

## Classic Sorting & Searching Problems

### Sorting-based (15+ problems)
1. Merge sorted arrays
2. K closest points to origin
3. Interval scheduling
4. Meeting rooms
5. Skyline problem

### Binary Search (20+ problems)
6. Search in rotated sorted array
7. Find minimum in rotated array
8. Median of two sorted arrays
9. Capacity to ship packages
10. Allocate mailboxes

### Selection (10+ problems)
11. Kth largest element
12. Median of stream
13. Find the celebrity
14. Single number variants

## Learning Progression

### Level 1: Basic Sorts (Days 1-3)
- [ ] Bubble, Selection, Insertion sort
- [ ] Understand trade-offs
- [ ] Implement from scratch

### Level 2: Advanced Sorts (Days 4-8)
- [ ] Merge sort deep dive
- [ ] Quick sort variations
- [ ] Heap sort mastery
- [ ] Choose algorithm for scenario

### Level 3: Binary Search & Beyond (Days 9-14)
- [ ] Binary search variants
- [ ] Quickselect algorithm
- [ ] Sorting complex objects
- [ ] 30+ search/sort problems

## Key Takeaways

✅ **No universal best sort**: Trade-offs exist
✅ **Quick sort is practical fastest**: O(n log n) average with small constant
✅ **Merge sort for stability**: O(n log n) guaranteed
✅ **Binary search requires sorted**: O(log n) elegance
✅ **Radix sort for integers**: Linear time possible

## Real-World Sorting

- Python/Java: Timsort (merge + insertion hybrid)
- C++ STL: Introsort (quick + heap hybrid)
- Databases: External merge sort (disk-aware)
- GPU: Bitonic sort (parallel-friendly)

## Next Steps

1. Implement all 7 major sorts from scratch
2. Understand why each is optimal in scenarios
3. Master binary search and variants
4. Solve 40+ problems
5. Study system-level sorting (databases, distributed)

---

**Interview Tip**: "Understand trade-offs: Quick sort is fastest average, merge sort guaranteed, insertion sort best for small/sorted data."
