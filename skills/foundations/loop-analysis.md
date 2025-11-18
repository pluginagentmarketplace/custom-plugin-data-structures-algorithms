---
name: loop-analysis
description: Master nested loop complexity analysis. Learn to analyze simple loops, nested loops, and complex loop patterns. Critical for understanding O(n²), O(n³), and beyond. Use when calculating complexity of nested iterations.
---

# Loop Analysis

## Single Loop: O(n)
Loop runs n times, each iteration O(1) = O(n)

## Nested Loops: O(n²)
Loop inside loop, each n times = O(n²)

## Dependent Loops: O(n²)
Inner loop count depends on outer
Pattern: 1 + 2 + ... + n = n(n+1)/2 = O(n²)

## Key Patterns
- Nested same range: O(n²)
- Nested different ranges: O(n×m)
- Sequential loops: O(n+m)
- Loop with exponential work: O(2^n)

## Practice
- Triple nested: O(n³)
- Break early: Can reduce complexity
- Dependent bounds: Sum the series
