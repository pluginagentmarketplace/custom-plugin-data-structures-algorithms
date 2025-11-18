---
name: advanced-techniques-skill
description: Greedy algorithms, backtracking, two-pointers, sliding window, union-find, bit manipulation, and interview preparation strategies for advanced problem-solving.
---

# Advanced Techniques Skill

## Quick Start

**Advanced Problem-Solving Patterns:**
1. **Greedy**: Make locally optimal choice
2. **Backtracking**: Explore all possibilities
3. **Two-Pointers**: Partition or match endpoints
4. **Sliding Window**: Optimize subarray problems
5. **Union-Find**: Track connected components
6. **Bit Manipulation**: Use binary properties

## Greedy Algorithms

**When it works:**
- Optimal substructure exists
- Greedy choice leads to global optimum
- Examples: Huffman coding, Dijkstra, Kruskal

**When it fails:**
- Longest increasing subsequence
- 0/1 Knapsack
- Must use DP instead

```python
# Activity Selection (greedy works!)
def activity_selection(activities):
    # activities = [(start, end), ...]
    activities.sort(key=lambda x: x[1])  # Sort by end time
    selected = [activities[0]]

    for i in range(1, len(activities)):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])

    return selected
    # Time: O(n log n), Space: O(n)
    # Greedy: always pick earliest ending activity
```

## Backtracking Pattern

```python
def backtrack(path, remaining):
    # Base case
    if is_complete(path):
        solution.append(path[:])
        return

    # Try all choices
    for choice in get_choices(remaining):
        if is_valid(choice):
            # Make choice
            path.append(choice)
            # Explore
            backtrack(path, remaining - choice)
            # Undo (backtrack)
            path.pop()

# N-Queens Problem
def solve_nqueens(n):
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i] == col:
                return False
        # Check diagonals
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(board, row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1

    solutions = []
    backtrack([-1] * n, 0)
    return solutions
    # Time: O(n!), Space: O(n)
```

**Classic problems:**
- Permutations, combinations
- Sudoku solver
- Word search
- Partition problems
- Path finding

## Two-Pointer Technique

### Pattern 1: Opposite Ends

```python
# Container with Most Water
def max_area(heights):
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_water = max(max_water, width * height)

        # Move shorter boundary
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water
    # Time: O(n), Space: O(1)
```

### Pattern 2: Partition

```python
# Move zeros to end
def move_zeroes(nums):
    left = 0  # Insert position
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    # Time: O(n), Space: O(1)
```

### Pattern 3: Linked List

```python
# Find middle of linked list
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # slow is at middle
    # Time: O(n), Space: O(1)

# Detect cycle in linked list
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
    # Time: O(n), Space: O(1)
```

## Sliding Window Pattern

```python
def sliding_window(s, constraints):
    window = {}
    left = 0
    result = 0

    for right in range(len(s)):
        # Add to window
        window[s[right]] = window.get(s[right], 0) + 1

        # Shrink while invalid
        while not is_valid(window, constraints):
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result

# Longest Substring Without Repeating
def length_of_longest_substring(s):
    char_idx = {}
    max_len = 0
    left = 0

    for right in range(len(s)):
        if s[right] in char_idx and char_idx[s[right]] >= left:
            left = char_idx[s[right]] + 1

        char_idx[s[right]] = right
        max_len = max(max_len, right - left + 1)

    return max_len
    # Time: O(n), Space: O(min(n, charset))
```

**Use cases:**
- Substring problems
- Subarray problems
- Fixed/variable window sizes

## Union-Find (Disjoint Set Union)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    # Time: O(α(n)) ≈ O(1)
    # Space: O(n)

# Detect cycle in undirected graph
def has_cycle(graph):
    uf = UnionFind(len(graph))
    for u in range(len(graph)):
        for v in graph[u]:
            if u < v:  # Avoid checking twice
                if uf.connected(u, v):
                    return True
                uf.union(u, v)
    return False
```

**Applications:**
- Connected components
- Cycle detection
- MST (Kruskal's algorithm)
- Equivalence relations

## Bit Manipulation

```python
# Check if power of 2
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Count set bits
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Single Number (find number appearing once in array where all appear twice)
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR: a ^ a = 0, a ^ 0 = a
    return result

# Subsets using bitmask
def subsets(nums):
    n = len(nums)
    result = []
    for i in range(1 << n):  # 2^n possibilities
        subset = []
        for j in range(n):
            if i & (1 << j):  # Check if jth bit is set
                subset.append(nums[j])
        result.append(subset)
    return result
```

**Key operations:**
- `a & b`: Bitwise AND
- `a | b`: Bitwise OR
- `a ^ b`: Bitwise XOR (toggle)
- `~a`: Bitwise NOT
- `a << k`: Left shift (multiply by 2^k)
- `a >> k`: Right shift (divide by 2^k)

## Interview Preparation

### Clarification Phase (2 minutes)

```
Ask:
1. "What's the input size?" → Determines algorithm
2. "What are constraints?" → Memory, time limits
3. "Can I modify input?" → In-place vs extra space
4. "What about edge cases?" → Empty, single, duplicates
5. "Any follow-up?" → Optimization later
```

### Solution Progression

```
1. Brute Force (always start)
   - Understand problem
   - Simple to code
   - Shows baseline

2. Optimized Brute Force
   - Remove redundant work
   - Better data structures
   - Still intuitive

3. Optimal
   - Best time/space
   - Show trade-offs
   - Can explain improvements
```

### Testing Strategy

```python
def test_solution():
    # Test 1: Simple case
    assert solution([1]) == ...

    # Test 2: Example from problem
    assert solution([...]) == ...

    # Test 3: Edge case
    assert solution([]) == ...
    assert solution([1, 1, 1]) == ...

    # Test 4: Large input
    assert solution(large_test) == ...
```

## Problem Pattern Recognition

| Pattern | Algorithm | Example |
|---------|-----------|---------|
| Sorted array | Binary search | Search in rotated |
| Tree/Graph | DFS/BFS | Connected components |
| Optimization | DP | Knapsack |
| Partition | Two-pointer | Container with water |
| Substring/Subarray | Sliding window | Longest without repeating |
| Connected components | Union-find | Number of islands |
| Greedy choice | Greedy | Activity selection |
| Try all | Backtracking | Permutations |
| Binary properties | Bit operations | Single number |

## Interview Red Flags

❌ Jump into code without understanding
❌ Don't think aloud
❌ Ignore edge cases
❌ Don't test code
❌ Don't optimize

✅ Clarify requirements first
✅ Explain approach
✅ Handle edge cases
✅ Test thoroughly
✅ Discuss optimization

## Time Management

```
45-minute interview:
├─ 2 min: Read & clarify
├─ 8 min: Think about approach
├─ 20 min: Code solution
├─ 10 min: Test & optimize
└─ 5 min: Discuss trade-offs
```

## Mock Interview Checklist

- [ ] Understand problem completely
- [ ] Ask clarifying questions
- [ ] Explain approach before coding
- [ ] Code cleanly with comments
- [ ] Test with multiple cases
- [ ] Discuss time/space complexity
- [ ] Suggest optimizations
- [ ] Handle edge cases

## Real-World Integration

**System Design Context:**
```
Algorithm choice depends on:
1. Input size: 1M vs 1B elements
2. Memory: 1GB vs 1TB available
3. Latency: Interactive vs batch
4. Throughput: One query vs many/second
5. Distribution: Centralized vs distributed
```

**Example:** Searching 1M users
- ❌ Linear O(n) = 1M operations
- ✅ Binary search O(log n) = 20 operations
- ✅ Hash lookup O(1) = 1 operation

---

**Advanced techniques separate good developers from great ones!**
