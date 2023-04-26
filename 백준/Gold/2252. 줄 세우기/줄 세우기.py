from collections import deque
from sys import stdin
input = stdin.readline

N,M = map(int,input().split())
visited = [0] * (N+1)

graph = [[] for i in range((N+1))]

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    visited[b] += 1

def wii():
    result = []
    q = deque()

    for i in range(1,N+1):
        if visited[i] == 0:
            q.append(i)

    while q :
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            visited[i] -=1

            if visited[i] == 0:
                q.append(i)

    for i in result:
        print(i, end= " ")

wii()