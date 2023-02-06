lst = [list(map(int, input().split())) for _ in range(5)]
di=[-1,-1,-1,0,0,1,1,1]
dj=[-1,0,1,-1,1,-1,0,1]
def ans(a,b):
    for i in range(8):
        dy=a+di[i]
        dx=b+dj[i]
        if 0<=dy<5 and 0<=dx<4:
            if lst[dy][dx]!=0:
                return 0
    return 1

cnt=0
for i in range(5):
    for j in range(4):
        if lst[i][j]==1:
            ret=ans(i,j)
            if ret==0:
                cnt+=1
if cnt==0:
    print('안정')
else:
    print('불완전')