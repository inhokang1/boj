import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    word = input()
    c = list(word)
    count = 0
    for i in c:
        if i == "(":
            count +=1
        elif i == ")":
            count -=1
        if count < 0:
            print('NO')
            break   
    if count == 0:
        print("YES")
    elif count >0:
        print("NO")
