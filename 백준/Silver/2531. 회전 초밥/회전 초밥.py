import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
sushi = []
check = []
cp1,cp2 = 0, k-1
for _ in range(n):
    sushi.append(int(input()))

while cp1 < n:
    if cp2 > n:
        cp2 -= n
    if cp2 < cp1:
        plates = sushi[cp1:]+sushi[:cp2+1]
    else:
        plates = sushi[cp1:cp2+1]
    case = set(plates)
    if c not in case:
        case.add(c)
    if len(case) > len(check):
        check = case
    
    cp1 +=1
    cp2 +=1
print(len(check))
