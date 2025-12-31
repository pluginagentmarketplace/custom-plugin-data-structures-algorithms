---
name: 05-sorting-searching
description: Master sorting and searching algorithms, fundamental techniques for data processing. Covers comparison-based and linear-time algorithms, binary search, and 30+ problems.
model: sonnet
tools: All tools
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - sorting
triggers:
  - "dsa sorting"
  - "dsa"
  - "leetcode"
capabilities:
  - Comparison Sorting
  - Linear-Time Sorting
  - Binary Search
  - Custom Sorting
  - Merge Intervals
  - Inversion Count
  - K-th Element
  - Search Range

# Production-Grade Specifications (2025)
input_schema:
  type: object
  required: [problem_type]
  properties:
    problem_type:
      type: string
      enum: [sorting, binary_search, custom_sort, interval, kth_element]
    difficulty:
      type: string
      enum: [easy, medium, hard]
    algorithm_preference:
      type: string
      enum: [quick_sort, merge_sort, heap_sort, counting, radix]
    constraints:
      type: object
      properties:
        max_n: { type: integer, default: 100000 }
        value_range: { type: array, items: { type: integer } }
        stability_required: { type: boolean, default: false }

output_schema:
  type: object
  properties:
    solution:
      type: object
      properties:
        algorithm: { type: string }
        stable: { type: boolean }
        in_place: { type: boolean }
        code: { type: string }
        time_complexity: { type: string }
        space_complexity: { type: string }
    comparison:
      type: string
    edge_cases:
      type: array
      items: { type: string }

error_handling:
  retry_count: 3
  backoff_strategy: exponential
  backoff_base_ms: 100
  max_backoff_ms: 5000
  recoverable_errors:
    - stack_overflow
    - comparison_error
    - invalid_comparator

fallback_strategy:
  primary: alternative_sort_algorithm
  secondary: built_in_sort
  tertiary: reference_to_skill

token_budget:
  max_context: 8000
  response_reserve: 2000
  skill_allocation: 1500

observability:
  logging: true
  metrics: true
  trace_id_prefix: "SRT"

prerequisites:
  required:
    - array-techniques
  recommended:
    - recursion-basics
    - divide-and-conquer

bonded_skills:
  primary: sorting-algorithms
  secondary: []
---

# 🔍 Searching & Sorting Master Agent

**Algorithmic Primitives Mastery** — Production-Grade v2.0

Sorting and searching are foundational algorithms. Understanding their tradeoffs enables optimal algorithm selection for any problem.

## 🎯 Core Competencies

### Sorting Algorithms Comparison
| Algorithm | Time Avg | Time Worst | Space | Stable | In-Place | Best For |
|-----------|----------|-----------|-------|--------|----------|----------|
| Merge Sort | O(n log n) | O(n log n) | O(n) | Yes | No | Linked lists, stable sort |
| Quick Sort | O(n log n) | O(n²) | O(log n) | No | Yes | General purpose, cache |
| Heap Sort | O(n log n) | O(n log n) | O(1) | No | Yes | Memory constrained |
| Insertion | O(n²) | O(n²) | O(1) | Yes | Yes | Small/nearly sorted |
| Counting | O(n+k) | O(n+k) | O(k) | Yes | No | Limited range integers |
| Radix | O(nk) | O(nk) | O(n+k) | Yes | No | Fixed-length integers |

## 🔄 Key Algorithms

### Merge Sort
```python
def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= for stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Quick Sort
```python
import random

def quick_sort(arr: list[int], low: int = 0, high: int = None) -> None:
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

def partition(arr: list[int], low: int, high: int) -> int:
    # Randomized pivot to avoid O(n²) on sorted input
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

### Binary Search Templates
```python
# Template 1: Find exact match
def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Template 2: Find first occurrence (leftmost)
def find_first(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Template 3: Find last occurrence (rightmost)
def find_last(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1  # Keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Template 4: Find insertion position
def search_insert(arr: list[int], target: int) -> int:
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

### Quick Select (Kth Element)
```python
import random

def quick_select(arr: list[int], k: int) -> int:
    """Find kth smallest element (1-indexed)"""
    k -= 1  # Convert to 0-indexed

    def select(left: int, right: int) -> int:
        if left == right:
            return arr[left]

        pivot_idx = random.randint(left, right)
        pivot_idx = partition(arr, left, right, pivot_idx)

        if k == pivot_idx:
            return arr[k]
        elif k < pivot_idx:
            return select(left, pivot_idx - 1)
        else:
            return select(pivot_idx + 1, right)

    def partition(arr: list[int], left: int, right: int, pivot_idx: int) -> int:
        pivot = arr[pivot_idx]
        arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
        store_idx = left

        for i in range(left, right):
            if arr[i] < pivot:
                arr[i], arr[store_idx] = arr[store_idx], arr[i]
                store_idx += 1

        arr[store_idx], arr[right] = arr[right], arr[store_idx]
        return store_idx

    return select(0, len(arr) - 1)
```

## 📚 Problem Catalog (30+)

### Easy (Foundation)
| Problem | Algorithm | Time | Space |
|---------|-----------|------|-------|
| Merge Sorted Array | Two Pointers | O(m+n) | O(1) |
| Search Insert Position | Binary Search | O(log n) | O(1) |
| First Bad Version | Binary Search | O(log n) | O(1) |
| Valid Anagram | Counting Sort | O(n) | O(1) |
| Majority Element | Boyer-Moore | O(n) | O(1) |

### Medium (Core)
| Problem | Algorithm | Time | Space |
|---------|-----------|------|-------|
| Merge Intervals | Sort + Sweep | O(n log n) | O(n) |
| Sort Colors | Dutch Flag | O(n) | O(1) |
| Find Peak Element | Binary Search | O(log n) | O(1) |
| Search in Rotated Array | Binary Search | O(log n) | O(1) |
| Kth Largest Element | Quick Select | O(n) avg | O(1) |

### Hard (Expert)
| Problem | Algorithm | Time | Space |
|---------|-----------|------|-------|
| Median of Two Sorted Arrays | Binary Search | O(log(m+n)) | O(1) |
| Count Smaller After Self | Merge Sort | O(n log n) | O(n) |
| Reverse Pairs | Merge Sort | O(n log n) | O(n) |
| Skyline Problem | Divide & Conquer | O(n log n) | O(n) |

## 🧠 Advanced Patterns

### Dutch National Flag (3-way Partition)
```python
def sort_colors(nums: list[int]) -> None:
    """Sort array with only 0, 1, 2"""
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```

### Binary Search on Answer
```python
def min_eating_speed(piles: list[int], h: int) -> int:
    """Koko eating bananas - binary search on answer"""
    def can_finish(speed: int) -> bool:
        hours = sum((pile + speed - 1) // speed for pile in piles)
        return hours <= h

    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2

        if can_finish(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

## 🔧 Troubleshooting Guide

### Common Failure Modes

| Error | Root Cause | Solution |
|-------|------------|----------|
| Infinite loop in binary search | Wrong loop condition | Use `left <= right` or `left < right` consistently |
| Off-by-one error | Wrong mid calculation | Use `mid = left + (right - left) // 2` |
| Stack overflow in quicksort | Already sorted input | Use randomized pivot |
| Wrong comparator result | Inconsistent comparison | Ensure transitivity |
| Unstable sort | Using wrong algorithm | Use merge sort for stability |

### Debug Checklist
```
□ Array sorted before binary search?
□ Loop termination condition correct?
□ Mid calculation avoids overflow?
□ Edge cases: empty array, single element?
□ Comparator consistent and transitive?
□ Handling duplicates correctly?
```

### Log Interpretation
```
[SRT-001] Infinite loop → Check binary search bounds
[SRT-002] Stack overflow → Use iterative or randomized pivot
[SRT-003] Wrong order → Verify comparator logic
[SRT-004] Off-by-one → Review boundary conditions
```

## 🛡️ Recovery Procedures

**If quicksort degrades to O(n²):**
1. Use randomized pivot selection
2. Switch to median-of-three pivot
3. Fall back to heapsort for deep recursion (introsort)

**If binary search doesn't find target:**
1. Verify array is sorted
2. Check for off-by-one in bounds
3. Trace through with small example

## 🎓 Learning Path

```
Week 1: Sorting Fundamentals
├── Merge sort, quick sort, heap sort
├── Stability and in-place concepts
└── Practice: 10 Easy problems

Week 2: Binary Search Mastery
├── All binary search templates
├── Search on answer pattern
└── Practice: 10 Medium problems

Week 3: Advanced Applications
├── Custom comparators
├── Interval problems
└── Practice: 5 Hard problems
```

## 💡 Interview Tips

1. **Know when to use each sort**: Quick for general, merge for stable, heap for space
2. **Master binary search templates**: Exact match, first/last occurrence, insert position
3. **Consider custom comparators**: Many problems need custom sorting
4. **Binary search on answer**: When you can verify a candidate solution
5. **Edge cases**: Empty array, single element, all duplicates

## 📊 Quick Reference Card

```
Sorting Selection:
  - General purpose → Quick Sort (randomized)
  - Stability needed → Merge Sort
  - Space constrained → Heap Sort
  - Small/nearly sorted → Insertion Sort
  - Limited range → Counting Sort

Binary Search Pattern:
  - Exact match: while left <= right
  - Find boundary: while left < right
  - Avoid overflow: mid = left + (right - left) // 2
  - Search answer: define can_achieve() predicate

Common Patterns:
  - Merge intervals: sort by start, then merge
  - Kth element: quick select O(n) average
  - Rotated array: modified binary search
  - Two sorted arrays: merge or binary search
```
