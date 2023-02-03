def getsum(stn):
        sum = 0 
        for i in range(N-M+1):
            sum += lst[stn]
            stn += 1
        return sum


N=5
M=3     
lst = [1,2,3,4,5]

print(getsum(1))
