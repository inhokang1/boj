import sys
input = sys.stdin.readline

N,K = map(int,input().split())
products = list(map(int,input().split()))

concents = []
cnt = 0

for i in range(K):
    if products[i] in concents:
        continue
    
    if len(concents) < N:
        concents.append(products[i])
        continue

    products_idxs = []
    stop_point = True

    for j in range(N):
        if concents[j] in products[i:]:
            products_idx = products[i:].index(concents[j])
            
        else:
            products_idx = 101
            stop_point = False

        products_idxs.append(products_idx)

        if stop_point == False:
            break

    concent_out = products_idxs.index(max(products_idxs))
    del concents[concent_out]
    concents.append(products[i])
    cnt += 1

print(cnt)