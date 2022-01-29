# BFS & DFS

from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        p = queue.popleft()
        print(p, "", end = '')
        for i in graph[p]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True


def dfs(graph, start, visited):
    visited[start] = True
    print(start, "", end = '')
    for i in graph[start]:
        if not (visited[i]):
            if not (visited[i]):
                dfs(graph, i, visited)


# 각 노드와 연결된 정보 (ex. [2, 3, 8]은 1번 노드와 연결된 정보이고, [1, 4, 5]는 3번 노드와 연결된 정보)
graph = deque([
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
])

visited = [False] * 9
print("DFS")
dfs(graph, 1, visited)

visited = [False] * 9
print("\nBFS")
bfs(graph, 1, visited)