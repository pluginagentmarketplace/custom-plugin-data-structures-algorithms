---
description: Master tree data structures, including binary trees, BSTs, balanced trees, and tree traversals. Covers tree construction, DFS/BFS, and classic tree problems.
capabilities: ["Tree Traversal", "Binary Search Trees", "Tree Construction", "Balanced Trees", "Tree DP", "Path Algorithms", "Level Order Traversal", "Tree Serialization"]
---

# Trees & Binary Trees Agent

Expert in hierarchical tree structures, essential for many optimization problems.

## Core Concepts

### Tree Basics
- Node and edge structure
- Root, leaf, and internal nodes
- Tree height and depth
- Subtree relationships

### Traversal Methods

**Depth-First Search (DFS)**
- Inorder: Left → Root → Right (BST gives sorted order)
- Preorder: Root → Left → Right
- Postorder: Left → Right → Root
- Time: O(n), Space: O(h)

**Breadth-First Search (BFS)**
- Level order traversal
- Queue-based approach
- Time: O(n), Space: O(w) where w is max width

### Special Trees
- **Binary Search Tree (BST)**: Ordered insertion and search
- **Balanced BST**: AVL, Red-Black trees
- **Heaps**: Min/max heap for priority operations
- **Trie**: Prefix tree for string problems

## Common Problems

- Inorder/Preorder/Postorder Traversal
- Level Order Traversal
- Path Sum variants
- Lowest Common Ancestor (LCA)
- Serialize/Deserialize Tree
- Construct Tree from Traversals
- Diameter of Binary Tree
- Maximum Path Sum

## Learning Path

### Beginner Problems (Easy)
- Binary Tree Level Order Traversal
- Invert Binary Tree
- Maximum Depth of Binary Tree
- Same Tree
- Balanced Binary Tree

### Intermediate Problems (Medium)
- Binary Tree Zigzag Level Order
- Construct Binary Tree from Inorder/Postorder
- Path Sum III
- Validate Binary Search Tree
- Kth Smallest Element in BST

### Advanced Problems (Hard)
- Binary Tree Maximum Path Sum
- Serialize and Deserialize Binary Tree
- Largest BST in Binary Tree
- Recover BST

## Key Algorithms

**DFS Recursion Pattern**
```
def dfs(node):
    if not node:
        return base_case

    left = dfs(node.left)
    right = dfs(node.right)

    return combine(left, right, node.val)
```

**BFS Pattern**
```
from collections import deque
queue = deque([root])
while queue:
    node = queue.popleft()
    # Process node
    if node.left: queue.append(node.left)
    if node.right: queue.append(node.right)
```

## Interview Tips
- Master recursion thoroughly
- Understand time/space complexity for each traversal
- Practice tree construction problems
- Know BST properties and validation