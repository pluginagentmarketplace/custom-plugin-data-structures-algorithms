# /explore-agent

Explore and understand all available specialized agents in the plugin.

## Description

This command helps you discover what each agent specializes in and when to use them.

## Available Agents

### 1. 📚 Foundations & Complexity Analysis
**Specialization**: Algorithm efficiency and Big O notation
- Time and space complexity analysis
- Asymptotic notation and Big O classes
- Algorithm performance prediction
- Complexity comparison and optimization

**When to Use**:
- Starting your DSA journey
- Analyzing algorithm efficiency
- Choosing between algorithm approaches
- Preparing for complexity questions

**Key Topics**:
- Big O, Omega, Theta notation
- Best/Average/Worst case analysis
- Amortized complexity
- Practical complexity estimation

---

### 2. 🔗 Linear Data Structures
**Specialization**: Sequential data organization
- Arrays and strings manipulation
- Linked lists (singly, doubly, circular)
- Stacks and queues
- Two-pointer and sliding window techniques

**When to Use**:
- Working with sequential data
- Implementing data structure operations
- Solving array/string problems
- Learning fundamental structures

**Key Topics**:
- Basic operations and implementations
- Linked list algorithms (reversal, cycle detection)
- Stack applications (expression evaluation)
- Queue patterns (BFS preparation)

---

### 3. 🌳 Non-Linear Data Structures
**Specialization**: Hierarchical and connected structures
- Binary trees and BSTs
- Balanced trees (AVL, Red-Black)
- Heaps and priority queues
- Tries for string patterns
- Graph basics

**When to Use**:
- Organizing hierarchical data
- Implementing priority queues
- Solving tree problems
- Preparing for graph algorithms
- String pattern searching

**Key Topics**:
- Tree traversals (in-order, pre-order, post-order)
- BST operations and validation
- Heap operations and heapify
- Trie for autocomplete
- LCA and other tree problems

---

### 4. 🔍 Searching & Sorting Algorithms
**Specialization**: Search and sort techniques
- Linear and binary search
- Comparison-based sorting (Merge, Quick, Heap)
- Non-comparison sorts (Counting, Radix)
- Search optimization techniques

**When to Use**:
- Optimizing search performance
- Choosing sorting algorithms
- Solving interview problems
- Understanding algorithm trade-offs

**Key Topics**:
- Binary search variations
- Quick sort and Merge sort internals
- Stability and in-place requirements
- Counting and Radix sort
- Two-pointer and sliding window

---

### 5. 💡 Dynamic Programming
**Specialization**: Optimization through subproblems
- Problem identification and state definition
- Memoization vs tabulation
- Classic DP patterns
- Space optimization techniques

**When to Use**:
- Identifying DP problems
- Solving optimization problems
- Preparing for interview DP questions
- Understanding state transitions

**Key Topics**:
- Overlapping subproblems and optimal substructure
- String DP (LCS, edit distance)
- Array DP (LIS, coin change)
- 2D grid problems
- Knapsack variants

---

### 6. 🗺️ Graph Algorithms
**Specialization**: Connected data relationships
- Graph traversal (BFS, DFS)
- Shortest path algorithms (Dijkstra, Bellman-Ford)
- Minimum spanning trees
- Topological sorting
- Connectivity and cycle detection

**When to Use**:
- Solving graph problems
- Finding shortest paths
- Computing spanning trees
- Detecting cycles and connectivity
- Network and tree problems

**Key Topics**:
- Adjacency list and matrix representations
- BFS and DFS applications
- Dijkstra and Floyd-Warshall
- Kruskal and Prim algorithms
- Union-Find for connectivity

---

### 7. 🚀 Advanced Topics & System Design
**Specialization**: Optimization and real-world applications
- Hash table design and collision handling
- Bit manipulation techniques
- Advanced data structures (Segment Tree, Fenwick Tree)
- Hashing and hash functions
- Real-world system design patterns

**When to Use**:
- Solving bit manipulation problems
- Implementing custom hash tables
- Using advanced data structures
- Optimizing for production systems
- Competitive programming

**Key Topics**:
- Hashing and hash collision strategies
- Bit operations and tricks
- Union-Find for disjoint sets
- Segment trees for range queries
- LRU Cache and Bloom filters
- KMP and other string algorithms

---

## How to Use This Command

1. **Explore**: Read descriptions of all agents
2. **Identify**: Find agents matching your interests
3. **Deep Dive**: Ask Claude to explain specific topics
4. **Practice**: Use `/practice` to get problems for that agent

## Agent Dependencies

```
Foundations ↓
├── Linear Structures ↓
├── Non-Linear Structures → Searching & Sorting
├── Searching & Sorting ↓
├── Dynamic Programming
├── Graph Algorithms ↓
└── Advanced Topics (applies to all)
```

## Recommended Learning Order

1. **Start**: Foundations (always first)
2. **Build**: Linear → Non-Linear → Searching/Sorting
3. **Optimize**: Dynamic Programming
4. **Connect**: Graph Algorithms
5. **Master**: Advanced Topics

## Quick Selection

- **If you have < 2 hours**: Foundations
- **If you like sequences**: Linear Structures
- **If you like hierarchies**: Non-Linear Structures
- **If you like optimization**: Dynamic Programming
- **If you like connections**: Graph Algorithms
- **If you want everything**: Start with Foundations, then follow the order

## Next Steps

- Use `/practice` to solve problems from an agent
- Use `/learn` to get a personalized learning path
- Ask Claude questions about specific agent topics
