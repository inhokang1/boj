n1,n2 = input().split()
n3 = int(n1[::-1])
n4 = int(n2[::-1])
if n3 > n4 :
    print(n3)
elif n3 < n4 :
    print(n4)