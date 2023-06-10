import sys
input = sys.stdin.readline

n = int(input())
cnt = n

for i in range(n):
    word = input().rstrip()
    for j in range(len(word)-1):

        a = word[j]
        b = word[j+1]
        
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -=1
            break

print(cnt)



    