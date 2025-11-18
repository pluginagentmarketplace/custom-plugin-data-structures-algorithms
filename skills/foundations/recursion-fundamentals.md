---
name: recursion-fundamentals
description: Understand recursion complexity analysis. Learn call trees, recursion depth, and basic recurrence relations. Foundation for merge sort, quick sort, and recursive algorithms.
---

# Recursion Fundamentals

## Call Tree Concept
Each recursive call = node in tree

## Linear Recursion: O(n)
- n calls, each O(1) work = O(n)
- Depth: n
- Space: O(n) call stack

## Binary Recursion: O(2^n)
- Fibonacci without memoization
- 2 calls per level, depth n
- Exponential blowup

## Divide & Conquer: O(n log n)
- Split problem in half
- Depth: log(n)
- Work per level: O(n)
- Total: O(n log n)

## Key Insight
Recurrence: T(n) = a·T(n/b) + f(n)
- a = calls per level
- b = size reduction
- Master Theorem solves this
