import sys
from sys import stdin
sys.setrecursionlimit(10**6)
input = stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)

dfs(1)

for i in range(2,N+1):
    print(visited[i])