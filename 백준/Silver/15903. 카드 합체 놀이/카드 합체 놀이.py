import sys
import heapq
input = sys.stdin.readline

heap = []

n,m = map(int,input().split())

arr = list(map(int,input().split()))

for num in arr:
    heapq.heappush(heap,num)

for i in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap,a+b)
    heapq.heappush(heap,a+b)

print(sum(heap))