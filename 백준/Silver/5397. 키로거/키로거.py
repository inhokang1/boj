import sys
input = sys.stdin.readline

N = int(input())


for _ in range(N):
    word = list(input().rstrip())
    left =[]
    right =[]
    for i in word:
        if i == '<':
            if len(left) == 0:
                continue
            else:
                a = left.pop()
                right.append(a)
                
        elif i == '>':
            if len(right) == 0:
                continue
            else:
                b = right.pop()
                left.append(b)
                
        elif i == '-':
            if len(left) == 0:
                continue
            else:
                left.pop()
            
        else:
            left.append(i)
    right.reverse()
    stack = left + right

    print("".join(stack))


    # print("".join(left))
    