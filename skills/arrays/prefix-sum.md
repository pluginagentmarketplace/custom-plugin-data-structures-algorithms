---
name: prefix-sum-technique
description: Optimize range sum queries and subarray problems using prefix sum precomputation. Trade space for O(1) query time.
---

# Prefix Sum Technique

## Core Concept
Precompute cumulative sums for O(1) range queries.

```python
def buildPrefixSum(nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix

def rangeSum(prefix, left, right):
    return prefix[right + 1] - prefix[left]
```

## 2D Prefix Sum
```python
def buildPrefixSum2D(matrix):
    if not matrix:
        return []

    m, n = len(matrix), len(matrix[0])
    prefix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix[i][j] = matrix[i-1][j-1] + prefix[i-1][j] + \
                          prefix[i][j-1] - prefix[i-1][j-1]

    return prefix

def sumRegion(prefix, row1, col1, row2, col2):
    return prefix[row2+1][col2+1] - prefix[row1][col2+1] - \
           prefix[row2+1][col1] + prefix[row1][col1]
```

## Applications
- Range Sum Query: O(1) after O(n) precomputation
- Subarray Sum Equals K: O(n) with hash map
- Maximum Subarray: Kadane + prefix sums
- 2D Matrix Sum: O(1) queries in 2D grid