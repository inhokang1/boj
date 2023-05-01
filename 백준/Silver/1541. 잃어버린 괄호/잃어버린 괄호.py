from sys import stdin as s

arr = s.readline().rstrip().split("-")

cnt = 0

for i in arr[0].split("+"):
    cnt += int(i)

for i in arr[1:]:
    for j in i.split("+"):
        cnt -= int(j)

print(cnt)
