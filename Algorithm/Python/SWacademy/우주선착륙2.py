import sys
sys.stdin = open('input.txt','r')

def land(y,x):
    movey=[-1,0,1,0,-1,1,1,-1]
    movex=[0,1,0,-1,1,1,-1,-1]
    cnt = 0
    for i in range(8):
        ny = y + movey[i]
        nx = x + movex[i]
        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] < arr[y][x]:
                cnt += 1
    if cnt >= 4:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1,T+1):
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    can = 0
    for i in range(n):
        for j in range(m):
            can += land(i,j)

    print(f'#{tc} {can}')
