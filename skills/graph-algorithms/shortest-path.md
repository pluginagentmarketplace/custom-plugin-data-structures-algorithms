---
name: shortest-path
description: Master shortest path algorithms. Dijkstra, Bellman-Ford, Floyd-Warshall. Understand when to use each.
---

# Shortest Path Algorithms

## Dijkstra
- Time: O((V+E) log V) with heap
- Space: O(V)
- Handles: Non-negative weights
- Use: Most common, single-source

## Bellman-Ford
- Time: O(VE)
- Space: O(V)
- Handles: Negative weights
- Detects: Negative cycles

## Floyd-Warshall
- Time: O(V³)
- Space: O(V²)
- Handles: All-pairs shortest path
- Use: Small graphs, dense

## Decision Guide
- Single source, non-negative? → Dijkstra
- Single source, negative? → Bellman-Ford
- All pairs? → Floyd-Warshall
- DAG? → DAG shortest path

## Real-world Use
- GPS navigation (Dijkstra)
- Network routing (Bellman-Ford)
- Game pathfinding (A*)
