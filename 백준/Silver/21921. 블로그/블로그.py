import sys
input = sys.stdin.readline

n,x = map(int,input().split())
arr = list(map(int,input().split()))

a = sum(arr[:x])
b = [a]

for i in range(x,n):
    c = a - arr[i-x]+arr[i]
    b.append(c)
    a = c

if max(b) == 0:
    print("SAD")
else:
    print(max(b))
    print(b.count(max(b)))