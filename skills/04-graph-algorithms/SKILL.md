---
name: graph-algorithms-skill
description: Graph representations, BFS/DFS traversals, shortest path algorithms (Dijkstra, Bellman-Ford), minimum spanning trees, topological sort, and advanced graph techniques.
---

# Graph Algorithms Skill

## Quick Start

**Graph Fundamentals:**
- **Vertices (V)**: Nodes in the graph
- **Edges (E)**: Connections between vertices
- **Directed**: Edges have direction (A → B)
- **Undirected**: Edges are bidirectional (A ↔ B)
- **Weighted**: Edges have weights/costs
- **Unweighted**: All edges have weight 1

## Graph Representations

### Adjacency Matrix
```python
# For dense graphs or complete graphs
graph = [
    [0, 1, 4, 0],   # Node 0: connects to 1 (weight 1), 2 (weight 4)
    [1, 0, 2, 5],   # Node 1: connects to 0 (weight 1), 2 (weight 2), 3 (weight 5)
    [4, 2, 0, 1],
    [0, 5, 1, 0]
]

# Access: O(1)
# Space: O(V²)
# Best for: Dense graphs, complete graphs
```

### Adjacency List
```python
# For sparse graphs (most real-world graphs)
graph = {
    0: [(1, 1), (2, 4)],      # Node 0: [(neighbor, weight), ...]
    1: [(0, 1), (2, 2), (3, 5)],
    2: [(0, 4), (1, 2), (3, 1)],
    3: [(1, 5), (2, 1)]
}

# Or as list of lists
graph = [
    [(1, 1), (2, 4)],
    [(0, 1), (2, 2), (3, 5)],
    [(0, 4), (1, 2), (3, 1)],
    [(1, 5), (2, 1)]
]

# Access: O(degree)
# Space: O(V + E)
# Best for: Sparse graphs
```

## Depth-First Search (DFS)

```python
# Recursive
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node)

    for neighbor, weight in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited
    # Time: O(V + E), Space: O(V) [recursion stack]

# Iterative
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbor, weight in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited
```

**Use Cases:**
- Cycle detection
- Topological sort
- Connected components
- Strongly connected components
- Backtracking problems

## Breadth-First Search (BFS)

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result
    # Time: O(V + E), Space: O(V)
```

**Use Cases:**
- Shortest path in unweighted graphs
- Level-order traversal
- Bipartite checking
- Connected components

## Shortest Path Algorithms

### Dijkstra's Algorithm (Non-negative weights)

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in range(len(graph))}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        current_dist, node = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
    # Time: O((V + E) log V), Space: O(V)

# Example usage
graph = {
    0: [(1, 1), (2, 4)],
    1: [(0, 1), (2, 2), (3, 5)],
    2: [(0, 4), (1, 2), (3, 1)],
    3: [(1, 5), (2, 1)]
}
print(dijkstra(graph, 0))
# Output: {0: 0, 1: 1, 2: 3, 3: 4}
```

### Bellman-Ford Algorithm (Any weights, detects negative cycles)

```python
def bellman_ford(graph, start, num_vertices):
    distances = [float('inf')] * num_vertices
    distances[start] = 0

    # Relax edges V-1 times
    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            if distances[u] != float('inf'):
                for v, weight in graph[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight

    # Check for negative cycles
    for u in range(num_vertices):
        if distances[u] != float('inf'):
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    return None  # Negative cycle detected

    return distances
    # Time: O(V*E), Space: O(V)
```

## Minimum Spanning Tree (MST)

### Kruskal's Algorithm (Edge-based)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal(edges, num_vertices):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(num_vertices)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight
    # Time: O(E log E), Space: O(V)
```

### Prim's Algorithm (Vertex-based)

```python
import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    min_heap = [(0, start, -1)]
    total_weight = 0

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        if parent != -1:
            mst.append((parent, node, weight))
            total_weight += weight

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, node))

    return mst, total_weight
    # Time: O((V + E) log V), Space: O(V)
```

## Topological Sort

```python
def topological_sort_dfs(graph, num_vertices):
    visited = [False] * num_vertices
    stack = []

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)

    for i in range(num_vertices):
        if not visited[i]:
            dfs(i)

    return stack[::-1]
    # Time: O(V + E), Space: O(V)
    # Only for DAGs!

def topological_sort_bfs(graph, num_vertices):
    from collections import deque

    in_degree = [0] * num_vertices
    for u in range(num_vertices):
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([i for i in range(num_vertices) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == num_vertices else None
    # Time: O(V + E), Space: O(V)
```

## Cycle Detection

```python
# Undirected graph
def has_cycle_undirected(graph, num_vertices):
    visited = [False] * num_vertices

    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for i in range(num_vertices):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False

# Directed graph
def has_cycle_directed(graph, num_vertices):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * num_vertices

    def dfs(node):
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    for i in range(num_vertices):
        if color[i] == WHITE:
            if dfs(i):
                return True
    return False
```

## Classic Problems

**Basic (8+ problems):**
1. Number of connected components
2. Valid tree
3. Detect cycle
4. Topological sort
5. Course schedule

**Shortest Path (10+ problems):**
6. Network delay time (Dijkstra)
7. Cheapest flights with K stops (Bellman-Ford)
8. Path with maximum probability
9. Minimum cost to connect cities (MST)
10. Reachable nodes in subdivided graph

**Advanced (12+ problems):**
11. Critical connections
12. Word ladder (BFS)
13. Alien dictionary (Topological sort)
14. Minimum effort path (Dijkstra)
15. Reconstruct itinerary (Eulerian path)

## Algorithm Selection

| Problem | Algorithm | Time | Use When |
|---------|-----------|------|----------|
| Connected components | DFS/BFS/Union-Find | O(V+E) | Need all components |
| Shortest path (unweighted) | BFS | O(V+E) | No weights |
| Shortest path (weighted) | Dijkstra | O((V+E)logV) | Non-negative |
| Shortest path (negative) | Bellman-Ford | O(VE) | May have negative |
| MST | Kruskal/Prim | O(ElogE) | Connect all vertices |
| Topological sort | DFS | O(V+E) | DAG only |

---

**Graphs are the most powerful abstraction in CS - master them!**
