import sys
input = sys.stdin.readline

arr = list(input().rstrip())

stack = []
ans = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])

    else:
        if arr[i-1] == '(':
            stack.pop()
            ans += len(stack)

        else:
            stack.pop()
            ans += 1

print(ans)
