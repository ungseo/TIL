
T = int(input())

for tc in range(1,T+1):
    N,M =list(map(int,input().split()))
    
    lst = list(map(int,input().split()))
    
    temp = []
    
    def getsum(stn):
        sum = 0 
        for i in range(M):
            sum += lst[stn]
            stn += 1
        return sum
    for i in range(N-M+1):
        temp.append(getsum(i))
        
    minV = temp[0]
    maxV = temp[0]
    
    for i in range(len(temp)):
        if minV > temp[i]:
            minV = temp[i]
        if maxV < temp[i]:
            maxV = temp[i]
        
    print(f'#{tc} {maxV-minV}')
        
    