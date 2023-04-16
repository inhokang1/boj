import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())

stack = deque(str(i) for i in range(1,N+1))
answer = []

while len(stack)>=1:
    for i in range(K-1):
        stack.append(stack.popleft())
    answer.append(stack.popleft())

print("<%s>" %(", ".join(answer)))   