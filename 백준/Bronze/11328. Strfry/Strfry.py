n = int(input())


for _ in range(n):
    a,b = input().split()
    x = sorted(a)
    y = sorted(b)
    print("Possible" if x == y else "Impossible")



