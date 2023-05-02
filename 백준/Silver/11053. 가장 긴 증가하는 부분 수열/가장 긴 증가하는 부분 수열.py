import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int,input().split()))
B = [0]*N

for i in range(N):
    for j in range(i):
        if A[i]>A[j] and B[i]<B[j]:
            B[i]=B[j]
    B[i] += 1

print(max(B))