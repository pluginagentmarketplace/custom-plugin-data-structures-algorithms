---
name: complexity-analyzer
description: Complexity Analyzer - Master Time & Space Complexity
allowed-tools: Read
---

# Complexity Analyzer - Master Time & Space Complexity

Understand and analyze algorithmic complexity to optimize your solutions.

## Big O Notation

### Time Complexity Rankings (Best to Worst)
```
O(1)       - Constant         ✅ Excellent
O(log n)   - Logarithmic     ✅ Great
O(n)       - Linear          ✅ Good
O(n log n) - Linearithmic    ✅ Good
O(n²)      - Quadratic       ⚠️ Acceptable
O(n³)      - Cubic           ❌ Poor
O(2ⁿ)      - Exponential     ❌ Very Poor
O(n!)      - Factorial       ❌ Terrible
```

### Space Complexity
```
O(1)       - Constant space (in-place)
O(log n)   - Logarithmic space (recursion depth)
O(n)       - Linear space (new array/data structure)
O(n²)      - Quadratic space (2D structures)
```

## How to Calculate Complexity

### Rule 1: Drop Constants
```python
# O(2n) → O(n)
for i in range(n):
    ...
for i in range(n):
    ...

# O(n) → O(n)
```

### Rule 2: Drop Non-Dominant Terms
```python
# O(n² + n) → O(n²)
# Quadratic dominates linear

# O(n + log n) → O(n)
# Linear dominates logarithmic
```

### Rule 3: Multiply for Nested Loops
```python
# O(n)
for i in range(n):
    ...

# O(n²) - nested loop
for i in range(n):
    for j in range(n):
        ...

# O(n log n) - loop + binary search inside
for i in range(n):
    binary_search(...)
```

### Rule 4: O(n) for Sequential Loops
```python
# O(n)
for i in range(n):
    ...
for j in range(n):
    ...

# O(n + m)
for i in range(n):
    ...
for j in range(m):
    ...
```

## Algorithm Complexity Chart

| Data Structure | Access | Search | Insert | Delete |
|---|---|---|---|---|
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| Hash Table | - | O(1) | O(1) | O(1) |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(log n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) |

## Sorting Algorithms Comparison

| Algorithm | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |

## Common Patterns

### Linear Search
```python
# O(n) time, O(1) space
for num in arr:
    if num == target:
        return True
return False
```

### Binary Search
```python
# O(log n) time, O(1) space
left, right = 0, len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    ...
```

### Two Pointers
```python
# O(n) time, O(1) space
left, right = 0, len(arr) - 1
while left < right:
    if arr[left] + arr[right] == target:
        return [left, right]
    ...
```

### Sliding Window
```python
# O(n) time, O(1) or O(k) space
left = 0
for right in range(len(arr)):
    # Expand window
    ...
    while condition:
        # Shrink window
        left += 1
```

### Hash Map/Set
```python
# O(n) time average, O(n) space
seen = set()
for item in arr:
    if item in seen:  # O(1) average
        ...
    seen.add(item)
```

### DFS/BFS
```python
# O(V + E) time, O(V) space
# V = vertices, E = edges
```

## Optimization Techniques

### 1. Use Hash Tables Instead of Lists
```
Instead of:   O(n) lookup in list
Use:          O(1) lookup in hash map
Tradeoff:     Extra O(n) space
```

### 2. Use Sorting
```
Problem:      Find duplicates
Naive:        O(n²)
Sorted:       O(n log n)
With Hash:    O(n) space
```

### 3. Two Pointers vs Nested Loops
```
Nested loops:     O(n²)
Two pointers:     O(n) if sorted
Tradeoff:         Need to sort O(n log n)
```

### 4. Dynamic Programming
```
Brute force:      O(2ⁿ)
With memoization: O(n²) or better
Tradeoff:         O(n) space for cache
```

### 5. Greedy + Sorting
```
Optimal subproblem: Need to sort O(n log n)
Then greedy:        O(n)
Total:              O(n log n)
```

## Complexity Estimation Rules

### Recursion
- Depth = O(log n) → O(log n) space
- Depth = O(n) → O(n) space
- Time = 2^depth → O(2ⁿ)

### String Manipulation
- Concatenation in loop: O(n²) - strings are immutable
- Use list + join: O(n) - better approach

### Matrix Operations
- Nested loops: O(m × n)
- DFS/BFS on grid: O(m × n)
- Traversing diagonals: O(min(m,n))

## Space Complexity Hidden Costs

```python
# Explicitly O(1) but uses O(n) space for output
def getAllUsers():
    return [user for user in users]  # Output space

# Recursion call stack
def factorial(n):  # O(n) space due to recursion
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

## Interview Tip: Explain Complexity

When asked about complexity:

1. **State Time Complexity** - "This solution is O(n log n)"
2. **Explain Why** - "We sort the array (n log n) then iterate once (n)"
3. **Discuss Space** - "We use O(1) extra space except for output"
4. **Mention Tradeoffs** - "We trade space for time"
5. **Suggest Improvements** - "If memory is limited, we could use..."

---

**Master Complexity** → **Better Optimization** → **Better Interviews**!