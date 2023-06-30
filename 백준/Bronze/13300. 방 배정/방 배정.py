n, k = map(int, input().split())
st = [[0]*2 for _ in range(6)] #성별2개 6학년

#입력
for _ in range(n):
    # st[학년][성별]
    s,y= map(int, input().split())
    st[y-1][s-1] += 1

room = 0
for i in range(6):
    for j in range(2):
        if (st[i][j]%k == 0):
            room += st[i][j]/k
        else:
            room += st[i][j]//k+1
print(int(room))