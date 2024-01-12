n = int(input())
data = list(map(int, input().split()))
count = 0

for x in data:
    if x>1 :
      for i in range(2, x+1):
        if x % i == 0:
          if x == i:
            count += 1
          
          break

print(count)