import sys
input = sys.stdin.readline

N = int(input())

s = [[0,0]]

for i in range(1,N+1):
    a,b = map(int,input().split())
    s.append([a,b])

s = sorted(s, key=lambda a: a[0])
s = sorted(s, key = lambda a : a[1])

h = []
f = 0

for i in range(1, N+1):
    if f<=s[i][0]:
        h += [i]
        f = s[i][1]

print(len(h))