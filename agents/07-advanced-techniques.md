---
description: Advanced problem-solving techniques, system design integration, coding interview strategies, LeetCode patterns, mock interviews, and real-world algorithm applications.
capabilities: ["greedy-algorithms", "backtracking", "two-pointers", "sliding-window", "union-find", "system-design", "interview-strategies"]
---

# Advanced Techniques & Interview Prep

Bridge the gap between **knowing algorithms and solving real problems**. This agent covers advanced techniques, interview strategies, and system design integration that separates strong candidates from exceptional ones.

## Advanced Problem-Solving Techniques

### 1. Greedy Algorithm Pattern
**Strategy**: Make locally optimal choice at each step, hoping for global optimum.

```python
# Activity Selection Problem
def activity_selection(activities):
    # activities = [(start, end), ...]
    activities.sort(key=lambda x: x[1])  # Sort by end time
    selected = [activities[0]]

    for i in range(1, len(activities)):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])

    return selected
    # Time: O(n log n), Space: O(n)
```

**When greedy works:**
- Optimal substructure (subproblems contribute to optimal solution)
- Greedy choice property (local optimum → global optimum)
- Examples: Huffman coding, Kruskal's MST, Dijkstra's (modified greedy)

**When it fails:**
- Longest increasing subsequence (needs DP)
- 0/1 Knapsack (needs DP)
- Example: Coin change with arbitrary denominations

### 2. Backtracking Pattern
**Strategy**: Explore all possibilities, prune impossible branches.

```python
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

**Backtracking template:**
```python
def backtrack(path, remaining):
    if is_complete(path):
        solution.append(path)
        return

    for choice in choices:
        if is_valid(choice):
            path.append(choice)
            backtrack(path, remaining - choice)
            path.pop()
```

**Classic problems:** Permutations, combinations, Sudoku solver, word search, partition problems

### 3. Two-Pointer Technique
**Strategy**: Use two pointers from different ends, moving strategically.

```python
# Container with Most Water
def max_area(heights):
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_water = max(max_water, width * height)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water
    # Time: O(n), Space: O(1)
```

**Use cases:**
- Sorted array problems
- Linked list problems (cycle detection, middle finding)
- String problems (palindrome checking)
- Array partition problems

### 4. Sliding Window Pattern
**Strategy**: Maintain a window of elements, expand and contract optimally.

```python
# Longest Substring Without Repeating Characters
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
    # Time: O(n), Space: O(min(n, alphabet_size))
```

**Template:**
```python
def sliding_window(s):
    window = {}
    left = 0
    result = 0

    for right in range(len(s)):
        # Expand window
        add_to_window(s[right], window)

        # Contract window while condition violated
        while condition_violated(window):
            remove_from_window(s[left], window)
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result
```

**Problems:** Substring problems, subarray problems, permutation matching

### 5. Union-Find (Disjoint Set Union)
**Strategy**: Efficiently track connected components and union operations.

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
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    # Time: O(α(n)) ≈ O(1) per operation
    # α(n) is inverse Ackermann function
```

**Applications:**
- Connected components
- Cycle detection in undirected graphs
- Minimum spanning tree (Kruskal's)
- Equivalence relations

## System Design Integration

### Algorithm Choice Based on Scale

```
Small scale (< 1K):     Simple O(n²) acceptable
Medium scale (1K-1M):   Need O(n log n) or O(n)
Large scale (1M-1B):    O(n) or O(n log n) with small constant
Huge scale (1B+):       Distributed algorithms, approximation

Memory:
< 1GB:     In-memory algorithms
1GB-1TB:   Streaming, external merge sort
> 1TB:     MapReduce, distributed processing
```

### Real-World Algorithm Selection Example

**Problem**: Index 1 billion search queries for auto-complete

```python
# Wrong: Sort all 1B queries - O(n log n), uses 40GB memory
sorted_queries = sorted(all_queries)

# Right: Use trie for prefix matching
# Build trie: O(n*m) where m=avg query length
# Query: O(m + k) where k=top results
# Memory: ~1-2GB (compressed trie)

class AutocompleteIndex:
    def __init__(self):
        self.trie = TrieNode()
        self.query_count = {}

    def add_query(self, query, count):
        self.query_count[query] = count
        self.trie.insert(query, count)

    def autocomplete(self, prefix, k=10):
        node = self.trie.find_prefix(prefix)
        return self.trie.get_top_k(node, k)
        # Much faster and memory-efficient!
```

## Coding Interview Strategies

### Strategy 1: Clarification Phase (2 minutes)
```
Questions to ask:
1. "What's the input size?" (determines algorithm choice)
2. "Are there constraints?" (time limit, memory limit)
3. "Can I modify input?" (in-place vs extra space)
4. "What about edge cases?" (empty, single element, duplicates)
5. "Need to optimize further?" (space or time)
```

### Strategy 2: Think Aloud
```
Interviewer wants to see:
- Your thought process
- Problem-solving approach
- Communication skills
- How you handle mistakes

Good: "Let me think... I could use binary search because
       the array is sorted. Time would be O(log n)."

Bad: [Silent for 3 minutes, then writes code]
```

### Strategy 3: Solution Progression
```
1. Brute Force (always start here)
   - Easy to implement
   - Shows you understand problem
   - Interviewer sees your baseline

2. Optimized Brute Force
   - Remove redundant work
   - Better data structures
   - Still intuitive

3. Optimal Solution
   - Best time/space complexity
   - Requires insight or pattern knowledge
   - Show trade-offs
```

### Strategy 4: Validation
```python
# Always test with:
# 1. Simple case (n=1 or n=2)
# 2. Expected case (normal input)
# 3. Edge cases (empty, single, duplicates)
# 4. Stress case (maximum size)

def test_solution():
    # Test case 1: Single element
    assert solution([1]) == ...

    # Test case 2: Example from problem
    assert solution([...]) == ...

    # Test case 3: Duplicates
    assert solution([1,1,1,1]) == ...

    # Test case 4: Maximum input
    assert solution(large_array) == ...
```

## Common Interview Problem Patterns

### Pattern 1: Tree/Graph Traversal
- Solution: DFS or BFS template
- Variants: Serialize, level-order, path sum
- Count: 20+ problems

### Pattern 2: Dynamic Programming
- Solution: Define state, write recurrence
- Variants: 1D, 2D, tree, interval, digit
- Count: 30+ problems

### Pattern 3: Sliding Window / Two Pointers
- Solution: Move pointers strategically
- Variants: Substring, subarray, partition
- Count: 25+ problems

### Pattern 4: Backtracking / Recursion
- Solution: DFS with state management
- Variants: Permutations, combinations, partition
- Count: 20+ problems

### Pattern 5: Bit Manipulation
- Solution: Understand bit operations
- Variants: Single number, power of two, subset
- Count: 15+ problems

## Mock Interview Checklist

### Before Interview
- [ ] Understand company's tech stack
- [ ] Know top 5 problems they ask
- [ ] Review data structures deep dive
- [ ] Practice 10 recent problems

### During Interview
- [ ] Read problem carefully (2 min)
- [ ] Ask clarifying questions (1-2 min)
- [ ] Think aloud about approach (3-5 min)
- [ ] Code solution (15-20 min)
- [ ] Test with examples (3-5 min)
- [ ] Discuss optimization (3-5 min)

### Problem Difficulty Scale
- **Easy**: Implement standard algorithm
- **Medium**: Combine 2 algorithms or notice pattern
- **Hard**: Deep insight required or multiple techniques

## Top Interview Problem Sources

1. **LeetCode** (Most popular)
   - Categories by topic
   - Difficulty progression
   - Company-specific filters

2. **HackerRank** (Structured learning)
   - Curriculum tracks
   - Contest practice

3. **CodeSignal** (Company interviews)
   - Real company problems
   - Interview simulators

4. **Cracking the Coding Interview** (Book)
   - 189 problems
   - Interview preparation

## Time Management in Interview

```
45-minute interview breakdown:
├─ 2 min: Read & clarify
├─ 8 min: Think aloud about approach
├─ 20 min: Code solution
├─ 10 min: Test & optimize
└─ 5 min: Discuss trade-offs
```

## Optimization Techniques Checklist

```
Runtime Optimization:
- [ ] Unnecessary work? Remove it
- [ ] Repeated work? Cache (memoization)
- [ ] Better algorithm? O(n²) → O(n log n)?
- [ ] Premature termination? Early exit?

Space Optimization:
- [ ] Extra data structure needed? Reduce
- [ ] Can use original array? In-place
- [ ] Recursive → iterative?
- [ ] Two variables instead of array?
```

## Red Flags in Interview

❌ Jumping into code without understanding
❌ Not thinking aloud
❌ Ignoring edge cases
❌ Not testing your code
❌ Pessimistic about optimization

✅ Clarifying questions first
✅ Explaining approach clearly
✅ Handling edge cases
✅ Testing thoroughly
✅ Optimizing when possible

## Learning Progression

### Week 1-2: Pattern Recognition
- [ ] Identify problem type (tree, DP, two-pointer, etc.)
- [ ] Solve 5 problems of each pattern
- [ ] Understand trade-offs

### Week 3-4: System Design Thinking
- [ ] Understand scalability constraints
- [ ] Choose algorithms based on input size
- [ ] Consider real-world trade-offs

### Week 5-6: Interview Simulation
- [ ] Practice mock interviews
- [ ] Work through problem in 45 minutes
- [ ] Get feedback on communication

### Week 7-8: Deep Dive & Polish
- [ ] Solve 50+ problems
- [ ] Optimize solutions further
- [ ] Master edge case handling

## Key Takeaways

✅ **Clarify before coding**: 2 minutes saved = better solution
✅ **Think aloud**: Interviewer sees your thought process
✅ **Pattern recognition**: Know when to apply greedy, DP, etc.
✅ **Edge cases matter**: Sorting, empty arrays, duplicates
✅ **Optimize progressively**: Brute force → better → optimal
✅ **Practice timing**: 45 minutes feels short when you start

## Final Interview Tips

1. **Master 5 hard problems deeply** → understand all variations
2. **Know your weaknesses** → practice those patterns more
3. **Communicate constantly** → think out loud
4. **Handle stress** → it's okay to say "let me think"
5. **Follow up** → "Can I optimize further?" shows initiative

---

**The Secret**: "It's not about being the smartest. It's about clearly showing you know how to think through problems systematically."
