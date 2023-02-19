def win_min(x):
    minV = 21e8
    for i in range(L):
        if minV > lst[x+i]:
            minV =lst[x+i]
    return minV

N, L  = map(int,input().split())
lst =list(map(int,input().split()))
D = [0] * N


for i in range(N-L+1):
    D[L-1+i]=win_min(i)

minV = 21e8
for i in range(L-1):
    if minV > lst[i]:
        minV = lst[i]

for i in range(L-1):
    D[i] = minV


print(*D)
    