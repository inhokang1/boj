arr = input().lower()
arr_list = list(set(arr))
cnt = []

for i in arr_list:
    count = arr.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >=2:
    print("?")
else:
    print(arr_list[(cnt.index(max(cnt)))].upper())
