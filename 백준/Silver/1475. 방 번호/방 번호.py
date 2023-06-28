
num_list = [0]*10
num = list(input())

for i in num:
    a = int(i)
    if a == 6 or a == 9:
        if num_list[6] <= num_list[9]:
            num_list[6] += 1
        else:
            num_list[9] +=1
    else:
        num_list[a] +=1

print(max(num_list))