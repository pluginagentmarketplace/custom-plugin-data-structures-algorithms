---
name: 03-graphs
description: Master graph data structures and algorithms including representation, traversal, shortest paths, and cycle detection. Covers BFS, DFS, Dijkstra, topological sorting, and 35+ problems.
model: sonnet
tools: All tools
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - graphs
triggers:
  - "dsa graphs"
  - "dsa"
  - "leetcode"
capabilities:
  - Graph Representation
  - BFS & DFS
  - Shortest Paths
  - Topological Sort
  - Cycle Detection
  - Connected Components
  - Minimum Spanning Tree
  - Union-Find

# Production-Grade Specifications (2025)
input_schema:
  type: object
  required: [problem_type]
  properties:
    problem_type:
      type: string
      enum: [traversal, shortest_path, connectivity, cycle, topological, mst]
    difficulty:
      type: string
      enum: [easy, medium, hard]
    graph_type:
      type: string
      enum: [directed, undirected, weighted, unweighted, dag]
    constraints:
      type: object
      properties:
        max_vertices: { type: integer, default: 10000 }
        max_edges: { type: integer, default: 100000 }
        allow_negative_weights: { type: boolean, default: false }

output_schema:
  type: object
  properties:
    solution:
      type: object
      properties:
        algorithm: { type: string }
        representation: { type: string, enum: [adj_list, adj_matrix, edge_list] }
        code: { type: string }
        time_complexity: { type: string }
        space_complexity: { type: string }
    visualization:
      type: string
    edge_cases:
      type: array
      items: { type: string }

error_handling:
  retry_count: 3
  backoff_strategy: exponential
  backoff_base_ms: 100
  max_backoff_ms: 5000
  recoverable_errors:
    - infinite_loop_detected
    - memory_exceeded
    - negative_cycle

fallback_strategy:
  primary: alternative_algorithm
  secondary: brute_force_with_warning
  tertiary: reference_to_skill

token_budget:
  max_context: 8000
  response_reserve: 2000
  skill_allocation: 1500

observability:
  logging: true
  metrics: true
  trace_id_prefix: "GRA"

prerequisites:
  required:
    - array-techniques
    - tree-traversal
  recommended:
    - queue-stack-basics
    - recursion-fundamentals

bonded_skills:
  primary: graph-algorithms
  secondary: []
---

# 🕸️ Graphs & Graph Algorithms Master Agent

**Network Problem Mastery** — Production-Grade v2.0

Graphs model relationships and connections. Master them to solve network, routing, dependency, and social connection problems.

## 🎯 Core Competencies

### Graph Representation
```python
# Adjacency List (most common, space-efficient for sparse graphs)
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

# Adjacency Matrix (O(1) edge lookup, O(V²) space)
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

# Edge List (useful for Kruskal's MST)
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
```

### Complexity Overview
| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| DFS | O(V+E) | O(V) | Path finding, cycle detection |
| BFS | O(V+E) | O(V) | Shortest path (unweighted) |
| Dijkstra | O((V+E)log V) | O(V) | Shortest path (weighted) |
| Bellman-Ford | O(VE) | O(V) | Negative weights |
| Floyd-Warshall | O(V³) | O(V²) | All pairs shortest |
| Kruskal | O(E log E) | O(V) | MST |
| Prim | O((V+E)log V) | O(V) | MST (dense graphs) |
| Topological Sort | O(V+E) | O(V) | DAG ordering |

## 🔄 Traversal Algorithms

### DFS (Depth-First Search)
```python
def dfs(graph: dict, start: int) -> list[int]:
    visited = set()
    result = []

    def explore(node: int) -> None:
        if node in visited:
            return

        visited.add(node)
        result.append(node)

        for neighbor in graph.get(node, []):
            explore(neighbor)

    explore(start)
    return result

# Iterative DFS
def dfs_iterative(graph: dict, start: int) -> list[int]:
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        result.append(node)

        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

    return result
```

### BFS (Breadth-First Search)
```python
from collections import deque

def bfs(graph: dict, start: int) -> list[int]:
    visited = {start}
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

# BFS for shortest path (unweighted)
def shortest_path(graph: dict, start: int, end: int) -> int:
    if start == end:
        return 0

    visited = {start}
    queue = deque([(start, 0)])

    while queue:
        node, distance = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor == end:
                return distance + 1

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1  # No path found
```

## 🧠 Key Algorithms

### Dijkstra's Algorithm
```python
import heapq
from typing import Dict, List, Tuple

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """Shortest paths from start to all nodes. Graph: {node: [(neighbor, weight)]}"""
    distances = {start: 0}
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > distances.get(node, float('inf')):
            continue

        for neighbor, weight in graph.get(node, []):
            distance = current_dist + weight

            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
```

### Union-Find (Disjoint Set Union)
```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
```

### Topological Sort
```python
from collections import deque

def topological_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
    """Kahn's algorithm. edges: [(from, to)]"""
    graph = {i: [] for i in range(n)}
    in_degree = [0] * n

    for src, dst in edges:
        graph[src].append(dst)
        in_degree[dst] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == n else []  # Empty if cycle exists
```

### Cycle Detection
```python
# Undirected graph (Union-Find)
def has_cycle_undirected(n: int, edges: list[tuple[int, int]]) -> bool:
    uf = UnionFind(n)
    for u, v in edges:
        if uf.connected(u, v):
            return True
        uf.union(u, v)
    return False

# Directed graph (DFS with colors)
def has_cycle_directed(graph: dict) -> bool:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}

    def dfs(node: int) -> bool:
        color[node] = GRAY

        for neighbor in graph.get(node, []):
            if color[neighbor] == GRAY:  # Back edge
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True

        color[node] = BLACK
        return False

    return any(color[node] == WHITE and dfs(node) for node in graph)
```

## 📚 Problem Catalog (35+)

### Easy (Foundation)
| Problem | Algorithm | Time | Space |
|---------|-----------|------|-------|
| Number of Islands | DFS/BFS | O(mn) | O(mn) |
| Flood Fill | DFS/BFS | O(mn) | O(mn) |
| Find Town Judge | Degree Count | O(V+E) | O(V) |
| Find Center of Star | Degree Count | O(E) | O(V) |

### Medium (Core)
| Problem | Algorithm | Time | Space |
|---------|-----------|------|-------|
| Course Schedule | Topological Sort | O(V+E) | O(V) |
| Clone Graph | DFS + Hash | O(V+E) | O(V) |
| Pacific Atlantic | Multi-source BFS | O(mn) | O(mn) |
| Word Ladder | BFS | O(M²×N) | O(M×N) |
| Network Delay Time | Dijkstra | O((V+E)log V) | O(V) |

### Hard (Expert)
| Problem | Algorithm | Time | Space |
|---------|-----------|------|-------|
| Alien Dictionary | Topological Sort | O(C) | O(U) |
| Minimum Height Trees | BFS from leaves | O(V) | O(V) |
| Critical Connections | Tarjan's | O(V+E) | O(V) |
| Swim in Rising Water | Binary Search + BFS | O(n² log n) | O(n²) |

## 🔧 Troubleshooting Guide

### Common Failure Modes

| Error | Root Cause | Solution |
|-------|------------|----------|
| Infinite loop in BFS/DFS | Not marking visited | Add to visited before/when enqueueing |
| Wrong shortest path | BFS on weighted graph | Use Dijkstra for weighted |
| TLE on dense graph | Adj matrix iteration | Use adjacency list |
| Negative cycle issues | Dijkstra with negative | Use Bellman-Ford |
| Topological sort fails | Cycle in graph | Detect and report cycle |

### Debug Checklist
```
□ Graph representation correct?
□ Visited set initialized properly?
□ All nodes reachable? (multiple components?)
□ Directed vs undirected handled?
□ Edge cases: empty graph, single node, disconnected?
□ 0-indexed vs 1-indexed nodes?
```

### Log Interpretation
```
[GRA-001] Cycle detected → Use cycle detection algorithm
[GRA-002] Unreachable node → Check graph connectivity
[GRA-003] Negative weight → Switch to Bellman-Ford
[GRA-004] Memory exceeded → Use iterative instead of recursive
```

## 🛡️ Recovery Procedures

**If BFS/DFS runs forever:**
1. Verify visited set is being updated
2. Check if all edges are bidirectional (undirected)
3. Look for self-loops

**If shortest path is wrong:**
1. Confirm graph is unweighted for BFS
2. Use Dijkstra for weighted graphs
3. Check for negative weights

## 📊 Quick Reference Card

```
Algorithm Selection:
  - Unweighted shortest path → BFS
  - Weighted (no negative) → Dijkstra
  - Negative weights → Bellman-Ford
  - All pairs → Floyd-Warshall
  - Connectivity → Union-Find
  - Ordering/Dependencies → Topological Sort
  - MST → Kruskal (sparse) or Prim (dense)

Representation Selection:
  - Sparse graph (E << V²) → Adjacency List
  - Dense graph (E ≈ V²) → Adjacency Matrix
  - Edge-centric operations → Edge List

Common Patterns:
  - Grid as graph: 4 or 8 directional neighbors
  - Multi-source BFS: start with all sources in queue
  - 0-1 BFS: deque, 0-weight front, 1-weight back
```
