---
name: dp-patterns
description: Master dynamic programming patterns. State definition, transitions, memoization vs tabulation. Solve 100+ classic problems.
---

# DP Patterns

## Pattern 1: Linear Sequences
Fibonacci, climbing stairs, house robber
- State: dp[i] = solution for first i elements
- Transition: Based on previous states

## Pattern 2: 2D Grids
Unique paths, minimum path sum
- State: dp[i][j] = solution at (i,j)
- Transition: From neighbors

## Pattern 3: Strings
Longest common subsequence, edit distance
- State: dp[i][j] = solution for s1[0..i], s2[0..j]
- Transition: Character matching/comparison

## Pattern 4: Optimization
Knapsack, coin change
- State: dp[i] = optimal for target i
- Transition: Try all options

## Memoization vs Tabulation
- Memoization: Top-down, recursive
- Tabulation: Bottom-up, iterative
- Both: O(n) space and time typically

## Key Insight
Identify overlapping subproblems and optimal substructure
