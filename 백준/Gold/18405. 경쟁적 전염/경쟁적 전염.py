from collections import deque

# 시험관의 크기와 바이러스 개수를 입력받기
n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스 정보를 담는 리스트

# 바이러스의 위치 정보 입력받기
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    # 입력받은 행 중에 바이러스가 있다면
    if graph[i][j] != 0:
      # 바이러스의 종류와 시간, 위치를 표시하고 바이러스 정보에 추가
      data.append((graph[i][j], 0, i, j))

# 바이러스 종류별로 오름차순 정렬 후 큐에 삽입
data.sort()
q = deque(data)

# 타겟 변수 입력받기
target_s, target_x, target_y = map(int, input().split())
# 시간 변수
s = 0

# 북, 동, 남, 서 이동방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 큐가 비거나 시간이 다 되었을 때 반복문 종료
while q:
  # 바이러스 종류, 현재시간, 바이러스 위치 꺼내오기
  virus, cnt, x, y = q.popleft()
  if cnt == target_s:
    break
  # 모든 이동방향을 확인하며  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 다음 방향으로 이동이 가능하다면
    if 0 <= nx < n and 0 <= ny < n:
      # 바이러스가 존재하지 않다면
      if graph[nx][ny] == 0:
        # 바이러스 전파
        graph[nx][ny] = virus
        # 바이러스 데이터 큐에 삽입
        q.append((virus, cnt+1, nx, ny))

# 정답 출력
print(graph[target_x - 1][target_y - 1])