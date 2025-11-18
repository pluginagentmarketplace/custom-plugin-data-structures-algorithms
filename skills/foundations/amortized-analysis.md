---
name: amortized-analysis
description: Understand amortized time complexity. Learn why vector append is O(1) amortized. Critical for understanding dynamic data structures.
---

# Amortized Analysis

## Dynamic Array Append
Sometimes resize (O(n)), usually append (O(1))
Average: O(1) per operation

## Why?
Resize happens logarithmically
O(n) total work / n operations = O(1) amortized

## Common Examples
- Vector append: O(1) amortized
- Hash table insert: O(1) amortized  
- Incremental operations: Often amortized O(1)

## Key Pattern
Individual operations vary, but sequence averages to better complexity
