import sys
from sys import stdin
sys.setrecursionlimit(5000)
input = stdin.readline

N = int(input())
M = int(input())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [False] * (N + 1)

for _ in range(M):
    a,b = map(int,input().split())
    #입력 값이 간선이 이어주는 두 노드라서 1,2 가 입력되면
    # 1의 루트는 2    2의 루트는 1 이 된다는 말과 같다
    graph[a].append(b)
    graph[b].append(a)

#정렬
for i in graph:
    i.sort()

# DFS 함수
def dfs(graph, v, visited):
    global count
    visited[v] = True
    count +=1
    
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph,i,visited)


count = 0
dfs(graph,1,visited)

print(count-1)
