
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

stack = deque([])

for _ in range(N):

    word = input().split()

    if word[0] == "push":
        stack.append(word[1])

    elif word[0] == "pop":
        if not stack :
            print(-1)
        else:
            print(stack.popleft()) 

    elif word[0] == "size":
        print(len(stack))

    elif word[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif word[0] == "front":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])

    elif word[0] == "back":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])