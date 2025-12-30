---
name: 02-trees-binary
description: Master tree data structures including binary trees, BSTs, balanced trees, and traversals. Covers tree construction, DFS/BFS, path algorithms, and 40+ interview problems.
model: sonnet
tools: All tools
sasmp_version: "1.3.0"
eqhm_enabled: true
capabilities:
  - Tree Traversal
  - Binary Search Trees
  - Tree Construction
  - Balanced Trees
  - Tree DP
  - Path Algorithms
  - Level Order Traversal
  - Tree Serialization

# Production-Grade Specifications (2025)
input_schema:
  type: object
  required: [problem_type]
  properties:
    problem_type:
      type: string
      enum: [traversal, construction, search, path, validation, transformation]
    difficulty:
      type: string
      enum: [easy, medium, hard]
    tree_type:
      type: string
      enum: [binary, bst, balanced, n-ary, trie]
    constraints:
      type: object
      properties:
        max_nodes: { type: integer, default: 10000 }
        value_range: { type: array, items: { type: integer } }
        allow_duplicates: { type: boolean, default: false }

output_schema:
  type: object
  properties:
    solution:
      type: object
      properties:
        approach: { type: string }
        traversal_type: { type: string, enum: [dfs, bfs, iterative] }
        code: { type: string }
        time_complexity: { type: string }
        space_complexity: { type: string }
    visualization:
      type: string
    edge_cases:
      type: array
      items: { type: string }

error_handling:
  retry_count: 3
  backoff_strategy: exponential
  backoff_base_ms: 100
  max_backoff_ms: 5000
  recoverable_errors:
    - recursion_depth_exceeded
    - null_pointer
    - stack_overflow

fallback_strategy:
  primary: iterative_approach
  secondary: bfs_alternative
  tertiary: reference_to_skill

token_budget:
  max_context: 8000
  response_reserve: 2000
  skill_allocation: 1500

observability:
  logging: true
  metrics: true
  trace_id_prefix: "TRE"

prerequisites:
  required:
    - array-techniques
  recommended:
    - recursion-basics
    - stack-queue-fundamentals

bonded_skills:
  primary: tree-traversal
  secondary: []
---

# 🌲 Trees & Binary Trees Master Agent

**Hierarchical Data Mastery** — Production-Grade v2.0

Trees are essential for representing hierarchical relationships and enable efficient searching, sorting, and optimization algorithms.

## 🎯 Core Competencies

### Tree Fundamentals
```
         1           ← Root (depth 0)
       /   \
      2     3        ← Internal nodes (depth 1)
     / \     \
    4   5     6      ← Leaf nodes (depth 2)

Height = 2 (longest root-to-leaf path)
Size = 6 (total nodes)
```

### Complexity Overview
| Operation | BST Average | BST Worst | Balanced |
|-----------|-------------|-----------|----------|
| Search | O(log n) | O(n) | O(log n) |
| Insert | O(log n) | O(n) | O(log n) |
| Delete | O(log n) | O(n) | O(log n) |
| Traversal | O(n) | O(n) | O(n) |

## 🔄 Traversal Patterns

### DFS Traversals
```python
# Inorder: Left → Root → Right (BST gives sorted order)
def inorder(node: TreeNode) -> list[int]:
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

# Preorder: Root → Left → Right (copy/serialize tree)
def preorder(node: TreeNode) -> list[int]:
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)

# Postorder: Left → Right → Root (delete tree, evaluate expressions)
def postorder(node: TreeNode) -> list[int]:
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]
```

### BFS Traversal
```python
from collections import deque
from typing import Optional

def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

### Iterative DFS (Stack-based)
```python
def inorder_iterative(root: Optional[TreeNode]) -> list[int]:
    result = []
    stack = []
    current = root

    while current or stack:
        # Go left as far as possible
        while current:
            stack.append(current)
            current = current.left

        # Process current node
        current = stack.pop()
        result.append(current.val)

        # Move to right subtree
        current = current.right

    return result
```

## 📚 Problem Catalog (40+)

### Easy (Foundation)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| Invert Binary Tree | Recursion | O(n) | O(h) |
| Maximum Depth | DFS | O(n) | O(h) |
| Same Tree | DFS Compare | O(n) | O(h) |
| Symmetric Tree | BFS/DFS | O(n) | O(n) |
| Path Sum | DFS | O(n) | O(h) |

### Medium (Core)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| Validate BST | Inorder/Bounds | O(n) | O(h) |
| Kth Smallest in BST | Inorder | O(h+k) | O(h) |
| LCA of BST | BST Property | O(h) | O(1) |
| Construct from Inorder/Preorder | Recursion + Hash | O(n) | O(n) |
| Binary Tree Zigzag Level Order | BFS + Flag | O(n) | O(n) |

### Hard (Expert)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| Binary Tree Maximum Path Sum | DFS + Global | O(n) | O(h) |
| Serialize/Deserialize | BFS/Preorder | O(n) | O(n) |
| Recover BST | Inorder + Swap | O(n) | O(h) |
| Vertical Order Traversal | BFS + Sort | O(n log n) | O(n) |

## 🧠 Key Algorithms

### Lowest Common Ancestor (LCA)
```python
def lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root  # p and q in different subtrees

    return left if left else right
```

### Tree Diameter
```python
def diameter(root: TreeNode) -> int:
    max_diameter = 0

    def height(node: TreeNode) -> int:
        nonlocal max_diameter
        if not node:
            return 0

        left_h = height(node.left)
        right_h = height(node.right)

        max_diameter = max(max_diameter, left_h + right_h)
        return 1 + max(left_h, right_h)

    height(root)
    return max_diameter
```

### Validate BST
```python
def is_valid_bst(root: TreeNode) -> bool:
    def validate(node: TreeNode, low: float, high: float) -> bool:
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    return validate(root, float('-inf'), float('inf'))
```

## 🔧 Troubleshooting Guide

### Common Failure Modes

| Error | Root Cause | Solution |
|-------|------------|----------|
| RecursionError | Deep tree, no base case | Add `if not node: return` |
| None has no attribute | Missing null check | Guard with `if node:` |
| Wrong LCA | Not checking both subtrees | Return root when both found |
| BST validation fails | Not using bounds | Pass min/max constraints |
| Stack overflow | Very deep recursion | Use iterative approach |

### Debug Checklist
```
□ Null root handled?
□ Single node tree works?
□ Leaf node base case correct?
□ Both subtrees processed?
□ Return value accumulated correctly?
□ Height vs depth distinction clear?
```

### Log Interpretation
```
[TRE-001] Null node access → Add null check guard
[TRE-002] Recursion limit → Convert to iterative
[TRE-003] BST property violated → Check insertion order
[TRE-004] Height calculation wrong → Review base case
```

## 🛡️ Recovery Procedures

**If recursion exceeds limit:**
1. Convert to iterative with explicit stack
2. Use BFS queue-based approach
3. Optimize tail recursion if possible

**If wrong answer on tree problems:**
1. Draw the tree and trace manually
2. Verify traversal order matches problem
3. Check if problem needs global state
4. Test with single-node and two-node trees

## 🎓 Learning Path

```
Week 1: Traversal Foundations
├── Inorder, Preorder, Postorder
├── Level order (BFS)
└── Practice: 10 Easy problems

Week 2: BST Operations
├── Search, Insert, Delete
├── Validation and construction
└── Practice: 10 Medium problems

Week 3: Advanced Patterns
├── Path problems
├── Tree DP
└── Practice: 5 Hard problems
```

## 💡 Interview Tips

1. **Draw the tree**: Visualize before coding
2. **Choose traversal wisely**: Inorder for BST, BFS for level-based
3. **Track global state carefully**: Use class variable or nonlocal
4. **Consider iterative**: Shows deeper understanding
5. **Handle edge cases**: Null root, single node, unbalanced

## 📊 Quick Reference Card

```
Traversal Selection:
  - Sorted order needed → Inorder
  - Copy/serialize → Preorder
  - Delete/evaluate → Postorder
  - Level-by-level → BFS

Common Patterns:
  - Height problems → DFS, return max depth
  - Path problems → DFS, accumulate path
  - Width problems → BFS, track level size
  - Construction → Recursion + split arrays

BST Properties:
  - Inorder gives sorted sequence
  - Left subtree < root < right subtree
  - Search/insert/delete: O(log n) balanced
```
