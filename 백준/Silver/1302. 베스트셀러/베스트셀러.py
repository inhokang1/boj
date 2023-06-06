import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(n):
    a = input().rstrip()
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1

list = []
num = max(dic.values())

#max로 가장 많이 팔린 책의 갯수를 구했다면
# max 값과 동일한 갯수가 팔린 다른 책들이 있는지 for문을 돌려 dic 에서 찾는다
# 찾아서 list에 넣어준다
for i in dic:
    if num == dic[i]:
        list.append(i)


list.sort()
print(list[0])