# DSA Mastery Plugin for Claude Code

🚀 **Ultimate Data Structures & Algorithms Plugin** - Master DSA with 7 specialized agents, 8+ skills, 300+ problems, and complete interview preparation.

Built for Claude Code with production-ready plugin format.

## 🎯 Overview

This plugin provides a complete learning system for mastering data structures and algorithms:

- **7 Specialized Agents**: Arrays, Trees, Graphs, DP, Sorting, Hash Tables, Greedy & Advanced
- **8+ Invokable Skills**: Code implementations with time/space complexity analysis
- **4 Interactive Commands**: Problem solver, difficulty selector, interview prep, complexity analyzer
- **300+ Problems**: From LeetCode Easy to Hard with solutions
- **Complete Interview Guide**: Top 20 questions, strategies, and best practices

## 📦 Plugin Structure

```
dsa-mastery-plugin/
├── .claude-plugin/
│   └── plugin.json                    # Plugin manifest
├── agents/                            # 7 DSA Agent definitions
│   ├── 01-arrays-lists.md
│   ├── 02-trees-binary.md
│   ├── 03-graphs.md
│   ├── 04-dynamic-programming.md
│   ├── 05-sorting-searching.md
│   ├── 06-hash-tables.md
│   └── 07-greedy-advanced.md
├── commands/                          # 4 Interactive Commands
│   ├── problem-solver.md
│   ├── difficulty-selector.md
│   ├── interview-prep.md
│   └── complexity-analyzer.md
├── skills/                            # 8 Code Implementation Skills
│   ├── arrays/SKILL.md
│   ├── trees/SKILL.md
│   ├── graphs/SKILL.md
│   ├── dp/SKILL.md
│   ├── sorting/SKILL.md
│   ├── hashing/SKILL.md
│   ├── backtracking/SKILL.md
│   └── bitmanip/SKILL.md
├── hooks/
│   └── hooks.json
└── README.md
```

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/pluginagentmarketplace/custom-plugin-data-structures-algorithms.git

# Load in Claude Code
# Option 1: From local directory
# In Claude Code settings: Add Plugin → ./custom-plugin-data-structures-algorithms

# Option 2: From absolute path
# ~/.claude-code/plugins/custom-plugin-data-structures-algorithms
```

### First Commands

```bash
# Find problems to solve
/problem-solver

# Choose your skill level
/difficulty-selector

# Prepare for interviews
/interview-prep

# Understand complexity
/complexity-analyzer
```

## 👥 7 Specialized DSA Agents

### 1. 📚 Arrays & Lists Agent
- Array operations and manipulation
- Sliding window technique
- Two pointers approach
- Prefix sum patterns
- **Skills**: Array techniques with code examples
- **Problems**: 50+ problems from Easy to Hard

### 2. 🌳 Trees & Binary Trees Agent
- Tree traversals (DFS, BFS, Inorder, Preorder)
- Binary Search Trees
- Balanced trees and AVL trees
- Tree dynamic programming
- **Skills**: Complete tree traversal implementations
- **Problems**: 40+ tree problems with solutions

### 3. 🕸️ Graphs & Graph Algorithms Agent
- Graph representations
- DFS and BFS traversal
- Shortest path algorithms (Dijkstra)
- Topological sorting
- Union-Find data structure
- **Skills**: Graph algorithm implementations
- **Problems**: 35+ graph problems

### 4. ⚡ Dynamic Programming Agent
- Memoization and tabulation
- State design and optimization
- Sequence DP patterns
- Knapsack problems and variants
- **Skills**: DP implementations with complexity
- **Problems**: 45+ DP problems from basics to hard

### 5. 🔍 Searching & Sorting Agent
- Sorting algorithms (Quick, Merge, Heap)
- Binary search and variations
- Linear-time sorting (Counting, Radix)
- Custom sorting with comparators
- **Skills**: Complete sorting algorithm codes
- **Problems**: 30+ sorting and searching problems

### 6. #️⃣ Hash Tables & Sets Agent
- Hash maps and hash sets
- Frequency counting patterns
- LRU Cache implementation
- Collision handling strategies
- **Skills**: Hashing techniques with real implementations
- **Problems**: 35+ hashing problems

### 7. 🎯 Greedy & Advanced Algorithms Agent
- Greedy algorithm strategy
- Backtracking patterns
- Bit manipulation tricks
- Mathematical algorithms
- **Skills**: Complete implementations for advanced techniques
- **Problems**: 40+ advanced problems

## 💡 Features

✅ **7 Expert Agents** - One for each DSA domain
✅ **8+ Invokable Skills** - Ready-to-use code implementations
✅ **4 Interactive Commands** - Solver, difficulty, interview, complexity
✅ **300+ Problems** - Easy, Medium, Hard levels
✅ **Complete Solutions** - Code examples in Python/JavaScript/Java/C++
✅ **Complexity Analysis** - Time and space breakdown for every solution
✅ **Interview Prep** - Top 20 questions with strategies
✅ **Progressive Learning** - Beginner → Intermediate → Advanced
✅ **Production-Ready** - Official Claude Code plugin format

## 📚 Learning Paths

### Beginner (0-2 weeks)
- Array fundamentals and two pointers
- Basic string manipulation
- Hash maps and sets
- Linked lists basics

### Intermediate (2-8 weeks)
- Trees and graph traversals
- Basic dynamic programming
- Sorting and searching
- Hash-based problems

### Advanced (8+ weeks)
- Hard DP problems
- Graph algorithms (Dijkstra, topological sort)
- Greedy strategies
- Bit manipulation tricks
- Interview-style problems

## 🛠️ Built-In Skills

### Array & Linked List
- **array-techniques**: Two pointers, sliding window, prefix sums

### Tree Algorithms
- **tree-traversal**: DFS, BFS, inorder, preorder, postorder

### Graph Algorithms
- **graph-algorithms**: DFS, BFS, Dijkstra, Union-Find, topological sort

### Dynamic Programming
- **dynamic-programming**: Memoization, tabulation, state design, DP templates

### Sorting & Searching
- **sorting-algorithms**: Merge sort, quick sort, binary search, complexity

### Hash-Based Techniques
- **hashing-techniques**: Frequency counting, LRU cache, duplicate detection

### Backtracking
- **backtracking-patterns**: Permutations, combinations, N-Queens, subsets

### Bit Manipulation
- **bit-manipulation**: Bit operations, XOR tricks, single number problems

## 📋 Commands Reference

### `/problem-solver`
Browse 300+ DSA problems organized by:
- Topic (arrays, trees, graphs, DP, sorting, hash, greedy)
- Difficulty (Easy, Medium, Hard)
- Complete with solutions and explanations

### `/difficulty-selector`
Choose your learning path based on:
- Current skill level (Beginner, Intermediate, Advanced)
- Time available (weeks to months)
- Learning goals
- Daily practice schedule

### `/interview-prep`
Master coding interviews with:
- Top 20 most frequently asked problems
- Interview day strategies
- Communication tips
- Preparation schedule
- Mock interview practice

### `/complexity-analyzer`
Understand time and space complexity:
- Big O notation guide
- Complexity comparisons for data structures
- Sorting algorithm complexity
- How to calculate and optimize

## 🔗 Related Resources

- **LeetCode**: https://leetcode.com
- **HackerRank**: https://www.hackerrank.com
- **GitHub**: https://github.com/pluginagentmarketplace/custom-plugin-data-structures-algorithms
- **License**: MIT

## 🤝 Contributing

Contributions welcome! Areas to enhance:
- More problem solutions
- Additional algorithm explanations
- Video walkthroughs
- Visualization tools
- More language implementations

## 📄 License

MIT License - See LICENSE file for details

## 🙌 Credits

Comprehensive DSA learning plugin built for Claude Code with best practices from:
- LeetCode community
- GeeksforGeeks
- Cracking the Coding Interview
- System Design Interview resources

---

**Ready to Master DSA?** 🚀

1. Use `/difficulty-selector` to pick your level
2. Use `/problem-solver` to find problems
3. Use `/complexity-analyzer` to understand optimization
4. Use `/interview-prep` to ace your interviews!

**Practice daily. Master DSA. Get hired.** 💪