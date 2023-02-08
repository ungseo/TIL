import sys
sys.stdin = open('input.txt','r')

T = 10


for tc in range(1,T+1):
    dump = int(input())
    h = list(map(int,input().split()))
    DAT = [0 for i in range(101)]
    
    def maxH():
        for i in range(100,0,-1):
            if DAT[i] !=0 :
                return i
        
    def minH():
        for i in range(1,101):
            if DAT[i] != 0:
                return i
    
    for i in h:
        DAT[i] += 1
    
    for i in range(dump):
        high = maxH()
        low = minH()
        
        DAT[high] -= 1
        DAT[high-1] += 1
        DAT[low] -= 1
        DAT[low+1] += 1
        
    print(f'#{tc} {maxH()-minH()}')
    
