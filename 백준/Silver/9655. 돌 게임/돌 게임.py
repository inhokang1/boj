import sys
input = sys.stdin.readline

n = int(input())

dp = [-1]*10001

# 1은 상근이를 뜻하고
# 0은 창영이를 뜻한다
dp[1] = 1
dp[2] = 0
dp[3] = 1

#문제는 홀수면 상근이가 이기고
# 짝수면 창영이가 이기는 게임이다
for i in range(4,n+1):
    if dp[i-1] == 1 or dp[i-3] == 1:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[n] == 1:
    print("SK")
else:
    print("CY")