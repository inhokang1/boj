from string import ascii_lowercase

arpha = list(input())
arpha_list = list(ascii_lowercase)
check_list = [0]*26

for i in range(len(arpha)):
    if arpha[i] in arpha_list:
        a = arpha_list.index(arpha[i])
        check_list[a] += 1

for i in range(len(check_list)):
    print(check_list[i], end= " ")