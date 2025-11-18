---
name: complexity-analysis-skill
description: Master Big-O notation, time and space complexity analysis, amortized complexity, and algorithm efficiency measurement. Essential for understanding algorithmic tradeoffs and choosing optimal solutions.
---

# Complexity Analysis Skill

## Quick Start

Complexity analysis answers: "How does algorithm performance scale with input size?"

### The Big-O Classes (from fastest to slowest)
```
O(1)       - Constant: Direct calculation, hash lookup
O(log n)   - Logarithmic: Binary search, balanced tree search
O(n)       - Linear: Simple loop through all elements
O(n log n) - Linearithmic: Good sorting, merge sort
O(n²)      - Quadratic: Nested loops, bubble sort
O(n³)      - Cubic: Triple nested loops
O(2^n)     - Exponential: Recursion without memoization
O(n!)      - Factorial: Permutation generation
```

## Core Concepts

### 1. Time Complexity
How many operations does the algorithm perform?

```python
# O(1) - Constant operations
def get_first(arr):
    return arr[0]

# O(n) - Linear with input size
def find_max(arr):
    max_val = float('-inf')
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - Nested loops
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# O(log n) - Divide and conquer
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
    return -1

# O(n log n) - Sorting with divide-and-conquer
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

### 2. Space Complexity
How much extra memory does the algorithm use?

```python
# O(1) - Constant space
def sum_array(arr):
    total = 0  # One variable
    for num in arr:
        total += num
    return total

# O(n) - Linear space with input
def create_map(arr):
    lookup = {}
    for num in arr:
        lookup[num] = True  # n keys
    return lookup

# O(log n) - Recursion depth (binary search)
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
    # Call stack depth: O(log n)

# O(n) - Recursion depth with backtracking
def permutations(arr):
    result = []
    def backtrack(path):
        if len(path) == len(arr):
            result.append(path[:])
            return
        for i in range(len(arr)):
            if arr[i] not in path:
                path.append(arr[i])
                backtrack(path)  # Recursion depth: O(n)
                path.pop()
    backtrack([])
    return result
```

### 3. Common Patterns

**Loop Analysis:**
```python
# Single loop: O(n)
for i in range(n):
    operation()

# Nested loops: O(n²)
for i in range(n):
    for j in range(n):
        operation()

# Sequential operations: O(n + m)
for i in range(n):
    operation()
for j in range(m):
    operation()
# Total: O(n + m), usually simplified to O(n) if n ≈ m

# Divide and conquer: O(log n)
while n > 1:
    n = n // 2

# Exponential: O(2^n)
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n-1) + fib_slow(n-2)
```

## Analysis Methods

### Master Theorem (for Recursion)
For `T(n) = a*T(n/b) + f(n)`:

```
If f(n) = O(n^c):
- If c < log_b(a): T(n) = O(n^log_b(a))
- If c = log_b(a): T(n) = O(n^c * log n)
- If c > log_b(a): T(n) = O(f(n))

Examples:
- Merge sort: a=2, b=2, f(n)=n → O(n log n)
- Binary search: a=1, b=2, f(n)=1 → O(log n)
- Naive matrix mult: a=8, b=2, f(n)=n² → O(n³)
```

### Amortized Analysis
Average cost over a sequence of operations.

```python
# Dynamic array append
# Single append might be O(n) when resizing
# But amortized: O(1)

class DynamicArray:
    def __init__(self):
        self.arr = [0] * 1
        self.size = 0

    def append(self, x):
        if self.size == len(self.arr):
            # Double capacity: O(n) operation
            new_arr = [0] * len(self.arr) * 2
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr

        self.arr[self.size] = x
        self.size += 1

# Why amortized O(1)?
# In n operations:
# - 1 resize at n=1, cost 1
# - 1 resize at n=2, cost 2
# - 1 resize at n=4, cost 4
# - ...
# - 1 resize at n, cost n
# Total: 1 + 2 + 4 + ... + n = 2n = O(n)
# Per operation: O(n)/n = O(1)
```

## Optimization Tips

### Recognize Inefficiencies
```python
# ❌ Slow: O(n) lookup in list in O(n) loop = O(n²)
for num in arr:
    if num in list_data:  # O(n) lookup
        process(num)

# ✅ Fast: O(1) lookup in set = O(n)
set_data = set(list_data)
for num in arr:
    if num in set_data:  # O(1) lookup
        process(num)
```

### Cache Results
```python
# ❌ Slow: Recompute same value
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n-1) + fib_slow(n-2)  # fib(3) computed many times

# ✅ Fast: Remember results
def fib_fast(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_fast(n-1, memo) + fib_fast(n-2, memo)
    return memo[n]
```

### Choose Right Data Structure
```python
# Task: Frequent lookups and insertions

# ❌ List: O(n) search, O(n) insert
# ✅ Hash set: O(1) search, O(1) insert
# ✅ Hash map: O(1) search, O(1) insert

# Task: Sorted data, range queries
# ❌ Hash set: No order, no range
# ✅ Binary search tree: O(log n) operations
# ✅ Sorted array: O(log n) search, O(n) update
```

## Practice Problems

### Level 1: Basic Analysis (5 problems)
1. Analyze 10 simple functions and write complexity
2. Sort algorithms by complexity
3. Identify inefficient loops
4. Predict runtime for given input sizes
5. Explain why O(n²) is worse than O(n log n)

### Level 2: Intermediate (5 problems)
6. Analyze recursive functions using master theorem
7. Understand amortized analysis for dynamic arrays
8. Choose data structure based on operations
9. Optimize O(n²) to O(n) or O(n log n)
10. Analyze code with multiple phases

### Level 3: Advanced (5 problems)
11. Complex recursion analysis
12. Amortized analysis proofs
13. Space-time trade-offs
14. System design complexity decisions
15. Predict scalability for different algorithms

## Key Rules

✅ **Drop lower order terms**: O(n² + n) → O(n²)
✅ **Drop constants**: O(2n) → O(n)
✅ **Nested loops multiply**: O(n) × O(m) = O(n*m)
✅ **Sequential phases add**: O(n) + O(n²) = O(n²)
✅ **Logarithmic bases don't matter**: O(log₂ n) = O(log₁₀ n)

## Common Complexity Classes

| Class | Operations for n=1M | Real-world |
|-------|-------------------|------------|
| O(1) | 1 | Hash lookup |
| O(log n) | 20 | Binary search |
| O(n) | 1 million | Simple loop |
| O(n log n) | 20 million | Merge sort |
| O(n²) | 1 trillion | Bubble sort |
| O(2^n) | Impossible | Brute force |

## Real-World Perspective

```
1M elements:
- O(n) = instant (~1ms)
- O(n log n) = still instant (~20ms)
- O(n²) = slow (~1000 seconds = way too long!)
- O(2^n) = impossible even for n=30

1B elements:
- O(n) = seconds
- O(n log n) = minutes
- O(n²) = centuries!
```

---

**Master complexity analysis and you understand the heart of algorithm design!**
