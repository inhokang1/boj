import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int,input().split()))
dp = [0]*n

for i in range(n):
    for j in range(i):
        if a[i]>a[j] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i] +=1


print(max(dp))
x = max(dp)

result = []
for i in range(n-1,-1,-1):
    if dp[i] == x:
        result.append(a[i])
        x -=1
result.reverse()
for r in result:
    print(r,end=" ")