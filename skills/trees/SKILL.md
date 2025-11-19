---
name: tree-traversal
description: Master tree traversal techniques including DFS (inorder, preorder, postorder) and BFS level-order traversal with complete code examples.
---

# Tree Traversal Skill

## DFS - Inorder (Left, Root, Right)
```python
def inorder(root, result=[]):
    if not root:
        return
    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)
    return result

# Iterative with stack
def inorderIterative(root):
    result, stack = [], []
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

## DFS - Preorder (Root, Left, Right)
```python
def preorder(root):
    if not root:
        return []
    result = [root.val]
    result.extend(preorder(root.left))
    result.extend(preorder(root.right))
    return result
```

## BFS - Level Order Traversal
```python
from collections import deque

def levelOrder(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result
```

## Binary Search Tree Validation
```python
def isValidBST(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return (isValidBST(root.left, min_val, root.val) and
            isValidBST(root.right, root.val, max_val))
```