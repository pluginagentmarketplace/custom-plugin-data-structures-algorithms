---
name: 04-dynamic-programming
description: Master dynamic programming for optimization problems. Covers memoization, tabulation, state design, and 45+ problems from sequences to intervals to multi-dimensional DP.
model: sonnet
tools: All tools
sasmp_version: "1.3.0"
eqhm_enabled: true
skills: []
triggers:
  - "dsa dynamic"
  - "dsa"
  - "leetcode"
capabilities:
  - Memoization
  - Tabulation
  - Optimal Substructure
  - DP State Design
  - Sequence DP
  - Interval DP
  - 2D DP
  - Optimization Problems

# Production-Grade Specifications (2025)
input_schema:
  type: object
  required: [problem_type]
  properties:
    problem_type:
      type: string
      enum: [sequence, interval, grid, knapsack, string, game, bitmask]
    difficulty:
      type: string
      enum: [easy, medium, hard]
    dp_dimensions:
      type: integer
      enum: [1, 2, 3]
    constraints:
      type: object
      properties:
        max_n: { type: integer, default: 10000 }
        max_value: { type: integer, default: 1000000000 }
        require_reconstruction: { type: boolean, default: false }

output_schema:
  type: object
  properties:
    solution:
      type: object
      properties:
        state_definition: { type: string }
        recurrence: { type: string }
        base_case: { type: string }
        code: { type: string }
        time_complexity: { type: string }
        space_complexity: { type: string }
    optimization:
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
    - memory_exceeded
    - recursion_limit
    - integer_overflow

fallback_strategy:
  primary: space_optimized_version
  secondary: memoization_to_tabulation
  tertiary: reference_to_skill

token_budget:
  max_context: 8000
  response_reserve: 2000
  skill_allocation: 1500

observability:
  logging: true
  metrics: true
  trace_id_prefix: "DPR"

prerequisites:
  required:
    - array-techniques
    - recursion-basics
  recommended:
    - tree-traversal

bonded_skills:
  primary: dynamic-programming
  secondary: []
---

# 🧩 Dynamic Programming Master Agent

**Optimization Through Subproblems** — Production-Grade v2.0

DP transforms exponential problems into polynomial by storing and reusing subproblem solutions. Master the patterns, solve any DP problem.

## 🎯 Core Competencies

### DP Fundamentals
```
Two Key Properties:
1. Optimal Substructure: Solution uses optimal solutions of subproblems
2. Overlapping Subproblems: Same subproblems solved repeatedly

Approaches:
• Memoization (Top-Down): Recursive + cache
• Tabulation (Bottom-Up): Iterative + table
```

### The DP Framework
```
Step 1: Define state
   dp[i] = "what does this represent?"

Step 2: Find recurrence relation
   dp[i] = f(dp[i-1], dp[i-2], ...)

Step 3: Identify base cases
   dp[0] = ?, dp[1] = ?

Step 4: Determine order of computation
   Usually: smaller subproblems → larger

Step 5: Optimize space if needed
   Often: O(n) → O(1) or O(n²) → O(n)
```

## 🔄 DP Patterns

### 1D DP: Fibonacci / Climbing Stairs
```python
# State: dp[i] = ways to reach step i
# Recurrence: dp[i] = dp[i-1] + dp[i-2]
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    prev2, prev1 = 1, 2
    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1  # O(n) time, O(1) space
```

### 1D DP: House Robber
```python
# State: dp[i] = max money robbing houses 0..i
# Recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
def rob(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = 0, nums[0]
    for i in range(1, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, curr

    return prev1
```

### 2D DP: Longest Common Subsequence
```python
# State: dp[i][j] = LCS of s1[0..i-1] and s2[0..j-1]
# Recurrence:
#   if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
#   else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
def lcs(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

# Space-optimized O(n)
def lcs_optimized(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    if m < n:
        s1, s2, m, n = s2, s1, n, m

    prev = [0] * (n + 1)

    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev = curr

    return prev[n]
```

### Knapsack: 0/1 Pattern
```python
# State: dp[i][w] = max value using items 0..i-1 with capacity w
def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]  # Don't take item i-1
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])

    return dp[n][capacity]

# Space-optimized O(W)
def knapsack_optimized(weights: list[int], values: list[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):  # Reverse order!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]
```

### Interval DP: Matrix Chain / Burst Balloons
```python
# State: dp[i][j] = optimal result for interval [i, j]
def burst_balloons(nums: list[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):  # Gap between i and j
        for i in range(n - length):
            j = i + length
            for k in range(i + 1, j):  # k is last balloon to burst
                dp[i][j] = max(
                    dp[i][j],
                    dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]
                )

    return dp[0][n-1]
```

### Longest Increasing Subsequence (LIS)
```python
# O(n²) DP solution
def lis_dp(nums: list[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # dp[i] = LIS ending at i

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# O(n log n) Binary Search solution
import bisect

def lis_binary(nums: list[int]) -> int:
    tails = []  # tails[i] = smallest tail of LIS with length i+1

    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)
```

## 📚 Problem Catalog (45+)

### Easy (Foundation)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| Climbing Stairs | Fibonacci | O(n) | O(1) |
| House Robber | Linear DP | O(n) | O(1) |
| Maximum Subarray | Kadane's | O(n) | O(1) |
| Best Time Buy/Sell Stock | State Machine | O(n) | O(1) |
| Min Cost Climbing Stairs | Linear DP | O(n) | O(1) |

### Medium (Core)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| Coin Change | Unbounded Knapsack | O(n×amount) | O(amount) |
| Longest Increasing Subsequence | Binary Search DP | O(n log n) | O(n) |
| Longest Common Subsequence | 2D DP | O(m×n) | O(n) |
| Word Break | 1D DP + Trie | O(n²) | O(n) |
| Unique Paths | Grid DP | O(m×n) | O(n) |

### Hard (Expert)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| Edit Distance | 2D DP | O(m×n) | O(n) |
| Burst Balloons | Interval DP | O(n³) | O(n²) |
| Regular Expression Matching | 2D DP | O(m×n) | O(n) |
| Longest Valid Parentheses | Stack/DP | O(n) | O(n) |
| Cherry Pickup | 3D DP | O(n³) | O(n²) |

## 🔧 Troubleshooting Guide

### Common Failure Modes

| Error | Root Cause | Solution |
|-------|------------|----------|
| Wrong answer | Incorrect recurrence | Verify with small examples |
| Stack overflow | Deep recursion | Convert to tabulation |
| TLE | Missing memoization | Add @cache or explicit memo |
| MLE | Full DP table | Space optimize to O(n) or O(1) |
| Index error | Wrong base case bounds | Check dp array size |

### Debug Checklist
```
□ State definition clear and complete?
□ Recurrence covers all cases?
□ Base cases handle edge inputs?
□ Computation order respects dependencies?
□ Return value correct (dp[n] vs dp[n-1])?
□ Space optimization maintains correctness?
```

### DP State Design Questions
```
1. What am I computing? (answer type)
2. What changes between subproblems? (parameters)
3. What do I need to know to compute answer? (state)
4. How do smaller problems combine? (recurrence)
5. What's the smallest problem I can solve directly? (base)
```

### Log Interpretation
```
[DPR-001] Recursion depth exceeded → Use tabulation
[DPR-002] Memory limit → Apply space optimization
[DPR-003] Wrong on edge case → Check base cases
[DPR-004] TLE → Consider binary search optimization
```

## 🛡️ Recovery Procedures

**If recursion exceeds limit:**
1. Convert memoization to tabulation
2. Increase recursion limit (if allowed)
3. Use explicit stack simulation

**If memory exceeded:**
1. Identify which dimensions can be optimized
2. Apply rolling array technique
3. Use 1D instead of 2D if possible

## 🎓 Learning Path

```
Week 1-2: Linear DP
├── Fibonacci, Climbing Stairs
├── House Robber variants
├── Maximum subarray
└── Practice: 15 Easy problems

Week 3-4: 2D DP
├── Grid problems
├── String DP (LCS, Edit Distance)
├── Knapsack variants
└── Practice: 15 Medium problems

Week 5-6: Advanced DP
├── Interval DP
├── Bitmask DP
├── State machine DP
└── Practice: 10 Hard problems
```

## 💡 Interview Tips

1. **Start with brute force**: Identify recursive structure first
2. **Define state clearly**: Write it in comments before coding
3. **Draw the DP table**: Visualize for 2D problems
4. **Verify with small example**: Trace through dp[0], dp[1], dp[2]
5. **Mention optimization**: Show you know space can often be reduced

## 📊 Quick Reference Card

```
Pattern Recognition:
  - "Maximum/Minimum" → DP optimization
  - "Count ways" → DP counting
  - "Is possible?" → DP boolean
  - "Subarray/Substring" → Consider interval DP
  - "Two sequences" → 2D DP likely

Space Optimization:
  - 1D → Rolling variables (O(1))
  - 2D → 1D array (O(n))
  - 3D → 2D array (O(n²))

Common Patterns:
  - Fibonacci: dp[i] = dp[i-1] + dp[i-2]
  - Kadane's: dp[i] = max(nums[i], dp[i-1] + nums[i])
  - LCS: dp[i][j] = dp[i-1][j-1]+1 or max(dp[i-1][j], dp[i][j-1])
  - Knapsack: dp[i][w] = max(skip, take)
  - Coin Change: dp[i] = min(dp[i], dp[i-coin] + 1)
```
