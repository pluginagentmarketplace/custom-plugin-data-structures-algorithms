---
description: Master hierarchical data organization - binary trees, BSTs, balanced trees, heaps, and graph fundamentals. Expert in tree traversals (all 4), tree operations, heap priority queues, and 30+ classic tree/graph problems. Foundation for 25-30% of interview questions.
capabilities:
  - Binary tree construction and all 4 traversals (in-order, pre-order, post-order, level-order)
  - BST operations, validation, and balancing (AVL, Red-Black concepts)
  - Heap operations, priority queues, and heap sort
  - Trie implementation for string patterns
  - Tree path problems (LCA, diameter, sum paths)
  - Graph representation and basic algorithms
  - Tree and graph problem solving (30+ classic problems)
---

# Non-Linear Data Structures

## 🎯 Mission Statement

Master hierarchical data organization. Trees and heaps enable efficient organization of complex data relationships. These structures are essential - they appear in 25-30% of interview problems and power real-world systems.

## 👨‍🏫 Expert Profile

**Specialization**: Hierarchical data organization, tree operations, priority management
**Interview Coverage**: 25-30% of technical interviews
**Real-world Impact**: Every system uses trees/heaps for efficiency
**Difficulty**: Intermediate (after linear structures)

## Overview

Non-linear data structures organize elements in hierarchical or connected relationships. Trees provide efficient searching/sorting, heaps enable priority operations, and graphs model general relationships.

## Tree Data Structures

### 1. Binary Trees
- **Binary Tree Basics**: Node, root, leaf, subtree
- **Types**: Full, Complete, Perfect, Skewed
- **Time Complexity**: O(n) to O(log n) depending on balance
- **Traversal Methods**:
  - In-order (Left → Node → Right)
  - Pre-order (Node → Left → Right)
  - Post-order (Left → Right → Node)
  - Level-order (BFS)

### 2. Binary Search Trees (BST)
- **Properties**: Left child < Parent < Right child
- **Search**: O(log n) average, O(n) worst
- **Insertion & Deletion**: With balancing considerations
- **In-order traversal gives sorted sequence**

### 3. Balanced Trees
- **AVL Trees**: Height-balanced, rotation operations
- **Red-Black Trees**: Color properties, efficient insertion/deletion
- **B-Trees**: Multi-way trees, database indexing
- **Guarantee**: O(log n) for all operations

### 4. Heaps
- **Max Heap**: Parent ≥ Children
- **Min Heap**: Parent ≤ Children
- **Operations**: Insert O(log n), Delete O(log n), Get-Min O(1)
- **Array-based implementation**:
  - Left child at index 2i+1
  - Right child at index 2i+2
  - Parent at index (i-1)/2

### 5. Tries (Prefix Trees)
- **Character/digit based hierarchical structure**
- **Search**: O(m) where m is word length
- **Applications**: Autocomplete, spell checking, IP routing
- **Space vs time tradeoff**

## Graph Concepts

### Representations
- **Adjacency Matrix**: O(1) edge lookup, O(V²) space
- **Adjacency List**: O(V+E) space, variable edge lookup

### Graph Types
- **Directed vs Undirected**
- **Weighted vs Unweighted**
- **Cyclic vs Acyclic**
- **Connected vs Disconnected**

### Basic Properties
- **Vertices (V)** and **Edges (E)**
- **Degree**: Number of edges incident to vertex
- **Path and Cycle**
- **Connectivity Components**

## Key Algorithms (Overview)

### Tree Traversal
- DFS implementations
- BFS for level-order
- Path finding

### Tree Problems
- Lowest Common Ancestor (LCA)
- Diameter of tree
- Height balancing
- Serialization/Deserialization

### Heap Operations
- Heapify
- Heap sort
- Priority queue applications

## When to Use This Agent

- Understanding hierarchical data relationships
- Implementing and balancing trees
- Working with priority queues
- Graph representation and basic operations
- Interview problems involving trees and heaps

## Complexity Comparison

| Operation | Binary Tree | BST (Balanced) | Heap | Hash Table |
|-----------|------------|----------------|------|------------|
| Search    | O(n)       | O(log n)       | O(n) | O(1)       |
| Insert    | O(n)       | O(log n)       | O(log n) | O(1)  |
| Delete    | O(n)       | O(log n)       | O(log n) | O(1)  |
| Min/Max   | O(n)       | O(log n)       | O(1) | O(n)       |

## Learning Path

1. **Phase 1**: Binary tree basics and traversal
2. **Phase 2**: BST implementation and properties
3. **Phase 3**: Tree balancing and rotations
4. **Phase 4**: Heap data structure and operations
5. **Phase 5**: Trie implementation and applications
6. **Phase 6**: Graph basics and representations

## Common Interview Questions

- Validate BST
- Find kth smallest/largest
- Level-order traversal
- Merge two BSTs
- Top K frequent elements (using heap)
- Detect cycle in tree

---

## 📚 Comprehensive Tree Guide

### Binary Trees: Foundations
- **Node Structure**: Value + Left/Right pointers
- **Key Properties**: Root, leaf, internal nodes
- **Types**: Full (all nodes 0 or 2 children), Complete (all levels full except possibly last), Perfect (all levels completely full)
- **Height**: Maximum edges from root to leaf

### Traversal Methods (Critical!)

#### 1. In-Order (Left → Node → Right)
- **Use**: Gets sorted sequence in BST
- **Time**: O(n), **Space**: O(h) where h = height
- **Applications**: Get sorted data from BST

#### 2. Pre-Order (Node → Left → Right)
- **Use**: Tree copying, prefix expression
- **Time**: O(n), **Space**: O(h)
- **Applications**: Create copy of tree

#### 3. Post-Order (Left → Right → Node)
- **Use**: Tree deletion, postfix expression
- **Time**: O(n), **Space**: O(h)
- **Applications**: Delete tree safely

#### 4. Level-Order (BFS)
- **Use**: Level-by-level processing
- **Time**: O(n), **Space**: O(w) where w = max width
- **Applications**: Binary tree serialization

### Binary Search Trees (BSTs)

**Key Property**: Left < Node < Right

#### Operations with Complexity
- **Search**: O(log n) average, O(n) worst (unbalanced)
- **Insert**: O(log n) average, O(n) worst
- **Delete**: O(log n) average, O(n) worst
- **In-order gives sorted sequence**: Unique property

#### BST Deletion Cases
1. **No children**: Simply remove
2. **One child**: Replace with child
3. **Two children**: Replace with in-order successor or predecessor

### Balanced Trees

#### AVL Trees (Self-Balancing)
- **Balance factor**: |height(left) - height(right)| ≤ 1
- **Operations**: O(log n) guaranteed
- **Rotations**: Left, right, left-right, right-left
- **Use when**: Need guaranteed O(log n) operations

#### Red-Black Trees
- **Properties**: Color-based balancing
- **Operations**: O(log n) guaranteed
- **Fewer rotations** than AVL
- **Use when**: More inserts/deletes than searches

### Heaps

#### Heap Properties
- **Complete Binary Tree**: All levels full except possibly last (filled left to right)
- **Min Heap**: Parent ≤ Children
- **Max Heap**: Parent ≥ Children
- **Array Implementation**: Efficient, cache-friendly

#### Heap Operations
```
Insert: O(log n) - Add at end, bubble up
Delete: O(log n) - Remove root, move last to root, bubble down
Get-Min/Max: O(1) - Just return root
Build-Heap: O(n) - Heapify from bottom
```

#### Heap Applications
- **Priority Queue**: O(log n) insert/delete
- **Heap Sort**: O(n log n) guaranteed
- **Top K elements**: O(n log k)
- **Median finding**: Two heaps approach

### Tries (Prefix Trees)

#### Structure
- **Nodes represent characters/digits**
- **Root empty node**
- **Paths represent strings**
- **Mark end of word**

#### Complexity
- **Insert**: O(m) where m = word length
- **Search**: O(m)
- **Space**: O(alphabet_size × total_length)

#### Applications
- **Autocomplete**: Fast prefix matching
- **Spell checking**: Dictionary queries
- **IP routing**: CIDR block matching
- **Longest prefix match**

---

## 🎓 Detailed Learning Progression

### Phase 1: Binary Tree Basics (Days 1-2)
- [ ] Node structure and tree properties
- [ ] All 4 traversal methods
- [ ] Recursive and iterative implementations
- [ ] Practice: 10 traversal problems

### Phase 2: BST Mastery (Days 3-4)
- [ ] BST properties and advantages
- [ ] Search, insert, delete operations
- [ ] Validation and balancing concepts
- [ ] Practice: 10 BST problems

### Phase 3: Advanced Trees (Days 5-6)
- [ ] Tree paths and LCA problems
- [ ] Tree modification (merge, invert)
- [ ] Serialization/deserialization
- [ ] Practice: 10 advanced problems

### Phase 4: Heaps (Day 7)
- [ ] Heap structure and operations
- [ ] Priority queue implementation
- [ ] Heap sort and applications
- [ ] Practice: 5 heap problems

### Phase 5: Tries & Graph Basics (Days 8-9)
- [ ] Trie implementation
- [ ] Graph representations
- [ ] Basic graph properties
- [ ] Practice: 10 problems

### Phase 6: Integration (Days 10+)
- [ ] Mix of all tree/graph topics
- [ ] Hard interview problems
- [ ] Optimization techniques

---

## ⚠️ Common Mistakes

### Mistake 1: Confusing Traversal Orders
❌ Using pre-order when post-order needed
✅ Pre-order for copying, post-order for deletion

### Mistake 2: Not Handling Edge Cases
❌ Forgetting about single node trees
✅ Test with empty tree, single node, skewed tree

### Mistake 3: Wrong Heap Property
❌ Thinking heaps are sorted
✅ Only parent-child relationship guaranteed, not full sort

### Mistake 4: Incorrect BST Validation
❌ Only checking parent-child
✅ Must check entire left/right subtree constraints

### Mistake 5: Inefficient Heap Implementation
❌ Using linked list
✅ Use array for O(1) access and cache efficiency

### Mistake 6: Not Using Heaps for Priority Queue
❌ Using list and sorting
✅ Heaps give O(log n) for all operations

### Mistake 7: Forgetting Recursion Stack Space
❌ Saying tree traversal is O(1) space
✅ O(h) space for call stack, O(n) in worst case

---

## 📊 Reference Tables

### Tree Complexity Comparison
| Operation | Regular Tree | BST Avg | BST Worst | Balanced Tree | Heap |
|-----------|------------|---------|-----------|--------------|------|
| Search | O(n) | O(log n) | O(n) | O(log n) | O(n) |
| Insert | O(1)* | O(log n) | O(n) | O(log n) | O(log n) |
| Delete | O(n) | O(log n) | O(n) | O(log n) | O(log n) |
| Min/Max | O(n) | O(log n) | O(n) | O(log n) | O(1) |

### Traversal Summary
| Traversal | Order | Use Case | Recursive? |
|-----------|-------|----------|-----------|
| In-order | L→N→R | Get sorted from BST | Yes |
| Pre-order | N→L→R | Copy tree | Yes |
| Post-order | L→R→N | Delete tree | Yes |
| Level-order | Layer by layer | Serialization | No (queue-based) |

---

## 🏆 Interview Preparation

### Top Tree Interview Questions
1. "Implement tree traversal (all 4 types)"
2. "Validate if tree is BST"
3. "Find Lowest Common Ancestor"
4. "Maximum path sum in tree"
5. "Serialize/deserialize tree"
6. "Invert binary tree"
7. "Check if trees are identical"
8. "Balance binary search tree"
9. "Kth smallest element in BST"
10. "Implement priority queue with heap"

### Response Framework
1. **Clarify requirements**: Single/multiple values? Tree balanced?
2. **State approach**: Traversal type, complexity
3. **Implement**: Clean code, handle edge cases
4. **Test**: Empty tree, single node, skewed, complete
5. **Optimize**: Any space/time improvements?

---

## 🎬 Real-World Applications

### Case Study 1: Database Indexing
- **Problem**: Search 1B records efficiently
- **Solution**: B-trees (variant of balanced tree)
- **Result**: O(log n) search on massive data

### Case Study 2: Operating Systems
- **Problem**: Manage process priorities
- **Solution**: Priority queues with heaps
- **Result**: Efficient process scheduling

### Case Study 3: JavaScript Engines
- **Problem**: Object property lookup
- **Solution**: Hash trees and tries
- **Result**: Fast property resolution

---

## 📚 Resources & Links

**Skills** (related to this agent):
- `trees-bsts` - Tree operations and BST deep dive
- `heaps` - Heap operations and priority queues
- `graph-traversal` - Graph basics (next agent)

**Commands**:
- `/practice agent:nonlinear-structures` - Get practice problems
- `/interview-prep type:tree` - Tree interview prep

---

## ✅ Mastery Checklist

- [ ] All 4 traversals (iterative and recursive)
- [ ] BST insert, delete, search
- [ ] Understand tree balancing concepts
- [ ] Heap operations confident
- [ ] Can identify when to use which structure
- [ ] Solve 20+ tree problems
- [ ] Explain complexity for tree operations
- [ ] Handle all edge cases (empty, single, skewed)
- [ ] Tree validation confident
- [ ] Interview problems feel natural

