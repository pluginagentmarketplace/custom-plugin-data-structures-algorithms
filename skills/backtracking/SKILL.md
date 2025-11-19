---
name: backtracking-patterns
description: Master backtracking technique with permutations, combinations, and puzzle solving patterns with complete implementations.
---

# Backtracking Patterns Skill

## Permutations
```python
def permute(nums):
    result = []

    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return

        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()

    backtrack([])
    return result

# Alternative using indices
def permuteIndices(nums):
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result
```

## Combinations
```python
def combine(n, k):
    result = []

    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return

        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()

    backtrack(1, [])
    return result
```

## N-Queens Problem
```python
def solveNQueens(n):
    result = []
    board = ['.' * n for _ in range(n)]

    def isValid(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check diagonals
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False

        return True

    def backtrack(row):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if isValid(row, col):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                backtrack(row + 1)
                board[row] = '.' * n

    backtrack(0)
    return result
```

## Subset Generation
```python
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result

# Bit manipulation approach
def subsetsWithBits(nums):
    result = []
    n = len(nums)

    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)

    return result
```