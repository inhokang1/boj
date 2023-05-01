import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    rank = []
    for i in range(N):
        rank.append(list(map(int,input().split())))

    rank_sort = sorted(rank)

    top = 0
    result = 1

    for i in range(1,N):
        if rank_sort[i][1] < rank_sort[top][1]:
            result += 1
            top = i

    print(result)