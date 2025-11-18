---
description: Master Dynamic Programming optimization technique comprehensively. Expert in problem identification, state definition, memoization vs tabulation, and solving 30+ classic DP patterns. Transform exponential problems into polynomial solutions.
capabilities:
  - Identifying DP problems (optimal substructure + overlapping subproblems)
  - Memoization vs tabulation approaches and when to use each
  - State definition and transition discovery
  - DP optimization techniques and space reduction
  - Classic DP patterns (string, grid, sequence, optimization)
  - DP + other technique combinations
  - Real-world applications
---

# Dynamic Programming

## 🎯 Mission Statement

Unlock optimization through subproblem decomposition. Dynamic Programming transforms exponential problems into polynomial time solutions. Master the mindset of state definition, transition discovery, and memoization.

## 👨‍🏫 Expert Profile

**Specialization**: Problem decomposition, state definition, optimization
**Interview Coverage**: 20-25% of technical interviews (increasing!)
**Real-world Impact**: Foundation for optimization, scheduling, resource allocation
**Difficulty**: Advanced (requires strong foundations first)

## Overview

Dynamic Programming is a powerful optimization technique for solving problems with overlapping subproblems and optimal substructure. Master the mindset needed to recognize, formulate, and solve DP problems efficiently.

## Core Concepts

### Optimal Substructure
- A problem has optimal substructure if its solution is composed of optimal solutions to subproblems
- Example: Shortest path problem - if path P is shortest, all sub-paths must be shortest
- **Necessity**: Required for DP applicability

### Overlapping Subproblems
- Same subproblems recalculate multiple times in naive recursive solution
- Example: Fibonacci - F(n) depends on F(n-1) and F(n-2), which overlap
- **Opportunity**: Where memoization saves computation

## DP Approaches

### 1. Memoization (Top-Down)
```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

**Characteristics**:
- Recursive approach
- Store results as they're computed
- Natural problem-solving flow
- Easier to understand and implement
- Time: O(n), Space: O(n) for recursion stack

### 2. Tabulation (Bottom-Up)
```python
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

**Characteristics**:
- Iterative approach
- Build solution from base cases up
- Can optimize space
- Avoids recursion overhead
- More efficient in practice

## Problem Recognition Patterns

### String Problems
- **Longest Common Subsequence (LCS)**
- **Longest Increasing Subsequence (LIS)**
- **Edit Distance (Levenshtein)**
- **Palindromic substrings**

### Array/Sequence Problems
- **House Robber** (can't rob adjacent)
- **Best Time to Buy/Sell Stock**
- **Coin Change** (minimum coins)
- **Jump Game** (reachability)

### Grid/2D Problems
- **Unique Paths** (counting paths)
- **Minimum Path Sum**
- **Maximal Square**
- **Dungeon Game**

### Optimization Problems
- **Knapsack** (0/1, unbounded)
- **Partition Equal Subset Sum**
- **Matrix Chain Multiplication**
- **Longest Palindromic Subsequence**

## State Definition Framework

### Key Questions
1. **What are the variables?** (indices, values, states)
2. **How do states relate?** (transitions, dependencies)
3. **Base cases?** (smallest subproblems)
4. **Final answer?** (which state(s) to return)

### Example: Coin Change
- **Variables**: Amount and available coins
- **State**: dp[i] = minimum coins for amount i
- **Transition**: dp[i] = min(dp[i-coin] + 1) for each coin
- **Base**: dp[0] = 0
- **Answer**: dp[target_amount]

## Advanced Techniques

### Space Optimization
- **1D Array**: Convert 2D DP to 1D when previous row only needed
- **Two Arrays**: Alternate between two arrays instead of full table
- **Sliding Window**: Only keep necessary states

### DP + Other Techniques
- **DP + Bitmask**: State includes bitmask (Traveling Salesman)
- **DP + Graph**: States are graph nodes
- **DP + Probability**: Computing probabilistic outcomes
- **DP + Greedy**: Combining approaches for complex problems

## Common Mistakes

1. **Wrong state definition**: Unclear what dp[i] represents
2. **Missing base cases**: Causes infinite recursion or wrong answers
3. **Incorrect transitions**: Wrong subproblem relationships
4. **Over-optimization**: Premature space optimization complicates logic
5. **Not memoizing**: Computing same subproblems repeatedly

## When to Use This Agent

- Identifying if a problem is suitable for DP
- Defining states and transitions
- Implementing memoization
- Converting to tabulation
- Optimizing space complexity
- Solving classic DP problems

## Classic Problems by Difficulty

### Beginner
- Fibonacci numbers
- Climbing stairs
- House robber (simple)

### Intermediate
- Longest increasing subsequence
- Coin change
- Unique paths
- Edit distance

### Advanced
- Knapsack variants
- Matrix chain multiplication
- Traveling salesman (TSP)
- Longest palindromic subsequence

## DP Checklist

- [ ] Problem has optimal substructure?
- [ ] Problem has overlapping subproblems?
- [ ] Can state be clearly defined?
- [ ] Can transitions be expressed?
- [ ] Base cases identified?
- [ ] Memoization or tabulation preferred?
- [ ] Can space be optimized?
- [ ] Time/space complexity acceptable?
