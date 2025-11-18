---
name: tree-structures-skill
description: Tree fundamentals, traversals (in/pre/post-order, BFS), BST operations, balancing concepts, heaps, and specialized trees (tries, segment trees). Complete tree problem-solving guide.
---

# Tree Structures Skill

## Quick Start

**Tree Types & Use:**
- **Binary Tree**: General hierarchical structure
- **BST**: Sorted data, fast search O(log n)
- **AVL/RB Tree**: Guaranteed O(log n) operations
- **Heap**: Priority queue, min/max extraction
- **Trie**: Prefix matching, auto-complete
- **Segment Tree**: Range queries and updates

## Binary Tree Basics

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Build tree from list
def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root
```

## Tree Traversals

### In-Order (Left → Root → Right)
```python
def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)
    # For BST: gives sorted sequence

def inorder_iterative(root):
    result = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result
```

### Pre-Order (Root → Left → Right)
```python
def preorder(node):
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)
    # Useful for copying tree, serialization

def preorder_iterative(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
```

### Post-Order (Left → Right → Root)
```python
def postorder(node):
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]
    # Useful for deletion, calculating heights

def postorder_iterative(root):
    if not root:
        return []
    result = []
    stack = [root]
    last_visited = None
    while stack:
        current = stack[-1]
        if current.left and last_visited != current.left:
            stack.append(current.left)
        elif current.right and last_visited != current.right:
            stack.append(current.right)
        else:
            result.append(current.val)
            last_visited = stack.pop()
    return result
```

### Level-Order (BFS)
```python
def level_order(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

## Binary Search Tree (BST)

```python
class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left:
                self._insert_recursive(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert_recursive(node.right, val)
            else:
                node.right = TreeNode(val)
        # O(log n) average, O(n) worst case

    def search(self, val):
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
        # O(log n) average, O(n) worst case

    def delete(self, val):
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(self, node, val):
        if not node:
            return None

        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            # Node to delete found
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Two children: find inorder successor
            successor = self._find_min(node.right)
            node.val = successor.val
            node.right = self._delete_recursive(node.right, successor.val)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
```

## Heaps (Priority Queue)

```python
import heapq

# Min-heap (default)
min_heap = [3, 1, 4, 1, 5, 9]
heapq.heapify(min_heap)  # O(n)
heapq.heappush(min_heap, 2)  # O(log n)
smallest = heapq.heappop(min_heap)  # O(log n)

# Max-heap (negate values)
max_heap = [-x for x in [3, 1, 4, 1, 5, 9]]
heapq.heapify(max_heap)
heapq.heappush(max_heap, -10)
largest = -heapq.heappop(max_heap)

# Heap sort
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]
```

**Use Cases:**
- Priority queues
- Kth largest element
- Median of streaming data
- Load balancing
- Dijkstra's algorithm

## Tries (Prefix Trees)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        # O(m) where m = word length

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end
        # O(m)

    def starts_with(self, prefix):
        return self._find_node(prefix) is not None
        # O(m)

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def get_all_with_prefix(self, prefix):
        node = self._find_node(prefix)
        if not node:
            return []
        results = []
        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, current, results):
        if node.is_end:
            results.append(current)
        for char, child in node.children.items():
            self._dfs(child, current + char, results)
```

## Tree Metrics

```python
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

def is_balanced(node):
    if not node:
        return True
    left_h = height(node.left)
    right_h = height(node.right)
    return abs(left_h - right_h) <= 1 and \
           is_balanced(node.left) and \
           is_balanced(node.right)

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def sum_nodes(node):
    if not node:
        return 0
    return node.val + sum_nodes(node.left) + sum_nodes(node.right)
```

## Classic Tree Problems

**Easy (10+ problems):**
1. Maximum depth
2. Symmetric tree
3. Path sum
4. Invert tree
5. Lowest common ancestor

**Medium (15+ problems):**
6. Binary tree level order traversal
7. Zigzag level order traversal
8. Vertical order traversal
9. Validate BST
10. Serialize/deserialize

**Hard (10+ problems):**
11. Binary tree maximum path sum
12. Recover BST
13. Hardest binary tree serialization
14. Tree diameter
15. Range sum query (Segment Tree)

## Key Concepts

✅ **In-order of BST is sorted**: Use for sorted iteration
✅ **Heights matter in AVL/RB**: Guarantees O(log n)
✅ **Heaps are almost complete**: Fit perfectly in arrays
✅ **Tries for prefixes**: O(m) not O(n)
✅ **Recursion is natural**: Most tree problems recursive

---

**Trees are everywhere in CS - master them and master algorithms!**
