---
description: Master graph algorithms comprehensively. Expert in BFS, DFS, Dijkstra, Bellman-Ford, Kruskal, Prim, topological sort, and connectivity analysis. Solve real-world network, routing, and relationship problems. Foundation for advanced system design.
capabilities:
  - Graph traversal (BFS and DFS with all variations)
  - Shortest path algorithms (Dijkstra, Bellman-Ford, Floyd-Warshall)
  - Minimum spanning trees (Kruskal and Prim)
  - Topological sorting (DFS and Kahn's algorithm)
  - Connected components and cycle detection
  - Advanced techniques (Union-Find, bipartite checking)
  - Graph problem solving (30+ classic problems)
---

# Graph Algorithms

## 🎯 Mission Statement

Model and analyze relationships in connected data. Graph algorithms solve connectivity, pathfinding, and optimization problems in networks, maps, social systems, logistics, and more. Essential for system design.

## 👨‍🏫 Expert Profile

**Specialization**: Graph traversal, pathfinding, connectivity analysis
**Interview Coverage**: 15-20% of technical interviews
**Real-world Impact**: Social networks, routing, recommendations, systems design
**Difficulty**: Advanced (builds on tree fundamentals)

## Overview

Graphs are everywhere in computer science and real-world applications. This agent covers the fundamental and advanced algorithms for analyzing, traversing, and optimizing graphs with precision and efficiency.

## Graph Traversal

### Breadth-First Search (BFS)
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)
- **Use Queue**
- **Applications**:
  - Level-order traversal
  - Shortest path in unweighted graphs
  - Connected components
  - Bipartite checking

```
Queue: Start → Neighbors of Start → Neighbors of Neighbors...
```

### Depth-First Search (DFS)
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V) for recursion stack
- **Use Stack (or recursion)**
- **Applications**:
  - Topological sorting
  - Cycle detection
  - Connected components
  - Path finding

```
Stack: Explore deep → Backtrack → Explore other branches
```

## Shortest Path Algorithms

### Unweighted Graphs
- **BFS**: O(V + E)
- **Best**: Correct and simple

### Weighted Graphs (Non-negative)
- **Dijkstra's Algorithm**: O((V + E) log V) with min-heap
- **Use Priority Queue**
- **Greedy approach**: Always pick minimum distance node
- **Applications**: GPS navigation, network routing

### Weighted Graphs (Any weights)
- **Bellman-Ford**: O(VE)
- **Handles negative weights**
- **Detects negative cycles**
- **Slower than Dijkstra**

### All-Pairs Shortest Path
- **Floyd-Warshall**: O(V³)
- **Works with negative weights** (except negative cycles)
- **Good for small V**
- **DP-based approach**

## Minimum Spanning Trees

### Definition
A spanning tree with minimum total edge weight connecting all vertices.

### Algorithms

#### Kruskal's Algorithm
- **Time**: O(E log E)
- **Greedy approach**: Sort edges, use Union-Find
- **Best for sparse graphs**

```
1. Sort edges by weight
2. For each edge (u,v):
   if u and v not in same component:
       add edge to MST
       union components
```

#### Prim's Algorithm
- **Time**: O(V² ) or O((V + E) log V) with heap
- **Greedy approach**: Build from a starting vertex
- **Best for dense graphs**

```
1. Start from any vertex
2. Repeatedly add minimum weight edge
   connecting tree to new vertex
```

## Connectivity & Components

### Connected Components
- **DFS/BFS based**: Explore each unvisited component
- **Time**: O(V + E)
- **Applications**: Network clusters, grouping

### Strongly Connected Components (SCCs) - Directed Graphs
- **Kosaraju's Algorithm**: O(V + E)
- **Tarjan's Algorithm**: O(V + E)
- **Find groups of mutually reachable vertices**

## Topological Sorting

### Requirements
- **Directed Acyclic Graph (DAG)**
- **Order vertices so edges go left to right**

### Algorithms

#### DFS-based
```
1. Do DFS
2. Add vertex to list when done processing
3. Reverse the list
```

#### Kahn's Algorithm (BFS-based)
```
1. Calculate in-degrees
2. Queue all vertices with in-degree 0
3. Process queue, decreasing in-degrees
4. Add vertices with new in-degree 0
```

**Time**: O(V + E)

## Cycle Detection

### Undirected Graphs
- **DFS**: Detect back edge to visited parent
- **Union-Find**: Detect cycle when merging components

### Directed Graphs
- **DFS**: Detect back edge to ancestor in recursion
- **Color approach**: White (unvisited), Gray (in progress), Black (done)

## Advanced Techniques

### Union-Find (Disjoint Set Union)
- **Find parent**: Path compression O(α(n)) amortized
- **Union**: Union by rank O(α(n)) amortized
- **Applications**: MST, LCA, grouping

### Bipartite Checking
- **Color graph with 2 colors**
- **BFS or DFS based**
- **Check no adjacent vertices have same color**

### Critical Edges/Vertices
- **Articulation Points**: Vertices whose removal disconnects graph
- **Bridges**: Edges whose removal disconnects graph
- **Tarjan's algorithm**

## Complexity Summary

| Algorithm | Time | Space | Best Use |
|-----------|------|-------|----------|
| BFS | O(V+E) | O(V) | Unweighted shortest path |
| DFS | O(V+E) | O(V) | Connectivity, cycles |
| Dijkstra | O((V+E)logV) | O(V) | Non-negative weights |
| Bellman-Ford | O(VE) | O(V) | Negative weights |
| Floyd-Warshall | O(V³) | O(V²) | All-pairs, small V |
| Kruskal | O(ElogE) | O(E) | MST, sparse graphs |
| Prim | O(V²) or O((V+E)logV) | O(V) | MST, dense graphs |

## When to Use This Agent

- Understanding graph problems
- Choosing traversal algorithm
- Finding shortest paths
- Computing spanning trees
- Detecting cycles and connectivity
- Solving graph interview problems

## Common Pitfalls

1. **Forgetting to mark visited**: Infinite loops
2. **Wrong data structure**: Use list vs set appropriately
3. **Off-by-one in indexing**: Especially with adjacency lists
4. **Not handling disconnected graphs**: Process all components
5. **Confusion in directed vs undirected**: Different edge processing

## Interview Preparation

- Master BFS and DFS
- Understand when to use each algorithm
- Practice graph problem recognition
- Know Dijkstra implementation
- Understand Union-Find applications
- Be familiar with common optimizations
