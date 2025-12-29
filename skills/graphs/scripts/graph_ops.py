#!/usr/bin/env python3
from collections import deque
def bfs(graph, start):
    visited, queue = {start}, deque([start])
    while queue:
        v = queue.popleft()
        for n in graph.get(v, []):
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return visited
