import sys
input = sys.stdin.readline

task = []
result = 0
n = int(input())
for _ in range(n):
    case = list(map(int,input().split()))
    if case[0] == 1:
        task.append((case[1],case[2]))
    if task:
        score, time = task.pop()
        time -= 1
        if time == 0:
            result += score
        else:
            task.append((score, time))
print(result)