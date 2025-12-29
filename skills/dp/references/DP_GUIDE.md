# Dynamic Programming Guide

## DP Pattern
1. Define state: dp[i] means...
2. Find recurrence: dp[i] = f(dp[i-1], ...)
3. Base case: dp[0] = ...
4. Build answer

## Classic Problems
- **Fibonacci**: dp[i] = dp[i-1] + dp[i-2]
- **Coin Change**: dp[a] = min(dp[a], dp[a-coin] + 1)
- **LCS**: dp[i][j] = dp[i-1][j-1]+1 or max(dp[i-1][j], dp[i][j-1])
