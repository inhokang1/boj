list = range(2, 10000)
sosu_list = []
def sosu():
    for i in list:
        if i==2 or i==3:
            sosu_list.append(i)
            continue
        else:    
            for j in range(2, int(i**0.5)+1):
                if i%j==0:
                    break
            else: sosu_list.append(i)  
   
# 골든바흐 수 구하기
def goldbach(n):
    k = n/2
    while True:
        if k in sosu_list and (n-k) in sosu_list:
            print(int(k), int(n-k))
            break
        else:
            k-=1


if __name__ == "__main__":
    sosu()
    test = int(input())
    for i in range(test):
        num = int(input())
        goldbach(num)