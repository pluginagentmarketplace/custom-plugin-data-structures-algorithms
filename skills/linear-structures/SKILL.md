---
name: linear-structures
description: Implement and manipulate linear data structures including arrays, strings, linked lists, stacks, and queues. Use when working with sequential data, implementing data structure operations, or solving linear structure problems.
---

# Linear Data Structures

## Quick Start

Linear structures organize data in a sequence. Master the operations and choose the right structure for your problem.

### Data Structure Selector

| Structure | Ordered | Insert | Access | Delete | Use When |
|-----------|---------|--------|--------|--------|----------|
| Array | Yes | O(n) | O(1) | O(n) | Random access needed |
| Linked List | Yes | O(1)* | O(n) | O(1)* | Insert/delete at known position |
| Stack | LIFO | O(1) | Top only | O(1) | Last-in-first-out pattern |
| Queue | FIFO | O(1) | Front only | O(1) | First-in-first-out pattern |
| Deque | Hybrid | O(1) | Both ends | O(1) | Both ends access |

## Arrays

### Basic Operations
```python
# Create array
arr = [1, 2, 3, 4, 5]

# Access: O(1)
element = arr[2]  # Returns 3

# Insert at end: O(1) amortized
arr.append(6)

# Insert at position: O(n)
arr.insert(2, 99)  # Insert 99 at index 2

# Delete: O(n)
arr.pop(2)  # Remove element at index 2
```

### Two-Pointer Technique
```python
def two_sum_sorted(arr, target):
    """Find two numbers that sum to target"""
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

## Strings

### String vs List of Characters
- Strings are immutable in Python
- String concatenation creates new object: O(n) time
- Convert to list for efficient modification

### Common String Operations
```python
# String slicing: O(n)
substring = s[start:end]

# String reversal: O(n)
reversed_s = s[::-1]

# Check palindrome: O(n)
is_palindrome = s == s[::-1]

# Count character frequency: O(n)
from collections import Counter
freq = Counter(s)
```

## Linked Lists

### Node Definition
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning: O(1)
    def insert_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Find node: O(n)
    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None
```

### Linked List Reversal
```python
def reverse_linked_list(head):
    """Reverse linked list in-place: O(n) time, O(1) space"""
    prev = None
    current = head
    while current:
        next_temp = current.next  # Save next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev forward
        current = next_temp       # Move current forward
    return prev
```

### Floyd's Cycle Detection
```python
def has_cycle(head):
    """Detect cycle in linked list"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Found cycle
            return True
    return False
```

## Stacks

### Basic Stack Implementation
```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        """Add element: O(1)"""
        self.items.append(value)

    def pop(self):
        """Remove and return top: O(1)"""
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        """View top element: O(1)"""
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0
```

### Valid Parentheses
```python
def is_valid_parentheses(s):
    """Check if parentheses are balanced"""
    stack = Stack()
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:
            stack.push(char)
        else:
            if stack.is_empty() or pairs[stack.pop()] != char:
                return False
    return stack.is_empty()
```

## Queues

### Basic Queue Implementation
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        """Add element: O(1)"""
        self.items.append(value)

    def dequeue(self):
        """Remove and return front: O(1)"""
        return self.items.popleft() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0
```

### Sliding Window
```python
def max_sliding_window(arr, k):
    """Find max in each window of size k: O(n)"""
    from collections import deque

    queue = deque()  # Stores indices
    result = []

    for i in range(len(arr)):
        # Remove elements outside window
        while queue and queue[0] < i - k + 1:
            queue.popleft()

        # Remove smaller elements
        while queue and arr[queue[-1]] <= arr[i]:
            queue.pop()

        queue.append(i)

        # Add to result when window is formed
        if i >= k - 1:
            result.append(arr[queue[0]])

    return result
```

## Practice Problems

1. **Reverse array in-place**
2. **Merge sorted arrays**
3. **Palindrome string check**
4. **Flatten nested list**
5. **LRU Cache implementation**
6. **Stock span problem using stack**
7. **First non-repeating character**
8. **Anagram grouping**

## Common Patterns

### Pattern: Two Pointers
- Start at opposite ends
- Move towards center
- Used for sorted arrays, linked lists

### Pattern: Sliding Window
- Maintain fixed/variable window
- Two pointers (start, end)
- Used for substring/subarray problems

### Pattern: Fast & Slow Pointers
- Slow moves 1 step, fast moves 2 steps
- Detect cycles in linked lists
- Find middle of linked list

## Key Takeaways

✓ Array: Fast random access, slow insertion
✓ Linked List: Fast insertion, slow access
✓ Stack: LIFO, useful for recursion, backtracking
✓ Queue: FIFO, useful for BFS, task scheduling
✓ Know trade-offs between structures
✓ Two-pointer and sliding window are powerful patterns
