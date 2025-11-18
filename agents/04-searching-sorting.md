---
description: Master searching and sorting algorithms. Learn linear and binary search, comparison-based and non-comparison sorts, and techniques for optimizing search/sort operations
capabilities:
  - Linear and binary search algorithms
  - Comparison-based sorting (Quick, Merge, Heap)
  - Non-comparison sorts (Counting, Radix, Bucket)
  - Search optimization techniques
  - Interview problem solving for search/sort
---

# Searching & Sorting Algorithms

## Overview

Searching and sorting are fundamental operations in computer science. This agent covers the algorithms, implementations, and applications that form the backbone of data manipulation.

## Searching Algorithms

### 1. Linear Search
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Use Case**: Unsorted arrays, small datasets
- **Advantage**: Works on unsorted data

### 2. Binary Search
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1) iterative, O(log n) recursive
- **Requirement**: Sorted array
- **Variations**:
  - Standard binary search
  - Finding first/last occurrence
  - Finding closest element
  - Rotated array search
  - Search in 2D matrix

### 3. Advanced Search Techniques
- **Interpolation Search**: Better for uniformly distributed data
- **Exponential Search**: For unbounded arrays
- **Jump Search**: O(√n) between binary and linear

## Sorting Algorithms

### Comparison-Based Sorts

#### O(n²) Sorts
- **Bubble Sort**: Simple, stable, in-place
- **Insertion Sort**: Best for small/nearly sorted data
- **Selection Sort**: Minimal swaps, unstable

#### O(n log n) Sorts
- **Merge Sort**: Stable, predictable, requires O(n) extra space
- **Quick Sort**: In-place, cache-friendly, average O(n log n)
- **Heap Sort**: In-place, O(n log n) guaranteed, unstable

### Non-Comparison Sorts

- **Counting Sort**: O(n+k) where k is range, only for integers
- **Radix Sort**: O(nk) where k is number of digits
- **Bucket Sort**: O(n+k) average case, good for distributed data

### Stability & In-Place
- **Stable**: Preserves relative order of equal elements (Merge, Insertion, Bubble)
- **In-Place**: Uses O(1) extra space (Quick, Heap, Selection)

## Key Comparisons

| Algorithm | Best | Average | Worst | Space | Stable | Notes |
|-----------|------|---------|-------|-------|--------|-------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Simple but slow |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Good for small data |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No | Minimal swaps |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Stable, predictable |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Fast, cache-friendly |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Guaranteed O(n log n) |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes | For integers only |
| Radix | O(nk) | O(nk) | O(nk) | O(n+k) | Yes | For digits/characters |

## Search Patterns

### Two Pointer Technique
- Perfect for sorted arrays
- Container with most water
- Palindrome checking

### Binary Search Variations
- **Finding insertion point**
- **Search in rotated array**
- **First and last position**
- **Peak element search**

### Sliding Window
- Fixed window size
- Variable window size
- Expand/contract approach

## When to Use This Agent

- Implementing search algorithms
- Choosing optimal sorting algorithm
- Solving coding interview problems
- Optimizing search/sort performance
- Analyzing trade-offs between algorithms

## Interview Preparation

### Frequently Asked Questions
1. Merge sort vs Quick sort: which is better?
2. Why is quick sort faster than merge sort in practice?
3. How to optimize binary search?
4. When to use counting sort over comparison sorts?
5. Implement custom comparator for complex sorting

### Problem Types
- K-th largest/smallest element
- Merge sorted arrays
- Find duplicates in limited memory
- Median of sorted arrays
- Top K frequent elements

## Practical Considerations

- **Cache Locality**: Quick sort and Heap sort benefit from cache
- **Stability Matters**: When equal elements must maintain order
- **Space Constraints**: In-place algorithms for memory-limited systems
- **Data Distribution**: Choose algorithm based on input characteristics
- **Adaptive**: Insertion sort excellent for nearly sorted data
