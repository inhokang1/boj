import sys
input = sys.stdin.readline

N,K = map(int,input().split())

coins = []
cnt = 0

for i in range(N):
    coins.append(int(input()))

#coins의 값들을 역순으로 나오게 하기위해 reversed 사용
for coin in reversed(coins):
    cnt += K//coin
    K %= coin

print(cnt)

