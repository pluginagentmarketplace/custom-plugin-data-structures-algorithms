---
name: hashing
description: Master hash tables. Hash functions, collision handling, complexity analysis. O(1) lookups with good design.
---

# Hashing

## Hash Function
- Deterministic
- Uniform distribution
- Fast computation
- Minimize collisions

## Collision Handling

### Chaining
- Linked list per bucket
- O(1) avg, O(n) worst
- Space: Pointers

### Open Addressing
- Linear probing
- Quadratic probing
- Double hashing

## Load Factor
- α = n/m (elements/buckets)
- Keep α < 0.75
- Resize when exceeded

## Complexity
- Insert: O(1) avg
- Delete: O(1) avg
- Search: O(1) avg
- Worst: O(n)

## Hash Table Applications
- Duplicate detection
- Frequency counting
- Caching (with LRU)
- Set/Dictionary
