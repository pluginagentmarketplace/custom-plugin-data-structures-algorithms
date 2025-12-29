# Graphs Guide

## BFS - Level-order, Shortest Path (Unweighted)
```python
from collections import deque
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## Dijkstra - Shortest Path (Weighted)
O((V+E) log V) with heap
