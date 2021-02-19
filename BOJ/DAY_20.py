# 210216 TUE
# 1260
# from collections import deque


# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=" ")
#     for i in graph[v]:
#         # if not visited[i]:
#         if (not visited[i]) and graph[v][i]:
#             dfs(graph, i, visited)


# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end=" ")
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True


# n, m, v = map(int, input().split())
# graph = [[]]
# visited = [False]*(m+1)
# for _ in range(m):
#     graph.append(list(map(int, input().split())))
# print(graph, visited)
# dfs(graph, graph.index(v), visited)
# print(graph.index(v))
# for i in graph:
#     if v in i:
#         v = graph.index(i)
#         break
# print(visited)
# dfs(graph, v, visited)

# 11724
def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    for i in graph[v]:
        print(f"i: {i}")
        if not visited[i]:
            dfs(i)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (m+1)
print(graph)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
# for i in range(1, n+1):
#     if not visited[i]:
#         dfs(i)

print(visited)
