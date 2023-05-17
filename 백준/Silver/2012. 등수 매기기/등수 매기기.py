import sys
input = sys.stdin.readline

#사람수
n = int(input())

#예상 등수 리스트로 받기
a = []
for _ in range(n):
    a.append(int(input()))
#등수 정렬
a.sort()

#정렬된 리스트에서 각 숫자들이 자기숫자와 index+1 이 틀리다면 
# 차이 만큼의 절대값을 cnt에 저장
cnt = 0
for i in range(len(a)):
    if a[i] == i+1:
        continue
    else:
        b = a[i] - (i+1)
        cnt += abs(b)

print(cnt)
