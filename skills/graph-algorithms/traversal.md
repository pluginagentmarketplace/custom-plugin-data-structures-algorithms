---
name: graph-traversal
description: Master BFS and DFS. Understand when to use each, applications. Connected components, cycles, and topological sort.
---

# Graph Traversal

## BFS (Breadth-First Search)
- Time: O(V+E)
- Space: O(V)
- Queue-based
- Use: Shortest path (unweighted), level-order

## DFS (Depth-First Search)
- Time: O(V+E)
- Space: O(V)
- Recursion or stack
- Use: Connectivity, cycles, topological sort

## Connected Components
Count separate components using DFS/BFS

## Cycle Detection
- Undirected: Back edge in DFS
- Directed: Back edge to ancestor

## Topological Sort
- Use DFS with finish times
- Or Kahn's algorithm (BFS with in-degrees)
- Only for DAGs

## Applications
- Network connectivity
- Path finding
- Social networks
- Dependency resolution
