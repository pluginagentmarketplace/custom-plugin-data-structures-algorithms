---
name: nonlinear-structures
description: Work with hierarchical and connected data structures including binary trees, balanced trees, heaps, and graphs. Use for tree problems, priority queues, and hierarchical data organization.
---

# Non-Linear Data Structures

## Quick Start

Trees and heaps are perfect for hierarchical relationships. Master their operations for interview success.

### Structure Selector

| Structure | Search | Insert | Delete | Min/Max | Use When |
|-----------|--------|--------|--------|---------|----------|
| Binary Tree | O(n) | O(1) | O(1) | O(n) | General hierarchy |
| BST | O(log n) avg | O(log n) avg | O(log n) avg | O(log n) | Sorted access needed |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) | Balanced required |
| Heap | O(n) | O(log n) | O(log n) | O(1) | Priority queue |
| Trie | O(m) | O(m) | O(m) | - | String patterns |

## Binary Trees

### Node Definition
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### Tree Traversals

#### In-Order (Left → Node → Right)
```python
def inorder(node, result=[]):
    """For BST, gives sorted sequence"""
    if node:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)
    return result
```

#### Pre-Order (Node → Left → Right)
```python
def preorder(node, result=[]):
    """Useful for tree copying"""
    if node:
        result.append(node.value)
        preorder(node.left, result)
        preorder(node.right, result)
    return result
```

#### Post-Order (Left → Right → Node)
```python
def postorder(node, result=[]):
    """Useful for deletion"""
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.value)
    return result
```

#### Level-Order (BFS)
```python
from collections import deque

def levelorder(root):
    """Breadth-first traversal"""
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)
    return result
```

## Binary Search Trees

### BST Properties
- Left subtree < Node < Right subtree
- In-order traversal gives sorted sequence
- Average: O(log n), Worst: O(n) (unbalanced)

### Search in BST
```python
def search_bst(node, value):
    """O(log n) average, O(n) worst"""
    if not node:
        return None
    if node.value == value:
        return node
    elif value < node.value:
        return search_bst(node.left, value)
    else:
        return search_bst(node.right, value)
```

### Insert into BST
```python
def insert_bst(node, value):
    """O(log n) average"""
    if not node:
        return TreeNode(value)
    if value < node.value:
        node.left = insert_bst(node.left, value)
    else:
        node.right = insert_bst(node.right, value)
    return node
```

### Validate BST
```python
def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    """Check if tree satisfies BST property"""
    if not node:
        return True
    if node.value <= min_val or node.value >= max_val:
        return False
    return (is_valid_bst(node.left, min_val, node.value) and
            is_valid_bst(node.right, node.value, max_val))
```

## Heaps

### Heap Properties
- **Max Heap**: Parent ≥ Children
- **Min Heap**: Parent ≤ Children
- **Complete Binary Tree**: All levels filled except possibly last
- **Array Representation**:
  - Parent at i: children at 2i+1, 2i+2
  - Child at i: parent at (i-1)//2

### Heap Operations
```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, index):
        """Move element up after insertion"""
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        """Move element down after deletion"""
        size = len(self.heap)
        while 2 * index + 1 < size:
            smaller = 2 * index + 1
            if 2 * index + 2 < size and self.heap[2 * index + 2] < self.heap[smaller]:
                smaller = 2 * index + 2
            if self.heap[index] > self.heap[smaller]:
                self.heap[index], self.heap[smaller] = self.heap[smaller], self.heap[index]
                index = smaller
            else:
                break

    def insert(self, value):
        """Insert: O(log n)"""
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """Extract minimum: O(log n)"""
        if not self.heap:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self.heapify_down(0)
        return min_val
```

### Priority Queue
```python
import heapq

# Min heap (default)
pq = []
heapq.heappush(pq, 5)
heapq.heappush(pq, 3)
min_val = heapq.heappop(pq)  # Returns 3

# For max heap, negate values
heapq.heappush(pq, -5)
heapq.heappush(pq, -3)
max_val = -heapq.heappop(pq)  # Returns 5
```

## Tries (Prefix Trees)

### Trie Node
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert word: O(m) where m = word length"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """Search exact word: O(m)"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        """Find words with prefix: O(m)"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

## Common Problems

1. **Lowest Common Ancestor (LCA)**
2. **Diameter of Tree** - longest path between any two nodes
3. **Balanced Tree Check**
4. **Path Sum** - find path with target sum
5. **Serialize/Deserialize Tree**
6. **Kth Smallest in BST**
7. **Top K Frequent Elements** - using heap

## Tree Complexity Summary

| Operation | Binary Tree | Balanced BST | Heap |
|-----------|------------|--------------|------|
| Search | O(n) | O(log n) | O(n) |
| Insert | O(1) | O(log n) | O(log n) |
| Delete | O(n) | O(log n) | O(log n) |
| Min/Max | O(n) | O(log n) | O(1)/O(n) |

## Key Takeaways

✓ Tree traversals: in-order, pre-order, post-order, level-order
✓ BST for sorted search and access
✓ Heaps for priority queue operations
✓ Tries for prefix-based searching
✓ Balanced trees guarantee O(log n) operations
✓ Array representation efficient for heaps
