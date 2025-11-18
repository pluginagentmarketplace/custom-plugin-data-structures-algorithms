---
name: dynamic-programming
description: Master Dynamic Programming optimization technique with memoization and tabulation. Learn state definition, transitions, and solve classic DP problems with confidence.
---

# Dynamic Programming

## Quick Start

DP solves problems by breaking them into overlapping subproblems and storing results.

### DP Problem Checklist
- [ ] **Optimal Substructure**: Solution uses optimal subproblem solutions
- [ ] **Overlapping Subproblems**: Same subproblems solved multiple times
- [ ] **States Definable**: Clear what variables represent a subproblem
- [ ] **Transitions Clear**: How states relate to each other

## Memoization vs Tabulation

### Memoization (Top-Down)
```python
def fibonacci_memo(n, memo=None):
    """Recursive with caching"""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Time: O(n), Space: O(n) + O(n) recursion stack
```

**Pros**: Natural recursion flow, only compute needed states
**Cons**: Recursion overhead, stack depth issues

### Tabulation (Bottom-Up)
```python
def fibonacci_tab(n):
    """Iterative with table"""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Time: O(n), Space: O(n)
```

**Pros**: Faster, no recursion overhead, can optimize space
**Cons**: Need to identify all states upfront

## Classic DP Patterns

### Pattern 1: Linear Sequences

#### Fibonacci
```python
# State: dp[i] = fibonacci(i)
# Transition: dp[i] = dp[i-1] + dp[i-2]
```

#### Climbing Stairs
```python
def climb_stairs(n):
    """Reach n stairs, can climb 1 or 2 steps"""
    if n <= 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1  # One way to stay at base
    dp[1] = 1  # One way to reach 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # Either from i-1 or i-2

    return dp[n]
```

### Pattern 2: Array/Sequence

#### House Robber
```python
def rob(nums):
    """Rob houses, can't rob adjacent"""
    if not nums:
        return 0

    dp = [0] * len(nums)
    dp[0] = nums[0]

    if len(nums) > 1:
        dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        # Rob current house + max before previous, or skip current
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])

    return dp[-1]

# Time: O(n), Space: O(n), can optimize to O(1)
```

#### Longest Increasing Subsequence (LIS)
```python
def longest_increasing_subsequence(arr):
    """Find longest increasing subsequence length"""
    n = len(arr)
    if n == 0:
        return 0

    dp = [1] * n  # Every element is LIS of length 1

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
    # Time: O(n²), Space: O(n)
```

### Pattern 3: 2D Grid

#### Unique Paths
```python
def unique_paths(m, n):
    """Paths in m×n grid, move right or down only"""
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]
    # Time: O(m×n), Space: O(m×n)
```

#### Minimum Path Sum
```python
def min_path_sum(grid):
    """Min sum path from top-left to bottom-right"""
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    # Initialize first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Initialize first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill rest
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]
```

### Pattern 4: String

#### Edit Distance (Levenshtein)
```python
def edit_distance(s1, s2):
    """Min edits to transform s1 to s2"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],      # Delete
                    dp[i][j-1],      # Insert
                    dp[i-1][j-1]     # Replace
                )

    return dp[m][n]
    # Time: O(m×n), Space: O(m×n)
```

### Pattern 5: Optimization

#### Coin Change
```python
def coin_change(coins, amount):
    """Min number of coins to make amount"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins for amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
    # Time: O(amount × coins), Space: O(amount)
```

#### 0/1 Knapsack
```python
def knapsack(weights, values, capacity):
    """Max value with weight limit"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item
            dp[i][w] = dp[i-1][w]

            # Take item if it fits
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    values[i-1] + dp[i-1][w - weights[i-1]]
                )

    return dp[n][capacity]
    # Time: O(n × capacity), Space: O(n × capacity)
```

## Space Optimization

### 1D Array Optimization
```python
def coin_change_optimized(coins, amount):
    """Reduce from O(amount×coins) to O(amount) space"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

### Two Array Optimization
```python
def climbing_stairs_optimized(n):
    """Reduce space from O(n) to O(1)"""
    if n <= 1:
        return 1

    prev, curr = 1, 1

    for i in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr
```

## Problem Recognition Framework

### Ask These Questions
1. **Can problem be broken into subproblems?**
2. **Are subproblems solved multiple times?**
3. **Can solution be expressed recursively?**
4. **What variables define a unique state?**
5. **How do states transition to each other?**

### Common Variations
- **Counting**: How many ways/solutions
- **Optimization**: Max/min values
- **Existence**: Is solution possible
- **Construction**: Build actual solution

## Common Mistakes

❌ Over-complicating state definition
❌ Missing base cases
❌ Wrong state transitions
❌ Not memoizing all states
❌ Wrong return value
✓ Start simple, optimize after correctness

## Interview Tips

- Identify DP early in problem analysis
- Start with brute force, add memoization
- Draw state transition diagram
- Test with small examples
- Optimize space if needed

## Key Takeaways

✓ Two keys: optimal substructure + overlapping subproblems
✓ Memoization easier to code, tabulation faster
✓ State definition is crucial
✓ Pattern recognition helps identification
✓ Space optimization often possible
✓ Practice classic problems to build intuition
