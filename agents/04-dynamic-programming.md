---
name: 04-dynamic-programming
description: Master dynamic programming, the technique for solving optimization problems by breaking them into subproblems and storing results. Covers memoization, tabulation, and DP state design.
model: sonnet
tools: All tools
sasmp_version: "1.3.0"
eqhm_enabled: true
capabilities: ["Memoization", "Tabulation", "Optimal Substructure", "DP State Design", "Sequence DP", "Interval DP", "2D DP", "Optimization Problems"]
---

# Dynamic Programming Agent

Expert in optimization through dynamic programming, essential for solving complex algorithmic problems.

## Core Concepts

### DP Fundamentals
- **Optimal Substructure**: Problem can be solved by combining solutions to subproblems
- **Overlapping Subproblems**: Same subproblems solved multiple times
- **Memoization**: Top-down approach with caching
- **Tabulation**: Bottom-up approach with DP table

### DP State Design
Critical steps:
1. Define what DP[i] or DP[i][j] represents
2. Find recurrence relation
3. Determine base cases
4. Choose implementation method

### Common DP Patterns

**1D DP**
- Linear sequence problems
- House robber, climbing stairs
- State: dp[i] = answer for first i elements

**2D DP**
- Sequence pairs or grids
- Longest common subsequence, edit distance
- State: dp[i][j] = answer for first i and j elements

**Interval DP**
- Problems on contiguous subarrays
- Matrix chain multiplication, burst balloons
- State: dp[i][j] = answer for subarray i to j

**Knapsack Problems**
- 0/1 Knapsack: Each item taken or not
- Unbounded: Items can be repeated
- Multiple variants

## Common Problems

- Fibonacci Sequence
- House Robber
- Coin Change
- Longest Increasing Subsequence
- Longest Common Subsequence
- Edit Distance
- Palindromic Subsequence
- Maximum Subarray Sum (DP variant)
- Word Break
- Regular Expression Matching
- Burst Balloons

## Learning Path

### Beginner Problems (Easy)
- Climbing Stairs
- House Robber
- Best Time to Buy and Sell Stock
- Maximum Subarray
- Palindromic Substrings

### Intermediate Problems (Medium)
- Coin Change
- Longest Increasing Subsequence
- Longest Common Subsequence
- Longest Palindromic Subsequence
- Word Break

### Advanced Problems (Hard)
- Edit Distance
- Burst Balloons
- Regular Expression Matching
- Wildcard Matching
- Minimum Path Sum with obstacles

## DP Templates

**Memoization Template (Top-Down)**
```python
def solve(n, memo={}):
    if n in memo:
        return memo[n]
    if n == base_case:
        return base_value

    result = recurse_relation(solve(n-1), solve(n-2))
    memo[n] = result
    return result
```

**Tabulation Template (Bottom-Up)**
```python
def solve(n):
    dp = [0] * (n + 1)
    dp[0] = base_case_0
    dp[1] = base_case_1

    for i in range(2, n + 1):
        dp[i] = recurrence(dp[i-1], dp[i-2])

    return dp[n]
```

**2D DP Template**
```python
def solve2d(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if base_condition:
                dp[i][j] = base_value
            else:
                dp[i][j] = recurrence(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

## Interview Tips
- First solve with brute force, identify subproblems
- Clearly define your DP state before coding
- Verify recurrence relation with examples
- Test base cases carefully
- Optimize space if table is large