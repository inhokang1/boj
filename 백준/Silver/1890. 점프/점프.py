import sys
input = sys.stdin.readline

N = int(input())

game = [list(map(int, input().split())) for i in range(N)]

dp = [[0]*N for _ in range(N)]

dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if x == y == N-1:
            print(dp[x][y])
            exit(0)

        dist = game[x][y]
        if x+dist < N:
            dp[x+dist][y] += dp[x][y]

        if y+dist < N:
            dp[x][y+dist] += dp[x][y]