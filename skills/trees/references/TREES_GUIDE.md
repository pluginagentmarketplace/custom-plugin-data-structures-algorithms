# Trees Guide

## Binary Tree Traversals
```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
```

## BST Operations
- **Search**: Compare, go left/right
- **Insert**: Find null, insert
- **Delete**: 3 cases (leaf, one child, two children)
