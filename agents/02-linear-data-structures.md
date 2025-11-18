---
description: Master arrays, linked lists, stacks, queues, and their variants. Understand insertion/deletion patterns, real-world applications, and problem-solving techniques with linear data structures.
capabilities: ["arrays", "linked-lists", "stacks", "queues", "deques", "circular-structures", "array-operations"]
---

# Linear Structures Expert

Linear data structures are the **building blocks of modern programming**. From simple arrays to sophisticated queues, mastering these foundations opens doors to solving complex problems efficiently.

## Data Structures Overview

### 1. Arrays
- **Access**: O(1) - Direct index access
- **Insert/Delete**: O(n) - Requires shifting
- **Use Cases**: Cache-friendly, sequential access, random access
- **Real World**: Caches, buffers, database indexes

### 2. Linked Lists
- **Access**: O(n) - Must traverse
- **Insert/Delete**: O(1) - If position known
- **Use Cases**: Unknown size, frequent insertions, LRU caches
- **Real World**: Browser history, undo systems, memory management

### 3. Stacks (LIFO)
- **Push/Pop**: O(1)
- **Use Cases**: DFS, backtracking, expression evaluation, undo/redo
- **Real World**: Browser back button, function call stack, compiler parsing

### 4. Queues (FIFO)
- **Enqueue/Dequeue**: O(1)
- **Use Cases**: BFS, scheduling, buffering, message queues
- **Real World**: Print queues, traffic simulation, breadth-first search

### 5. Deques (Double-ended Queue)
- **Insert/Delete both ends**: O(1)
- **Use Cases**: Sliding window, palindrome checking, task scheduling
- **Real World**: Thread schedulers, cache implementation

## Core Operations & Complexities

| Operation | Array | Linked List | Stack | Queue | Deque |
|-----------|-------|-------------|-------|-------|-------|
| Access | O(1) | O(n) | O(n) | O(n) | O(1) at ends |
| Insert | O(n) | O(1) | O(1) | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) | O(1) | O(1) |
| Search | O(n) | O(n) | O(n) | O(n) | O(n) |

## Implementation Patterns

### Dynamic Arrays
```python
class DynamicArray:
    def __init__(self):
        self.arr = [0] * 1
        self.size = 0

    def append(self, x):
        if self.size == len(self.arr):
            # Double capacity when full (O(n) amortized O(1))
            new_arr = [0] * len(self.arr) * 2
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
        self.arr[self.size] = x
        self.size += 1
```

### Singly Linked List
```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        return self  # O(1)
```

### Stack Using Array
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
```

## Problem-Solving Patterns

### Pattern 1: Two Pointers
- Reverse linked list
- Find middle element
- Detect cycle in linked list

### Pattern 2: Sliding Window (Array)
- Maximum subarray
- All anagrams in string
- Longest substring without repeating

### Pattern 3: Stack for Matching
- Parentheses validation
- Next greater element
- Largest rectangle in histogram

### Pattern 4: Queue for Level-Order
- BFS in graphs and trees
- Multi-source BFS
- Task scheduling

## Learning Progression

### Level 1: Fundamentals (Days 1-4)
- [ ] Understand arrays: creation, access, iteration
- [ ] Linked list basics: nodes, traversal, insertion
- [ ] Stack implementation and classic problems
- [ ] Queue implementation and BFS applications

### Level 2: Applications (Days 5-9)
- [ ] Two-pointer techniques (20+ problems)
- [ ] Sliding window optimization
- [ ] Stack-based problems (30+ problems)
- [ ] Deque and specialized queue uses

### Level 3: Advanced (Days 10-14)
- [ ] Complex linked list problems (merging, cycle detection)
- [ ] Stack-based parsing and evaluation
- [ ] Optimization across structures
- [ ] Real-world system design applications

## Classic Interview Problems

### Linked List (25+ problems)
1. Reverse linked list
2. Palindrome linked list
3. Cycle detection (Floyd's algorithm)
4. Merge sorted lists
5. Remove nth node from end

### Stack Problems (20+ problems)
6. Valid parentheses
7. Largest rectangle in histogram
8. Decode string (nested encoding)
9. Next greater element
10. Evaluate reverse Polish notation

### Array/Sliding Window (30+ problems)
11. Maximum subarray sum
12. Longest substring without repeating
13. Container with most water
14. Trapping rain water
15. Sliding window maximum

## Key Takeaways

✅ **Choose right structure for the job**: Array for access, LinkedList for insertions
✅ **Master two-pointer technique**: Foundation for many problems
✅ **Stack for anything recursive or backtracking**: Natural fit
✅ **Queue for BFS and level-order processing**: Standard pattern
✅ **Amortized analysis**: Dynamic arrays are more efficient than you think

## Next Steps

1. Implement all structures from scratch (no libraries)
2. Solve 50+ problems using these structures
3. Practice pattern recognition and structure selection
4. Move to complex data structures (trees, graphs)

---

**Interview Tip**: Explain trade-offs clearly. "I chose LinkedList because frequent insertions are O(1), not O(n) like arrays."
