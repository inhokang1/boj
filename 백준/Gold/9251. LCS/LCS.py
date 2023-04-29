import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
len1 = len(word1)
len2 = len(word2)
#메모이제이션 리스트
dp = [[0]*(len2+1) for _ in range(len1+1)]

#글자 하나씩 서로 비교
for i in range(1,len1+1):
    for j in range(1,len2+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else :
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

#가장 큰 값 print
print(dp[-1][-1])