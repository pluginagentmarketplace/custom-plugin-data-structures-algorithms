---
description: Master dynamic programming problem-solving strategies, memoization vs tabulation, DP on trees, interval DP, digit DP. Recognize and solve 50+ DP patterns.
capabilities: ["memoization", "tabulation", "dp-optimization", "dp-on-trees", "interval-dp", "digit-dp", "bitmask-dp"]
---

# Dynamic Programming Strategist

Dynamic Programming is the **art of optimization through memory trade-off**. Once you master the pattern recognition and transition formulation, you'll solve problems that seem impossible at first glance.

## Core Insight: Overlapping Subproblems + Optimal Substructure

Every DP problem has two prerequisites:

### 1. Optimal Substructure
The optimal solution uses optimal solutions to subproblems.

```python
# Example: Maximum subarray sum
# opt[i] = max money we can get considering arr[0..i]
# opt[i] = max(opt[i-1] + arr[i], arr[i])
#          └─ includes current    └─ restart here
```

### 2. Overlapping Subproblems
Subproblems are computed multiple times.

```python
# Fibonacci without DP (exponential)
def fib(n):           # fib(5)
    if n <= 1:        # ├─ fib(4)
        return n      # │  ├─ fib(3)
    return fib(n-1) + fib(n-2)  # │  │  ├─ fib(2)  [computed again!]
                      # │  │  └─ fib(1)
                      # │  └─ fib(3)  [recomputed!]
```

## DP Approaches

### Approach 1: Top-Down (Memoization)
```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]  # Return cached result
    if n <= 1:
        return n

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Time: O(n), Space: O(n) [recursion stack + memo]
# Natural for thinking recursively
```

**Advantages:**
- Intuitive, follows problem thinking
- Only computes needed subproblems
- Better for sparse DP tables

### Approach 2: Bottom-Up (Tabulation)
```python
def fib_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Time: O(n), Space: O(n)
# Iterative, guaranteed no stack overflow
```

**Advantages:**
- No recursion overhead
- Better iterative control
- Can optimize space more easily

## Space Optimization Technique

Many DP problems only need last few states:

```python
# Instead of dp[n] array
def fib_optimized(n):
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr

# Space: O(1) instead of O(n)
```

## DP Problem Categories & Patterns

### Category 1: Linear DP (1D)
```python
# Pattern: dp[i] = result for arr[0..i]

# House robber: max money robbing non-adjacent houses
def house_robber(nums):
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[n-1]
    # Time: O(n), Space: O(n) → O(1)
```

### Category 2: 2D DP
```python
# Pattern: dp[i][j] = result for first i items, capacity j

# 0/1 Knapsack: max value with weight limit
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                # Include or exclude item
                dp[i][w] = max(
                    dp[i-1][w],  # Don't take
                    dp[i-1][w - weights[i-1]] + values[i-1]  # Take
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
    # Time: O(n*W), Space: O(n*W) → O(W)
```

### Category 3: DP on Strings
```python
# Longest common subsequence
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
    # Time: O(m*n), Space: O(m*n)
```

### Category 4: DP on Trees
```python
# Maximum sum path in tree

def max_path_sum(root):
    def dfs(node):
        if not node:
            return 0

        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        max_path_sum.result = max(
            max_path_sum.result,
            left + right + node.val
        )

        return max(left, right) + node.val

    max_path_sum.result = float('-inf')
    dfs(root)
    return max_path_sum.result
```

### Category 5: Interval DP
```python
# Burst balloons: max coins bursting balloons in interval [i, j]

def burst_balloons(nums):
    nums = [1] + [x for x in nums if x > 0] + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for length in range(3, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            for k in range(left + 1, right):
                dp[left][right] = max(
                    dp[left][right],
                    dp[left][k] +
                    dp[k][right] +
                    nums[left] * nums[k] * nums[right]
                )

    return dp[0][n-1]
```

### Category 6: Digit DP
```python
# Count numbers <= n without digit 7

def count_without_7(n):
    s = str(n)
    memo = {}

    def dp(pos, is_limit, num_str):
        if pos == len(num_str):
            return 1

        if (pos, is_limit) in memo:
            return memo[(pos, is_limit)]

        limit = int(num_str[pos]) if is_limit else 9
        result = 0

        for digit in range(0, limit + 1):
            if digit == 7:
                continue
            result += dp(pos + 1, is_limit and digit == limit, num_str)

        memo[(pos, is_limit)] = result
        return result

    return dp(0, True, s)
```

## DP Problem Recognition Checklist

- [ ] Does it ask for "maximum/minimum/count of..."?
- [ ] Can the solution be built from smaller solutions?
- [ ] Are there repeated subproblems?
- [ ] Is brute force exponential?
- [ ] Can I define state clearly (e.g., dp[i] means...)?
- [ ] Can I write the recurrence relation?

If yes to most, it's likely DP!

## Classic DP Problems (50+ patterns)

### Easy (10+ problems)
1. Climbing stairs
2. House robber
3. Best time to buy/sell stock
4. Maximum subarray
5. Longest increasing subsequence

### Medium (20+ problems)
6. 0/1 Knapsack
7. Coin change
8. Word break
9. Longest common subsequence
10. Longest palindromic subsequence
11. Edit distance
12. Unique paths in grid
13. Decode ways
14. Regular expression matching
15. Interleaving strings

### Hard (20+ problems)
16. Burst balloons
17. Wildcard matching
18. Max product subarray
19. Russian doll envelopes
20. Cherry pickup
21. Minimum path sum in grid with obstacles
22. Palindrome partition
23. Stock trading with cooldown/transaction limits
24. Longest increasing subsequence with constraints

## Learning Progression

### Level 1: Foundations (Days 1-4)
- [ ] Understand optimal substructure
- [ ] Recognize overlapping subproblems
- [ ] Implement memoization
- [ ] Solve 5 easy DP problems

### Level 2: Patterns (Days 5-11)
- [ ] Master 1D DP (array-based)
- [ ] Master 2D DP (knapsack variants)
- [ ] String DP patterns
- [ ] Solve 25+ medium problems

### Level 3: Advanced (Days 12-18)
- [ ] Tree DP
- [ ] Interval DP
- [ ] Digit DP
- [ ] Bitmask DP
- [ ] Solve 20+ hard problems

## DP Optimization Techniques

1. **Space optimization**: Reduce from 2D to 1D
2. **Pruning**: Skip impossible states
3. **Limit transitions**: Only valid state changes
4. **Early termination**: Found answer, stop computing

## Real-World DP Applications

| Application | DP Problem |
|-------------|-----------|
| Supply chain | Knapsack, coin change |
| Game AI | Minimax with memoization |
| Compiler | Edit distance, regex matching |
| Genomics | Longest common subsequence |
| Finance | Stock trading optimization |

## Key Takeaways

✅ **State definition is crucial**: "dp[i] means..." must be crystal clear
✅ **Recurrence relation**: Write before coding
✅ **Base cases**: Handle n=0, n=1 carefully
✅ **DP vs Greedy**: DP solves optimization, greedy is local optimal
✅ **Space optimization**: Often possible but lose ability to backtrack

## Next Steps

1. Solve 10 easy DP problems from LeetCode
2. Identify patterns in your solutions
3. Master 2D DP (knapsack family)
4. Move to specialized DP (trees, strings, intervals)
5. Develop pattern recognition speed

---

**Interview Tip**: "First check: optimal substructure and overlapping subproblems. Then: define state clearly. Finally: write recurrence and code."
