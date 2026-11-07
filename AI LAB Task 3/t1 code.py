from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': [] }
def bfs(strt, goal):
    queue = deque([(strt, [strt])])
    visited = []
    while queue:
        node, path = queue.popleft()
        visited.append(node)
        if node == goal:
            return visited, path
        for child in graph[node]:
            queue.append((child, path + [child]))
    return visited, None
def dfs(strt, goal):
    stack = [(strt, [strt])]
    visited = []
    while stack:
        node, path = stack.pop()
        visited.append(node)
        if node == goal:
            return visited, path
        for child in reversed(graph[node]):
            stack.append((child, path + [child]))
    return visited, None
print("BFS:", bfs('A', 'G'))
print("DFS:", dfs('A', 'G'))
