---
description: Master graphs, traversals (BFS, DFS), shortest paths (Dijkstra, Bellman-Ford), minimum spanning trees, topological sort, and advanced graph algorithms.
capabilities: ["graph-basics", "bfs-dfs", "shortest-path", "mst", "topological-sort", "strongly-connected", "bipartite-matching"]
---

# Graph Algorithms Guide

Graphs are the **most versatile data structure in computer science**. From social networks to route planning, mastering graph algorithms is essential for solving real-world problems at scale.

## Graph Representations

### 1. Adjacency Matrix
```python
# n x n matrix where matrix[i][j] = weight/existence
# Space: O(V²), Lookup: O(1), Dense graphs preferred

graph = [
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [0, 5, 1, 0]
]
```

### 2. Adjacency List
```python
# Dictionary/array of lists
# Space: O(V+E), Lookup: O(degree), Sparse graphs preferred

graph = {
    0: [(1, 1), (2, 4)],
    1: [(0, 1), (2, 2), (3, 5)],
    2: [(0, 4), (1, 2), (3, 1)],
    3: [(1, 5), (2, 1)]
}
```

## Core Traversal Algorithms

### Breadth-First Search (BFS)
```python
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    # Time: O(V+E), Space: O(V)
```

**Use Cases:**
- Shortest path in unweighted graphs
- Level-order traversal
- Finding connected components
- Bipartite graph detection

### Depth-First Search (DFS)
```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node)

    for neighbor, weight in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    # Time: O(V+E), Space: O(V) [recursion stack]
```

**Use Cases:**
- Topological sort
- Cycle detection
- Strongly connected components
- Backtracking problems

## Shortest Path Algorithms

### Dijkstra's Algorithm (Non-negative weights)
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
    # Time: O((V+E) log V), Space: O(V)
```

### Bellman-Ford (Negative weights allowed)
```python
def bellman_ford(graph, start, num_vertices):
    distances = {i: float('inf') for i in range(num_vertices)}
    distances[start] = 0

    # Relax edges V-1 times
    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            if distances[u] != float('inf'):
                for v, weight in graph[u]:
                    distances[v] = min(distances[v], distances[u] + weight)

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

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py
            return True
        return False

def kruskal(edges, num_vertices):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(num_vertices)
    mst = []

    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))

    return mst
    # Time: O(E log E), Space: O(V)
```

### Prim's Algorithm (Vertex-based)
```python
import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    min_heap = [(0, start, -1)]

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        if parent != -1:
            mst.append((parent, node, weight))

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, node))

    return mst
    # Time: O((V+E) log V), Space: O(V)
```

## Topological Sort

```python
def topological_sort(graph, num_vertices):
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
    # Time: O(V+E), Space: O(V)
    # Only for DAGs (Directed Acyclic Graphs)
```

**Use Cases:**
- Task scheduling (prerequisites)
- Dependency resolution
- Course scheduling
- Build system optimization

## Advanced Graph Algorithms

### Strongly Connected Components (Kosaraju)
- Time: O(V+E)
- Find groups of mutually reachable vertices
- Real use: Social network analysis

### Bipartite Graph Detection
- BFS/DFS with 2-coloring
- Time: O(V+E)
- Real use: Matching problems (jobs to workers)

### Maximum Flow / Minimum Cut
- Ford-Fulkerson, Edmonds-Karp
- Real use: Network optimization, supply chain

## Common Graph Problems (40+ problems)

### Basic Traversal (10+ problems)
1. Number of connected components
2. Detect cycle in undirected graph
3. Topological sort
4. Course schedule
5. Word ladder

### Shortest Path (12+ problems)
6. Network delay time (Dijkstra)
7. Cheapest flights with k stops (Bellman-Ford)
8. Path with maximum probability
9. Shortest path in grid
10. Reachable nodes in subdivided graph

### Advanced (18+ problems)
11. Critical connections in network
12. Minimum cost to connect cities (MST)
13. Maximum path sum (DAG)
14. Alien dictionary (Topological sort)
15. Reconstruct itinerary (Eulerian path)

## Learning Progression

### Level 1: Basics (Days 1-4)
- [ ] Graph representation (matrix vs list)
- [ ] BFS implementation and understanding
- [ ] DFS implementation and understanding
- [ ] Connected components and cycle detection

### Level 2: Shortest Paths (Days 5-9)
- [ ] Dijkstra's algorithm mastery
- [ ] Bellman-Ford and negative cycles
- [ ] A* algorithm fundamentals
- [ ] 20+ shortest path problems

### Level 3: Advanced (Days 10-15)
- [ ] MST algorithms (Kruskal, Prim)
- [ ] Topological sort and DAG applications
- [ ] SCC and bipartite matching
- [ ] Flow and matching problems

## Algorithm Selection Guide

| Problem | Algorithm | Time | Use When |
|---------|-----------|------|----------|
| Shortest path (unweighted) | BFS | O(V+E) | No weights |
| Shortest path (non-negative) | Dijkstra | O((V+E) log V) | Weights >= 0 |
| Shortest path (any weights) | Bellman-Ford | O(VE) | May have negative |
| MST | Kruskal/Prim | O(E log E) | Need minimum tree |
| Topological sort | DFS | O(V+E) | DAG only |
| All pairs | Floyd-Warshall | O(V³) | Small V |

## Real-World Applications

| Application | Algorithm |
|-------------|-----------|
| Google Maps | Dijkstra + A* |
| Social Networks | BFS (friends), SCC (communities) |
| Package Delivery | TSP + minimum path |
| Network Routing | OSPF (MST variant) |
| Database Queries | Topological sort |

## Next Steps

1. Implement BFS and DFS until automatic
2. Master Dijkstra and understand its variations
3. Solve 50+ graph problems
4. Study MST algorithms in depth
5. Learn advanced techniques (flow networks)

---

**Pro Tip**: "Most graph problems are variations of BFS/DFS + some modification. Master the base traversals first!"
