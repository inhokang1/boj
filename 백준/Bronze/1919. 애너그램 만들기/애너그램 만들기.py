a = input()
b = input()
arr = [0]*26

for i in a:
    arr[ord(i)-97] += 1
for i in b:
    arr[ord(i)-97] -= 1

ans = 0
for i in arr:
    ans += abs(i)
print(ans)
