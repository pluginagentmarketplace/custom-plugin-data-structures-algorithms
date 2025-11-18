---
name: dynamic-programming-skill
description: DP fundamentals, state definition, recurrence relations, memoization vs tabulation, space optimization, and pattern recognition for 50+ DP problem types.
---

# Dynamic Programming Skill

## Quick Start

**DP Checklist:**
- [ ] Problem asks for optimization (max/min/count)?
- [ ] Can solution be built from smaller solutions?
- [ ] Are subproblems computed repeatedly?
- [ ] Can I define state clearly?
- [ ] Can I write the recurrence?

If yes to most → **Use DP!**

## Core Principle

**DP = Recursion with Memoization**

Solve once, remember forever!

```python
# Without DP (exponential - recompute)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
    # fib(5): fib(3) computed 2 times, fib(2) computed 3 times!

# With DP (polynomial - memoize)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]  # <-- Remember!
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

## Approach 1: Top-Down (Memoization)

```python
def solve_top_down(n, memo={}):
    # Base case
    if n == 0:
        return 0

    # Check memo
    if n in memo:
        return memo[n]

    # Compute
    result = compute(n)

    # Store
    memo[n] = result
    return result

# Pros: Intuitive, only compute needed subproblems
# Cons: Recursion overhead, need to handle base cases carefully
```

## Approach 2: Bottom-Up (Tabulation)

```python
def solve_bottom_up(n):
    # Initialize
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1  # Base case

    # Fill table
    for i in range(2, n + 1):
        dp[i] = compute(dp, i)

    return dp[n]

# Pros: No recursion overhead, guaranteed no stack overflow
# Cons: Compute all subproblems, harder to think about initially
```

## Space Optimization

```python
# Original: O(n) space for DP array
def fib_tab(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Optimized: O(1) space (only need last 2 values)
def fib_optimized(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

## DP Problem Categories

### Category 1: 1D Linear DP

```python
# House Robber: max money robbing non-adjacent houses
def rob(nums):
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # Choice: skip or take current house

    return dp[n-1]
    # Time: O(n), Space: O(n) → O(1)
```

### Category 2: 2D DP

```python
# 0/1 Knapsack: max value with weight limit
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                # Include or exclude item
                dp[i][w] = max(
                    dp[i-1][w],  # Exclude
                    dp[i-1][w - weights[i-1]] + values[i-1]  # Include
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
    # Time: O(n*W), Space: O(n*W) → O(W)
```

### Category 3: String DP

```python
# Longest Common Subsequence
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

# Edit Distance (Levenshtein)
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

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
```

### Category 4: DP on Trees

```python
# Max path sum in tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    def dfs(node):
        if not node:
            return 0

        left = max(0, dfs(node.left))  # 0 if negative
        right = max(0, dfs(node.right))

        max_path_sum.result = max(
            max_path_sum.result,
            left + right + node.val
        )

        return max(left, right) + node.val  # Return to parent

    max_path_sum.result = float('-inf')
    dfs(root)
    return max_path_sum.result
```

### Category 5: Interval DP

```python
# Matrix Chain Multiplication
def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n-1]
```

### Category 6: Digit DP

```python
# Count numbers <= n without digit 7
def count_without_7(n):
    s = str(n)
    memo = {}

    def dp(pos, is_limit):
        if pos == len(s):
            return 1

        if (pos, is_limit) in memo:
            return memo[(pos, is_limit)]

        limit = int(s[pos]) if is_limit else 9
        result = 0

        for digit in range(0, limit + 1):
            if digit == 7:
                continue
            result += dp(pos + 1, is_limit and digit == limit)

        memo[(pos, is_limit)] = result
        return result

    return dp(0, True)
```

## State Definition Template

```
dp[i] = answer for first i elements
dp[i][j] = answer considering first i of A, first j of B
dp[i][j][k] = answer for A[0..i], B[0..j], with constraint k

Example:
dp[i] = max profit robbing houses [0..i]
dp[i][w] = max value with weight limit w using items [0..i]
dp[i][j] = LCS length for s1[0..i] and s2[0..j]
```

## Recurrence Relation Template

```
State: dp[i] = ...

Base case:
dp[0] = ...
dp[1] = ...

Recurrence:
dp[i] = f(dp[i-1], dp[i-2], ..., current element)

Example:
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

## Classic DP Problems (50+ patterns)

**Easy (10+ problems):**
1. Climbing stairs
2. House robber
3. Best time to buy/sell stock
4. Maximum subarray
5. Longest increasing subsequence

**Medium (20+ problems):**
6. 0/1 Knapsack
7. Coin change
8. Word break
9. Longest common subsequence
10. Edit distance
11. Unique paths in grid
12. Decode ways
13. Regular expression matching
14. Interleaving strings
15. Partition equal subset

**Hard (20+ problems):**
16. Burst balloons
17. Wildcard matching
18. Max product subarray
19. Russian doll envelopes
20. Cherry pickup

## Common Mistakes

❌ **Not memoizing**: Recomputing same subproblems
❌ **Wrong state definition**: Unclear what dp[i] means
❌ **Missing base case**: Infinite recursion or wrong answers
❌ **Off-by-one errors**: Index confusion in loops
❌ **Not considering all transitions**: Missing some choices

✅ **Check**: Define state, write recurrence, identify transitions
✅ **Test**: Small examples by hand
✅ **Optimize**: Space reduction once working

## Optimization Checklist

```
Runtime:
- [ ] Is recursion → memoization faster?
- [ ] Can reduce state dimensions?
- [ ] Can prune impossible states?

Space:
- [ ] Can use rolling array? (O(n) → O(1))
- [ ] Can use deque/queue instead of full DP table?
- [ ] Can reconstruct solution without full table?
```

## Real-World DP Applications

| Application | DP Problem |
|-------------|-----------|
| Supply chain | Knapsack, inventory |
| Compiler optimization | Word break, regex |
| Speech recognition | Edit distance, alignment |
| Genomics | LCS, sequence alignment |
| Finance | Stock trading variants |
| Game AI | Minimax with memoization |

---

**Master DP pattern recognition and optimization problems become easy!**
