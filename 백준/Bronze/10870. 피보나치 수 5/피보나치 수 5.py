from sys import stdin
input = stdin.readline
n = int(input())

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-2)+fibo(n-1)
    
print(fibo(n))