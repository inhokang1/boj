import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
A, B = map(int, input().split())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def BFS(a, b):
    queue = deque([A])
    visited[A] = 0

    while queue:
        people = queue.popleft()

        if people == b:
            return visited[B]
        
        for i in graph[people]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[people]+1
    return -1


print(BFS(A, B))