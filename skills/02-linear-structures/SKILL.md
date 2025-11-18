---
name: linear-data-structures-skill
description: Master arrays, linked lists, stacks, queues, and deques. Understand insertion/deletion patterns, memory layouts, and when to use each structure for optimal performance.
---

# Linear Data Structures Skill

## Quick Start

**Choose your structure:**
- **Array**: Need fast random access → O(1) index
- **Linked List**: Frequent insertions/deletions at known position → O(1)
- **Stack**: LIFO behavior, DFS, backtracking
- **Queue**: FIFO behavior, BFS, scheduling
- **Deque**: Need both ends → double-ended queue

## Arrays

```python
# Fixed size
arr = [1, 2, 3, 4, 5]
arr[0]        # O(1) access
arr.append(6) # O(1) amortized

# 2D Array
matrix = [[1, 2], [3, 4]]
matrix[0][1]  # O(1) access
```

**Pros:**
- O(1) random access
- Cache-friendly (contiguous memory)
- Simple and intuitive

**Cons:**
- O(n) insertion/deletion (except at end)
- Fixed size (in traditional arrays)
- Wasted space for sparse data

## Linked Lists

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return self  # O(1)

    def delete_at_head(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val  # O(1)

    def find(self, val):
        current = self.head
        while current:
            if current.val == val:
                return current
            current = current.next
        return None  # O(n)

    def __len__(self):
        return self.size
```

**Pros:**
- O(1) insertion/deletion at known position
- Dynamic size
- No wasted space

**Cons:**
- O(n) access (must traverse)
- Extra memory for pointers
- Cache-unfriendly (scattered memory)

## Stacks (LIFO)

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)  # O(1) amortized

    def pop(self):
        return self.items.pop() if self.items else None  # O(1)

    def peek(self):
        return self.items[-1] if self.items else None  # O(1)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

**Use Cases:**
- Function call stack
- Expression evaluation (parentheses matching)
- DFS traversal
- Undo/Redo functionality
- Browser back button
- Backtracking problems

**Example: Valid Parentheses**
```python
def is_valid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False
    return not stack
```

## Queues (FIFO)

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, x):
        self.items.append(x)  # O(1)

    def dequeue(self):
        return self.items.popleft() if self.items else None  # O(1)

    def peek(self):
        return self.items[0] if self.items else None  # O(1)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

**Use Cases:**
- BFS traversal
- Task scheduling
- Print queue
- Message passing
- Level-order tree traversal
- Resource sharing

**Example: BFS Level-Order**
```python
def level_order(root):
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

## Deques (Double-Ended Queue)

```python
from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def add_front(self, x):
        self.items.appendleft(x)  # O(1)

    def add_back(self, x):
        self.items.append(x)  # O(1)

    def remove_front(self):
        return self.items.popleft() if self.items else None  # O(1)

    def remove_back(self):
        return self.items.pop() if self.items else None  # O(1)

    def get_front(self):
        return self.items[0] if self.items else None  # O(1)

    def get_back(self):
        return self.items[-1] if self.items else None  # O(1)
```

**Use Cases:**
- Sliding window (max in every window)
- Palindrome checking
- Task scheduling with priority
- Cache implementation (LRU)

**Example: Sliding Window Maximum**
```python
def max_sliding_window(nums, k):
    deq = deque()
    result = []

    for i in range(len(nums)):
        # Remove elements outside current window
        while deq and deq[0][1] < i - k + 1:
            deq.popleft()

        # Remove elements smaller than current
        while deq and deq[-1][0] < nums[i]:
            deq.pop()

        deq.append((nums[i], i))
        result.append(deq[0][0])

    return result[k-1:]  # O(n)
```

## Two-Pointer Technique

```python
# Reverse array
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    # O(n) time, O(1) space

# Find pair with target sum
def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
    # O(n) time, O(1) space (array must be sorted)
```

## Sliding Window Pattern

```python
# Longest substring without repeating
def length_of_longest_substring(s):
    char_idx = {}
    max_len = 0
    left = 0

    for right in range(len(s)):
        if s[right] in char_idx and char_idx[s[right]] >= left:
            left = char_idx[s[right]] + 1
        char_idx[s[right]] = right
        max_len = max(max_len, right - left + 1)

    return max_len
    # O(n) time, O(min(n, charset)) space
```

## Complexity Comparison

| Operation | Array | LinkedList | Stack | Queue |
|-----------|-------|-----------|-------|-------|
| Access | O(1) | O(n) | O(n) | O(n) |
| Insert Start | O(n) | O(1) | O(1) | O(1) |
| Insert End | O(1) | O(1) | O(1) | O(1) |
| Delete Start | O(n) | O(1) | O(1) | O(1) |
| Delete End | O(1) | O(n) | O(1) | O(n) |
| Search | O(n) | O(n) | O(n) | O(n) |

## Classic Problems

**Easy (10+ problems):**
1. Reverse linked list
2. Merge sorted lists
3. Remove duplicates
4. Palindrome linked list
5. Valid parentheses

**Medium (15+ problems):**
6. Next greater element
7. Largest rectangle in histogram
8. Trapping rain water
9. Minimum window substring
10. Container with most water

## Key Rules

✅ **Array when**: Need fast random access
✅ **LinkedList when**: Frequent insertions/deletions
✅ **Stack when**: LIFO or DFS
✅ **Queue when**: FIFO or BFS
✅ **Deque when**: Need both ends

---

**Master linear structures - they're the foundation of all data structure knowledge!**
