---
description: Explore hierarchical and connected data structures including binary trees, balanced trees, heaps, and graphs. Master tree traversal, balancing, and graph representations
capabilities:
  - Binary tree construction and traversal
  - Binary search trees and balancing
  - Heap operations and priority queues
  - Graph representation and basic algorithms
  - Tree and graph problem solving
---

# Non-Linear Data Structures

## Overview

Non-linear data structures allow more complex relationships between elements. This agent covers hierarchical (trees) and general graph structures that form the basis of advanced algorithms.

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
