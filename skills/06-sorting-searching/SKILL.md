---
name: sorting-searching-skill
description: All major sorting algorithms (bubble, selection, insertion, merge, quick, heap, radix), binary search variants, and selection algorithms with complexity analysis.
---

# Sorting & Searching Skill

## Quick Start

**When to use each sort:**
- **Small n (< 50)**: Insertion sort
- **Nearly sorted**: Insertion sort
- **Stable required**: Merge sort
- **In-place needed**: Quick sort or Heap sort
- **Integers**: Radix sort
- **Practical fastest**: Quick sort

## Sorting Algorithms

### 1. Bubble Sort - O(n²)

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
            break  # Early exit if sorted
    return arr

# Best: O(n) [already sorted]
# Average: O(n²)
# Worst: O(n²)
# Space: O(1)
# Stable: Yes
```

### 2. Selection Sort - O(n²)

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

# Best: O(n²)
# Average: O(n²)
# Worst: O(n²)
# Space: O(1)
# Stable: No
# Good for: Minimizing memory writes
```

### 3. Insertion Sort - O(n²)

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

# Best: O(n) [already sorted]
# Average: O(n²)
# Worst: O(n²)
# Space: O(1)
# Stable: Yes
# Good for: Small arrays, nearly sorted data
```

### 4. Merge Sort - O(n log n)

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

# Best: O(n log n)
# Average: O(n log n)
# Worst: O(n log n)
# Space: O(n)
# Stable: Yes
# Good for: External sorting, linked lists, guaranteed O(n log n)
```

### 5. Quick Sort - O(n log n) average

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

# Best: O(n log n) [balanced pivot]
# Average: O(n log n)
# Worst: O(n²) [bad pivot]
# Space: O(log n) [recursion]
# Stable: No
# Good for: Practical fastest, in-place
```

### 6. Heap Sort - O(n log n)

```python
def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
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

# Best: O(n log n)
# Average: O(n log n)
# Worst: O(n log n)
# Space: O(1)
# Stable: No
# Good for: Guaranteed O(n log n), in-place
```

### 7. Radix Sort - O(d*n)

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

# Time: O(d * n) where d = number of digits
# Space: O(n + k) where k = 10
# Stable: Yes
# Good for: Integers, linear time
```

## Sorting Comparison

| Algorithm | Best | Avg | Worst | Space | Stable | Use |
|-----------|------|-----|-------|-------|--------|-----|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Small n |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No | Min writes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Small n |
| Merge | O(nlogn) | O(nlogn) | O(nlogn) | O(n) | Yes | External |
| Quick | O(nlogn) | O(nlogn) | O(n²) | O(logn) | No | Practical |
| Heap | O(nlogn) | O(nlogn) | O(nlogn) | O(1) | No | Guaranteed |
| Radix | O(dn) | O(dn) | O(dn) | O(n) | Yes | Integers |

## Binary Search

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

### Find First Occurrence

```python
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
```

### Find Last Occurrence

```python
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
```

### Find Insertion Position

```python
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

## Hybrid Approaches

### Timsort (Python's native)

```
1. Break into runs (insertion sort)
2. Merge runs (merge sort)
3. Detect natural runs (already sorted)

Properties:
- Time: O(n) to O(n log n)
- Space: O(n)
- Stable: Yes
- Used by: Python, Java, Android
```

## Practice Strategy

**Week 1:**
- [ ] Implement all 7 sorts from scratch
- [ ] Understand trade-offs
- [ ] Test with different inputs

**Week 2:**
- [ ] Master binary search variations
- [ ] Implement quickselect
- [ ] Solve 20+ search problems

**Week 3:**
- [ ] System design with sorting
- [ ] Choose algorithm for constraints
- [ ] Optimize time/space

## Key Rules

✅ **No universal best sort**: Trade-offs exist always
✅ **Quick sort is practical fastest**: O(n log n) average
✅ **Merge sort for stability**: Guaranteed O(n log n)
✅ **Insertion for small/sorted**: Cache-friendly
✅ **Binary search requires sorted**: Must sort first!

---

**Master sorting and searching - they power everything!**
