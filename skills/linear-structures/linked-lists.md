---
name: linked-lists  
description: Master linked list operations. Reversal, cycle detection, merging. Practical implementations and common problems.
---

# Linked Lists

## Node Definition
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

## Common Operations

### Reversal: O(n)
```python
def reverse(head):
    prev = None
    while head:
        next_temp = head.next
        head.next = prev
        prev = head
        head = next_temp
    return prev
```

### Cycle Detection: O(n)
Floyd's algorithm - slow and fast pointers

### Merging: O(n)
Merge two sorted lists

## Key Insights
✓ Access: O(n)
✓ Insert/Delete at known position: O(1)
✓ Find: O(n)
✓ Reversal: O(n) time, O(1) space

## Problems
- Reverse linked list
- Detect cycle
- Merge sorted lists
- Nth node from end
