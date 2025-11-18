---
description: Comprehensive guide to trees: binary trees, BST, AVL, heaps, tries, segment trees. Master tree traversals, balancing, and specialized tree problems.
capabilities: ["binary-trees", "bst", "avl-trees", "heaps", "tries", "segment-trees", "tree-traversal", "tree-problems"]
---

# Tree Structures Master

Trees are the **most important non-linear data structure**. From simple binary trees to specialized structures like segment trees, mastering trees unlocks solutions to countless real-world problems.

## Tree Family Overview

### 1. Binary Search Trees (BST)
- **Search/Insert/Delete**: O(log n) average, O(n) worst
- **Properties**: Left < Root < Right
- **Use Cases**: Sorted data, range queries, auto-complete
- **Real World**: Database indexes, file systems, expression parsing

### 2. AVL Trees (Self-Balancing BST)
- **Guaranteed O(log n)**: Always maintains balance
- **Rotation Cost**: O(log n) operations for rotations
- **Use Cases**: High-performance search applications
- **Real World**: Window managers, database engines

### 3. Red-Black Trees
- **Guaranteed O(log n)**: Simpler balancing than AVL
- **Faster insertions**: Fewer rotations than AVL
- **Use Cases**: Java TreeMap, C++ STL containers
- **Real World**: Linux kernel scheduler, databases

### 4. Heaps (Min/Max)
- **Insert/Delete**: O(log n)
- **Find Min/Max**: O(1)
- **Properties**: Complete binary tree, heap property
- **Use Cases**: Priority queues, sorting (heapsort), median finding
- **Real World**: Operating systems schedulers, Dijkstra's algorithm

### 5. Tries (Prefix Trees)
- **Search/Insert**: O(m) where m = word length
- **Memory**: O(alphabet_size * length)
- **Use Cases**: Auto-complete, spell-checking, IP routing
- **Real World**: Search engine prefixes, DNS systems

### 6. Segment Trees
- **Range Query/Update**: O(log n)
- **Construction**: O(n)
- **Use Cases**: Range sum/min/max, lazy propagation
- **Real World**: Graphics rendering, database query optimization

## Tree Traversal Algorithms

### Depth-First Traversals
```python
# In-order (Left -> Root -> Right)
# Gives sorted sequence in BST
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

# Pre-order (Root -> Left -> Right)
# Useful for copying tree
def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

# Post-order (Left -> Right -> Root)
# Useful for deletion, height calculation
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)

# Level-order (BFS)
# Breadth-first level by level
def levelorder(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

## Balancing & Rotations (AVL Example)

```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def rotate_right(z):
    y = z.left
    z.left = y.right
    y.right = z
    z.height = max(get_height(z.left), get_height(z.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    return y

def rotate_left(z):
    y = z.right
    z.right = y.left
    y.left = z
    z.height = max(get_height(z.left), get_height(z.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    return y
```

## Common Tree Problems by Category

### Basic Tree Problems (15+ problems)
1. Maximum depth / height
2. Symmetric tree check
3. Path sum validation
4. Tree inversion (mirror)
5. Lowest common ancestor

### BST Problems (20+ problems)
6. Validate BST
7. Kth smallest element
8. Convert sorted array to BST
9. Recover BST (two nodes swapped)
10. BST iterator

### Heap Problems (15+ problems)
11. Kth largest element
12. Median of running stream
13. Reorganize string (character frequency)
14. Sliding window maximum
15. Connect sticks (minimum cost)

### Advanced Tree Problems (20+ problems)
16. Serialize/deserialize tree
17. Vertical order traversal
18. Maximum path sum
19. Word search in Trie
20. Range sum query (Segment Tree)

## Learning Progression

### Level 1: Basics (Days 1-5)
- [ ] Binary tree traversals (all 4 methods)
- [ ] Tree structure basics
- [ ] Simple tree problems (height, balance check)
- [ ] BFS and DFS implementations

### Level 2: BST & Heaps (Days 6-11)
- [ ] BST operations (search, insert, delete)
- [ ] Heap operations and priority queue
- [ ] AVL tree basics (rotation concepts)
- [ ] Heap-based problems (25+ problems)

### Level 3: Advanced (Days 12-18)
- [ ] Tree serialization
- [ ] Segment trees and range queries
- [ ] Tries and advanced applications
- [ ] Complex tree path problems

## Key Insights

### Height vs Depth
- **Height**: Nodes below (root's height = tree height)
- **Depth**: Nodes above (root's depth = 0)

### Balanced Tree Benefits
```
Unbalanced (worst case)    Balanced (best case)
        1                         4
         \                       / \
          2                      2   6
           \                    / \ / \
            3                  1  3 5  7
             \
              4
O(n) access               O(log n) access
```

### Why Heaps Use Arrays
- Complete binary trees map perfectly to arrays
- Index relationships: parent=i//2, left=2i, right=2i+1
- No pointer overhead, better cache locality

## Real-World Applications

| Structure | Real Use |
|-----------|----------|
| BST | Database indexes |
| AVL/RB | Java TreeMap, Linux kernel |
| Heap | OS scheduler, priority tasks |
| Trie | Search suggestions, spell check |
| Segment Tree | Range queries, data compression |

## Next Steps

1. Implement all tree structures from scratch
2. Solve 70+ tree problems (LeetCode, CodeForces)
3. Master tree traversal patterns
4. Practice recursive thinking
5. Move to graphs (which are generalized trees)

---

**Interview Tip**: "Trees are everywhere in CS. Understand them deeply because graphs are just generalized trees, and many system designs use trees at their core."
