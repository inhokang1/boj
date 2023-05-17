import sys
input = sys.stdin.readline

n = int(input())

a = []
for _ in range(n):
    a.append(int(input()))
a.sort()

cnt = 0
for i in range(len(a)):
    if a[i] == i+1:
        continue
    else:
        b = a[i] - (i+1)
        cnt += abs(b)

print(cnt)
