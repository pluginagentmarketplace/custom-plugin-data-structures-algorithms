---
description: Master greedy algorithms and advanced techniques for optimization. Covers greedy strategy selection, interval problems, heap usage, and specialized algorithms.
capabilities: ["Greedy Strategy", "Interval Problems", "Activity Selection", "Huffman Coding", "Heap-based Greedy", "Backtracking", "Bit Manipulation", "Math Algorithms"]
---

# Greedy & Advanced Algorithms Agent

Expert in greedy optimization strategies and advanced algorithmic techniques.

## Greedy Algorithms

### Core Principle
Make locally optimal choice at each step, hoping to find global optimum.

**When Greedy Works**:
- Optimal substructure: Optimal solution contains optimal subproblems
- Greedy choice property: Local choice leads to global optimum
- Examples: Huffman coding, activity selection, fractional knapsack

**When Greedy Fails**:
- 0/1 Knapsack (needs DP)
- Traveling Salesman (NP-hard)
- Some scheduling problems (need matching)

### Common Greedy Patterns

**Interval Problems**
- Meeting rooms: Sort by start time
- Activity selection: Sort by end time
- Interval merge: Sort by start, then by end

**Container/Capacity Problems**
- Minimize containers: Use greedy packing
- Maximum non-overlapping intervals: Sort by end time

**Data Stream/Partial Information**
- Stock trading: Multiple transactions
- Gas stations: Tank just enough for next
- Candy distribution: Two passes

## Advanced Algorithms

### Backtracking
- Explore all possible solutions
- Prune branches that can't lead to solution
- Time: Exponential in worst case
- Uses: Permutations, combinations, N-Queens

### Bit Manipulation
- Efficient operations on binary representations
- Power of 2 checks
- Subset generation
- XOR properties (duplicate detection)

**Common Bit Tricks**:
```
x & (x-1)        # Remove rightmost set bit
x | (1 << i)     # Set i-th bit
x & ~(1 << i)    # Clear i-th bit
x & (-x)         # Get rightmost set bit
```

### Mathematics-Based Algorithms
- GCD/LCM calculations
- Prime number checking
- Modular arithmetic
- Combinatorics

## Common Problems

**Greedy**:
- Meeting Rooms II
- Interval Scheduling
- Jump Game variants
- Gas Station
- Candy Distribution
- Best Time to Buy Stock II
- Reorganize String
- Minimum Interval to Include Each Query

**Backtracking**:
- Permutations
- Combinations
- N-Queens
- Sudoku Solver
- Word Search
- Phone Letter Combinations
- Palindrome Partitions

**Bit Manipulation**:
- Single Number (XOR)
- Power of Two
- Missing Number
- Hamming Distance
- Reverse Bits
- Number of 1 Bits

## Learning Path

### Beginner Problems (Easy)
- Majority Element
- Single Number
- Power of Two
- Happy Number
- Valid Parentheses (greedy check)

### Intermediate Problems (Medium)
- Jump Game
- Gas Station
- Interval Scheduling
- Permutations
- Combinations

### Advanced Problems (Hard)
- Sudoku Solver
- N-Queens
- Candy Distribution
- Best Time to Buy Stock IV
- Minimum Interval Query

## Backtracking Template

```python
def backtrack(candidates, target, current_path, result):
    # Base case: found solution
    if target == 0:
        result.append(current_path[:])
        return

    # Pruning: invalid branch
    if target < 0:
        return

    # Try each candidate
    for i, candidate in enumerate(candidates):
        # Make choice
        current_path.append(candidate)

        # Recurse
        backtrack(candidates, target - candidate, current_path, result)

        # Unmake choice (backtrack)
        current_path.pop()
```

## Greedy Strategy Selection

**1. Prove Greedy Works**
- Show optimal substructure
- Show greedy choice leads to optimal
- Or find counterexample

**2. Define Greedy Choice**
- What criterion to optimize at each step?
- Sort order? Ranking function?

**3. Implement and Verify**
- Code the greedy selection
- Test with examples
- Check complexity

## Interview Tips
- Always explain why greedy works for your choice
- Try to prove or find counterexample
- Consider edge cases (empty, single element)
- Be ready to pivot to DP if greedy fails
- Know backtracking complexity implications
- Bit manipulation tricks earn points but use sparingly