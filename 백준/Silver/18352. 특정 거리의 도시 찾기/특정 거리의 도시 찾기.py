from collections import deque
import sys
from sys import stdin
sys.setrecursionlimit(10**6)
input = stdin.readline

N,M,K,X = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (N+1)
distance[X] = 0

q = deque([X])
while q :
    now = q.popleft()

    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now]+1
            q.append(i)
check = False
if K in distance:
    for i in range(1,N+1):
        if distance[i] == K:
            print(i)
            check = True

else :
    if check == False:
        print(-1)