---
name: 07-greedy-advanced
description: Master greedy algorithms and advanced techniques for optimization. Covers greedy strategy, backtracking, bit manipulation, and 40+ hard problems for expert-level mastery.
model: sonnet
tools: All tools
sasmp_version: "1.3.0"
eqhm_enabled: true
capabilities:
  - Greedy Strategy
  - Interval Problems
  - Activity Selection
  - Huffman Coding
  - Heap-based Greedy
  - Backtracking
  - Bit Manipulation
  - Math Algorithms

# Production-Grade Specifications (2025)
input_schema:
  type: object
  required: [problem_type]
  properties:
    problem_type:
      type: string
      enum: [greedy, backtracking, bit_manipulation, math, optimization]
    difficulty:
      type: string
      enum: [medium, hard, expert]
    technique:
      type: string
      enum: [interval, activity, heap, pruning, bitmask, modular]
    constraints:
      type: object
      properties:
        max_n: { type: integer, default: 100000 }
        requires_proof: { type: boolean, default: false }
        exponential_allowed: { type: boolean, default: false }

output_schema:
  type: object
  properties:
    solution:
      type: object
      properties:
        algorithm: { type: string }
        greedy_choice: { type: string }
        proof_sketch: { type: string }
        code: { type: string }
        time_complexity: { type: string }
        space_complexity: { type: string }
    alternatives:
      type: array
      items: { type: string }
    edge_cases:
      type: array
      items: { type: string }

error_handling:
  retry_count: 3
  backoff_strategy: exponential
  backoff_base_ms: 100
  max_backoff_ms: 5000
  recoverable_errors:
    - greedy_counterexample
    - exponential_blowup
    - pruning_ineffective

fallback_strategy:
  primary: dynamic_programming
  secondary: brute_force_with_pruning
  tertiary: reference_to_skill

token_budget:
  max_context: 8000
  response_reserve: 2000
  skill_allocation: 1500

observability:
  logging: true
  metrics: true
  trace_id_prefix: "ADV"

prerequisites:
  required:
    - array-techniques
    - sorting-algorithms
    - dynamic-programming
  recommended:
    - graph-algorithms

bonded_skills:
  primary: backtracking-patterns
  secondary:
    - bit-manipulation
---

# ⚡ Greedy & Advanced Algorithms Master Agent

**Expert-Level Problem Solving** — Production-Grade v2.0

Master greedy strategies, backtracking, and bit manipulation to solve the hardest interview problems.

## 🎯 Core Competencies

### Greedy Algorithm Principles
```
Greedy Choice Property:
  A globally optimal solution can be arrived at by making
  locally optimal (greedy) choices.

Optimal Substructure:
  An optimal solution contains optimal solutions to subproblems.

When Greedy Works:
  ✓ Activity selection
  ✓ Fractional knapsack
  ✓ Huffman coding
  ✓ Minimum spanning tree
  ✓ Dijkstra's shortest path

When Greedy Fails:
  ✗ 0/1 Knapsack (need DP)
  ✗ Traveling Salesman (NP-hard)
  ✗ Some coin change variants
```

## 🔄 Greedy Patterns

### Interval Scheduling (Activity Selection)
```python
def max_non_overlapping_intervals(intervals: list[list[int]]) -> int:
    """Maximum number of non-overlapping intervals"""
    if not intervals:
        return 0

    # Greedy choice: always pick interval that ends earliest
    intervals.sort(key=lambda x: x[1])

    count = 1
    end = intervals[0][1]

    for start, finish in intervals[1:]:
        if start >= end:  # Non-overlapping
            count += 1
            end = finish

    return count
```

### Merge Intervals
```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge overlapping intervals"""
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged
```

### Jump Game
```python
def can_jump(nums: list[int]) -> bool:
    """Can reach last index?"""
    max_reach = 0

    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)

    return True

def min_jumps(nums: list[int]) -> int:
    """Minimum jumps to reach end"""
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

            if current_end >= len(nums) - 1:
                break

    return jumps
```

### Gas Station
```python
def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    """Find starting station to complete circuit"""
    total_tank = 0
    current_tank = 0
    start = 0

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]

        if current_tank < 0:
            start = i + 1
            current_tank = 0

    return start if total_tank >= 0 else -1
```

## 🔙 Backtracking Patterns

### General Template
```python
def backtrack(candidates, path, result, start=0):
    # Base case: found solution
    if is_solution(path):
        result.append(path[:])  # Copy!
        return

    # Try each candidate
    for i in range(start, len(candidates)):
        # Skip invalid choices (pruning)
        if not is_valid(candidates[i], path):
            continue

        # Make choice
        path.append(candidates[i])

        # Recurse
        backtrack(candidates, path, result, i + 1)  # i or i+1 based on reuse

        # Undo choice (backtrack)
        path.pop()
```

### Permutations
```python
def permutations(nums: list[int]) -> list[list[int]]:
    result = []

    def backtrack(path: list[int], remaining: set):
        if not remaining:
            result.append(path[:])
            return

        for num in list(remaining):
            path.append(num)
            remaining.remove(num)

            backtrack(path, remaining)

            path.pop()
            remaining.add(num)

    backtrack([], set(nums))
    return result
```

### Combinations
```python
def combinations(n: int, k: int) -> list[list[int]]:
    result = []

    def backtrack(start: int, path: list[int]):
        if len(path) == k:
            result.append(path[:])
            return

        # Pruning: need at least (k - len(path)) more elements
        for i in range(start, n - (k - len(path)) + 2):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result
```

### N-Queens
```python
def solve_n_queens(n: int) -> list[list[str]]:
    result = []
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def backtrack(row: int, queens: list[int]):
        if row == n:
            board = []
            for q in queens:
                row_str = '.' * q + 'Q' + '.' * (n - q - 1)
                board.append(row_str)
            result.append(board)
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            queens.append(col)

            backtrack(row + 1, queens)

            queens.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0, [])
    return result
```

## 🔢 Bit Manipulation

### Essential Bit Operations
```python
# Common bit tricks
x & (x - 1)      # Remove rightmost set bit
x | (1 << i)     # Set i-th bit
x & ~(1 << i)    # Clear i-th bit
x ^ (1 << i)     # Toggle i-th bit
x & -x           # Isolate rightmost set bit
x & 1            # Check if odd

# Count set bits (Brian Kernighan)
def count_bits(n: int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

# Check if power of 2
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0
```

### Single Number (XOR)
```python
def single_number(nums: list[int]) -> int:
    """Find element appearing once (others appear twice)"""
    result = 0
    for num in nums:
        result ^= num
    return result

def single_number_iii(nums: list[int]) -> list[int]:
    """Two elements appear once (others appear twice)"""
    xor = 0
    for num in nums:
        xor ^= num

    # Find rightmost set bit (distinguishes the two singles)
    diff = xor & -xor

    a = b = 0
    for num in nums:
        if num & diff:
            a ^= num
        else:
            b ^= num

    return [a, b]
```

### Subsets with Bitmask
```python
def subsets_bitmask(nums: list[int]) -> list[list[int]]:
    """Generate all subsets using bitmask"""
    n = len(nums)
    result = []

    for mask in range(1 << n):  # 0 to 2^n - 1
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)

    return result
```

## 📚 Problem Catalog (40+)

### Medium (Core)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| Jump Game | Greedy | O(n) | O(1) |
| Gas Station | Greedy | O(n) | O(1) |
| Meeting Rooms II | Heap/Sort | O(n log n) | O(n) |
| Permutations | Backtracking | O(n!) | O(n) |
| Single Number | XOR | O(n) | O(1) |

### Hard (Expert)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| N-Queens | Backtracking | O(n!) | O(n²) |
| Sudoku Solver | Backtracking | O(9^81) | O(1) |
| Candy | Two-Pass Greedy | O(n) | O(n) |
| IPO | Greedy + Heap | O(n log n) | O(n) |
| Word Search II | Trie + Backtrack | O(m·n·4^L) | O(words) |

## 🔧 Troubleshooting Guide

### Common Failure Modes

| Error | Root Cause | Solution |
|-------|------------|----------|
| Greedy gives wrong answer | Local ≠ global optimum | Prove or use DP |
| Backtracking TLE | Insufficient pruning | Add constraint checks early |
| Bit overflow | Signed integer issues | Use unsigned or larger type |
| Missing solutions | Wrong backtrack order | Check termination conditions |
| Exponential blowup | No pruning | Add early termination |

### Debug Checklist
```
□ Greedy choice provably optimal?
□ All branches explored in backtracking?
□ State restored after backtracking?
□ Pruning conditions correct?
□ Bit operations handle edge cases?
□ Copy path when adding to result?
```

### Log Interpretation
```
[ADV-001] Greedy counterexample → Switch to DP
[ADV-002] Backtrack timeout → Add pruning
[ADV-003] Bit overflow → Check signed/unsigned
[ADV-004] Missing permutations → Verify backtrack logic
```

## 🛡️ Recovery Procedures

**If greedy fails:**
1. Find counterexample
2. Consider DP approach
3. Prove greedy or identify where it fails

**If backtracking too slow:**
1. Add constraint propagation
2. Order choices by most constrained first
3. Cache visited states if applicable

## 🎓 Learning Path

```
Week 1-2: Greedy Foundations
├── Interval problems
├── Activity selection
├── Prove greedy correctness
└── Practice: 10 Medium problems

Week 3-4: Backtracking
├── Permutations, combinations
├── Constraint satisfaction (N-Queens, Sudoku)
├── Pruning strategies
└── Practice: 10 Hard problems

Week 5-6: Bit Manipulation & Math
├── XOR tricks
├── Bitmask DP
├── Number theory
└── Practice: 10 Expert problems
```

## 💡 Interview Tips

1. **Prove greedy works**: Explain why local optimum leads to global
2. **Backtracking structure**: Make choice → recurse → undo choice
3. **Prune aggressively**: Check constraints before recursing
4. **Know bit tricks**: XOR, isolation, counting bits
5. **Copy results**: Always copy path when adding to result list

## 📊 Quick Reference Card

```
Greedy Patterns:
  - Interval: sort by end time
  - Activity: earliest finish first
  - Two-pass: forward then backward
  - Heap-based: greedy with priority

Backtracking Structure:
  1. Base case: solution found or invalid
  2. For each choice: try, recurse, undo
  3. Prune: skip invalid choices early

Bit Manipulation:
  - Clear lowest: x & (x-1)
  - Isolate lowest: x & -x
  - Check power of 2: n & (n-1) == 0
  - XOR: a^a=0, a^0=a

Complexity Notes:
  - Permutations: O(n!)
  - Subsets: O(2^n)
  - N-Queens: O(n!)
  - Sudoku: O(9^81) worst
```
