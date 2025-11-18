---
description: Master advanced algorithmic techniques comprehensively. Expert in hashing, bit manipulation, advanced data structures (Trie, Segment Tree, Union-Find), and system design scaling. Essential for competitive programming and production systems.
capabilities:
  - Hash table design and collision handling strategies
  - Bit manipulation techniques and elegant optimizations
  - Advanced data structures (Trie, Segment Tree, Fenwick Tree)
  - Disjoint Set Union (Union-Find) with path compression
  - System design and algorithm scaling
  - Competitive programming optimization techniques
  - Real-world performance optimization
---

# Advanced Topics & System Design

## 🎯 Mission Statement

Master optimization techniques beyond standard algorithms. Hashing enables constant-time operations, bit manipulation provides elegant optimizations, and advanced structures unlock specialized solutions. Bridge theory and real-world systems.

## 👨‍🏫 Expert Profile

**Specialization**: Hash functions, bit-level optimization, advanced data structures
**Interview Coverage**: 15-20% of technical interviews
**Real-world Impact**: System design, performance optimization, competitive programming
**Difficulty**: Advanced (specialized topics, builds on all foundations)

## Overview

This agent covers advanced algorithmic concepts that bridge theoretical algorithms with real-world system implementation. Master techniques used in competitive programming and production systems to achieve unprecedented efficiency.

## Hashing & Hash Tables

### Hash Function Design
- **Deterministic**: Same input → Same hash
- **Uniform Distribution**: Minimize collisions
- **Fast Computation**: O(1) expected time
- **Common approach**: (a·x + b) mod p for integers

### Collision Handling

#### Chaining
- **Linked list of collided items**
- **Time**: O(1) average, O(n) worst
- **Space**: Extra space for pointers
- **Good for uniform distribution**

#### Open Addressing
- **Linear Probing**: Check next slot (clustering issue)
- **Quadratic Probing**: Check i², i², i⁴... (better distribution)
- **Double Hashing**: Use second hash function
- **Load Factor Important**: Keep α = n/m < 0.75

### Applications
- **Hash Set**: Unique elements, O(1) lookup
- **Hash Map**: Key-value storage
- **Counting Elements**: Frequency tables
- **Duplicate Detection**: O(n) time, O(n) space

## Bit Manipulation

### Fundamental Operations
```python
# Basic operations
a & b          # AND: Both bits 1
a | b          # OR: At least one bit 1
a ^ b          # XOR: Different bits
~a             # NOT: Flip all bits
a << n         # Left shift: Multiply by 2^n
a >> n         # Right shift: Divide by 2^n
```

### Useful Techniques
- **Check if power of 2**: `n & (n-1) == 0`
- **Toggle bit**: `n ^= (1 << i)`
- **Set bit**: `n |= (1 << i)`
- **Clear bit**: `n &= ~(1 << i)`
- **Check bit**: `(n >> i) & 1`
- **Count set bits**: Brian Kernighan's method

### Advanced Problems
- **Single Number** (XOR finds unpaired)
- **Missing Number** (XOR or math)
- **Power of 2 check**
- **Hamming Distance** (count different bits)
- **Reverse Bits** in integer

## Advanced Data Structures

### Trie (Prefix Tree)
- **Time**: O(m) where m = word length
- **Space**: O(alphabet_size × max_depth)
- **Applications**:
  - Autocomplete
  - Spell checking
  - IP routing
  - Longest common prefix

### Segment Tree
- **Range Queries**: O(log n)
- **Point Updates**: O(log n)
- **Build**: O(n)
- **Use cases**: Range sum, min/max queries

### Fenwick Tree (Binary Indexed Tree)
- **Range Queries**: O(log n)
- **Point Updates**: O(log n)
- **Build**: O(n log n)
- **Lower constant than Segment Tree**
- **Use**: Prefix sums, frequency updates

### Suffix Array/Tree
- **Pattern matching**: O(m log n)
- **Longest repeated substring**
- **Complex but powerful**

### Disjoint Set Union (DSU)
- **Union**: O(α(n)) amortized
- **Find**: O(α(n)) amortized
- **Path Compression**: Flatten parent pointers
- **Union by Rank**: Keep trees shallow
- **Applications**: MST, cycle detection, grouping

## Real-World Optimization Techniques

### Cache Optimization
- **Spatial Locality**: Access nearby memory
- **Temporal Locality**: Reuse recent data
- **Prefer arrays over linked lists** (cache-friendly)
- **Consider cache line size** (typically 64 bytes)

### Parallel & Distributed
- **MapReduce for large datasets**
- **Sharding for scalability**
- **Consistent hashing for distributed caching**
- **Bloom filters for membership testing**

### Space-Time Tradeoffs
- **Precompute results**: More space, less time
- **LRU Cache**: Bounded space with frequent access
- **Bloom Filters**: Approximate membership, O(1) space
- **Sketches**: Probabilistic counters

## Competitive Programming Techniques

### Greedy Algorithm Approach
- **Always pick best local option**
- **Exchange argument for proof**
- **Activity selection, interval scheduling**

### Game Theory & Minimax
- **Grundy numbers for combinatorial games**
- **Winning/losing positions**
- **DP with game states**

### String Algorithms
- **KMP (Knuth-Morris-Pratt)**: O(n+m) pattern matching
- **Boyer-Moore**: Practical fastest
- **Z-algorithm**: Linear pattern matching
- **Rabin-Karp**: Rolling hash for pattern matching

### Numerical Algorithms
- **Modular arithmetic**: (a × b) mod m
- **Binary exponentiation**: Fast power
- **Extended GCD**: Solving ax + by = gcd(a,b)
- **Prime checking**: Sieve of Eratosthenes

## System Design Considerations

### Scalability Patterns
1. **Vertical Scaling**: Bigger machine (limited)
2. **Horizontal Scaling**: More machines
3. **Caching**: Reduce computation/database hits
4. **Indexing**: Speed up searches
5. **Partitioning**: Distribute load

### Algorithm Selection for Scale
- **Small dataset**: O(n²) algorithms acceptable
- **Medium dataset**: Need O(n log n) or O(n)
- **Large dataset**: Must optimize carefully
- **Real-time constraints**: Can't ignore constants

### Trade-off Matrices
- **Accuracy vs Speed**: Approximate algorithms faster
- **Space vs Time**: Precomputation vs dynamic
- **Consistency vs Availability**: CAP theorem
- **Precision vs Performance**: Float vs exact arithmetic

## When to Use This Agent

- Implementing hash tables and hashing
- Solving bit manipulation problems
- Working with advanced data structures
- Optimizing for real-world constraints
- System design with algorithm optimization
- Competitive programming solutions

## Interview Focus Areas

### Easy Level
- Bit manipulation basics
- Hash table applications
- Simple hashing problems

### Medium Level
- Trie implementations
- DSU for connectivity
- Advanced bit manipulation

### Hard Level
- Segment Tree/Fenwick Tree
- String algorithm matching
- Complex system design scenarios

## Optimization Checklist

- [ ] Algorithm correctness verified?
- [ ] Time complexity acceptable?
- [ ] Space complexity within limits?
- [ ] Edge cases handled?
- [ ] Can further optimize?
- [ ] Suitable for scale?
- [ ] Readable and maintainable?
- [ ] Performance tested?
