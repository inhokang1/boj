from sys import stdin as s


#테스트케이스
T = int(s.readline().rstrip())

for i in range(T):
    #동전 가지 수
    N = int(s.readline().rstrip())

    #동전 종류
    coins = list(map(int, s.readline().rstrip().split()))

    #얼마?
    M = int(s.readline().rstrip())

    dp = [0] * (M+1)
    dp[0] = 1
    
    for coin in coins:
        for j in range(1,M+1):
            if j>= coin:
                dp[j] += dp[j-coin]

    print(dp[M])