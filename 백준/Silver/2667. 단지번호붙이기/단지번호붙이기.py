#DFS로 1이 나오면 1로 연결된 노드들을 방문
num = []
def dfs(x,y):

    if x <= -1 or x >= n or y<= -1 or y>= n:
        return False
    
    #1을 찾으면 
    if graph[x][y] != 0:
        global count
        count +=1
        # 방문처리
        graph[x][y] = 0

        # 상하좌우 확인
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x, y+1)

        return True
    return False



n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

result = 0
count = 0


for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            result +=1
            num.append(count)
            count = 0
            
num.sort()
print(result)
for i in range(len(num)):
    print(num[i])