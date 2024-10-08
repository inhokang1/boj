import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(x,y):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]

        if(0 <= nx < n) and (0 <= ny < m):
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                dfs(nx,ny)

#케이스 개수
T = int(input()) 

for _ in range(T):
    m,n,k = map(int,input().split())
    arr = [[0]*m for _ in range(n)]

    for _ in range(k):
        a,b = map(int,input().split()) 
        arr[b][a] = 1
    
    result = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                dfs(i,j)
                result +=1

    print(result)