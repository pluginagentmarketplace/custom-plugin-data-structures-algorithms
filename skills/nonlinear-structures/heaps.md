---
name: heaps
description: Master heap data structures. Min/max heaps, heapify, priority queues. O(log n) operations on dynamic datasets.
---

# Heaps

## Heap Properties
- Min Heap: Parent ≤ Children
- Max Heap: Parent ≥ Children
- Complete binary tree

## Array Representation
- Left child: 2i+1
- Right child: 2i+2
- Parent: (i-1)/2

## Operations
- Insert: O(log n) - heapify up
- Extract: O(log n) - heapify down
- Get min/max: O(1)
- Build heap: O(n)

## Applications
- Priority queue
- Heap sort: O(n log n)
- Top K elements
- Median finding

## Common Pattern
```python
import heapq
pq = []
heapq.heappush(pq, item)
min_item = heapq.heappop(pq)
```
