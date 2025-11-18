---
name: graph-algorithms
description: Master graph algorithms including BFS, DFS, shortest paths, and spanning trees. Use for connectivity, pathfinding, and graph optimization problems.
---

# Graph Algorithms

## Quick Start

Learn traversals first, then move to specialized algorithms.

### Algorithm Selection

| Problem | Algorithm | Time | Best For |
|---------|-----------|------|----------|
| Connected components | DFS/BFS | O(V+E) | Component counting |
| Shortest path (unweighted) | BFS | O(V+E) | Simple/unweighted |
| Shortest path (weighted) | Dijkstra | O((V+E)logV) | Non-negative weights |
| All pairs shortest | Floyd-Warshall | O(V³) | Small graphs |
| Minimum spanning tree | Kruskal/Prim | O(ElogE)/O(V²) | MST |
| Topological sort | Kahn/DFS | O(V+E) | DAG ordering |

## Graph Representation

### Adjacency List
```python
# Best for sparse graphs, most operations
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
# Space: O(V+E)
```

### Adjacency Matrix
```python
# Best for dense graphs, fast edge queries
import numpy as np

graph = np.array([
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 0],  # C
    [0, 1, 0, 0]   # D
])
# Space: O(V²)
```

## Traversal Algorithms

### Breadth-First Search (BFS)
```python
from collections import deque

def bfs(graph, start):
    """Visit all reachable vertices, level by level"""
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order
    # Time: O(V+E), Space: O(V)
```

### Depth-First Search (DFS)
```python
def dfs_recursive(graph, vertex, visited=None):
    """Visit vertices deeply, backtrack when needed"""
    if visited is None:
        visited = set()

    visited.add(vertex)
    print(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited
    # Time: O(V+E), Space: O(V) for recursion stack

def dfs_iterative(graph, start):
    """DFS using stack instead of recursion"""
    visited = set()
    stack = [start]
    order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            stack.extend(reversed(graph[vertex]))

    return order
```

## Shortest Path Algorithms

### Dijkstra's Algorithm
```python
import heapq

def dijkstra(graph, start):
    """Shortest path from start to all vertices (non-negative weights)"""
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        current_dist, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        for neighbor, weight in graph[current]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
    # Time: O((V+E)logV), Space: O(V)
```

### Bellman-Ford Algorithm
```python
def bellman_ford(vertices, edges, start):
    """Shortest path, handles negative weights, detects negative cycles"""
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0

    # Relax edges V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative cycles
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            raise ValueError("Negative cycle detected")

    return distances
    # Time: O(VE), Space: O(V)
```

### Floyd-Warshall Algorithm
```python
def floyd_warshall(graph):
    """All pairs shortest paths"""
    n = len(graph)
    dist = [row[:] for row in graph]  # Copy matrix

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
    # Time: O(V³), Space: O(V²)
```

## Minimum Spanning Tree

### Kruskal's Algorithm (with Union-Find)
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Find with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union with rank"""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal(n, edges):
    """Find MST using Kruskal's algorithm"""
    edges.sort(key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(n)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            if len(mst) == n - 1:
                break

    return mst, total_weight
    # Time: O(ElogE), Space: O(V)
```

### Prim's Algorithm
```python
import heapq

def prim(graph, start):
    """Find MST using Prim's algorithm"""
    visited = set()
    min_heap = [(0, start)]
    mst_weight = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if u in visited:
            continue

        visited.add(u)
        mst_weight += weight

        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))
                mst_edges.append((u, v, w))

    return mst_edges, mst_weight
    # Time: O((V+E)logV), Space: O(V)
```

## Topological Sorting

### Kahn's Algorithm (BFS-based)
```python
from collections import deque

def topological_sort_kahn(n, edges):
    """Topological sort for DAG"""
    graph = [[] for _ in range(n)]
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return order if len(order) == n else []
    # Time: O(V+E), Space: O(V)
```

### DFS-based Topological Sort
```python
def topological_sort_dfs(graph):
    """DFS approach to topological sorting"""
    visited = set()
    order = []

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        order.append(v)

    for v in graph:
        if v not in visited:
            dfs(v)

    return order[::-1]  # Reverse to get topological order
    # Time: O(V+E), Space: O(V)
```

## Connectivity & Cycles

### Connected Components
```python
def find_components(graph):
    """Find all connected components"""
    visited = set()
    components = []

    def dfs(v, component):
        visited.add(v)
        component.append(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for v in graph:
        if v not in visited:
            component = []
            dfs(v, component)
            components.append(component)

    return components
    # Time: O(V+E), Space: O(V)
```

### Cycle Detection (Undirected)
```python
def has_cycle_undirected(graph):
    """Detect cycle in undirected graph"""
    visited = set()

    def dfs(v, parent):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent:  # Back edge found
                return True
        return False

    for v in graph:
        if v not in visited:
            if dfs(v, None):
                return True
    return False
```

## Interview Tips

- Master BFS and DFS first
- Understand when each algorithm applies
- Practice graph problem recognition
- Union-Find is powerful for connectivity
- Know adjacency list vs matrix trade-offs
- Debug by printing traversal order

## Key Takeaways

✓ BFS for shortest path (unweighted)
✓ Dijkstra for shortest path (weighted)
✓ DFS for connectivity and cycles
✓ Union-Find for MST and grouping
✓ Topological sort for dependency ordering
✓ Know space-time trade-offs
