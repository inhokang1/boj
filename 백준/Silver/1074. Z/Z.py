n,x,y = map(int,input().split())
cnt = 0
while n>1:
    if x <(2**n)/2 and y<(2**n)/2:
        # print("2사분면")
        pass

    elif x<(2**n)/2 and y >= (2**n)/2:
        # print("1사분면")
        # result = result + 16
        cnt += ((2**n)/2)**2
        y -=(2**n)/2

    elif x >= (2**n)/2 and y <(2**n)/2:
        # print("3사분면")
        # result = result + 16 * 2
        cnt += ((2**n)/2)**2*2
        x -= (2**n)/2

    elif x >= (2**n)/2 and y >=(2**n)/2:
        # print("4사분면")
        # result = result + 16 * 3
        cnt += ((2**n)/2)**2*3
        x -=(2**n)/2
        y -=(2**n)/2

    n -=1

if x ==0 and y == 0:
    print(int(cnt))
elif x ==0 and y == 1:
    print(int(cnt+1))
elif x ==1 and y == 0:
    print(int(cnt+2))
elif x ==1 and y == 1:
    print(int(cnt+3))