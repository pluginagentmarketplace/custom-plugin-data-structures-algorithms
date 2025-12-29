#!/usr/bin/env python3
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def height(root):
    return 1 + max(height(root.left), height(root.right)) if root else 0
