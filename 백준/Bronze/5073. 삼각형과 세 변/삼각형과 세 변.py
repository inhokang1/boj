import sys
input = sys.stdin.readline

while(True):
    a,b,c = map(int,input().rstrip().split())
    if a == b == c == 0:
        break
    if a == b == c :
        print("Equilateral")
    elif 2*max(a,b,c) >= (a+b+c):
        print("Invalid")
    elif a == c or a == b or b == c :
        print("Isosceles")
    else:
        print("Scalene")