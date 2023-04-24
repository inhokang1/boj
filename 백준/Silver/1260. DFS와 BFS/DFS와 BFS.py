from collections import deque

from sys import stdin
input = stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph,i,visited)


def bfs(graph,v,visited2):
    queue = deque([v])  
    visited2[v] = True

    while queue:
        q = queue.popleft()  
        print(q, end=" ")

        for i in graph[q]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True


N,M,V = map(int,input().split())
graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (N + 1)
visited2 = [False] * (N + 1)

dfs(graph,V,visited)

print()

bfs(graph,V,visited2)