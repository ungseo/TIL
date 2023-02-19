import sys
sys.stdin = open('input.txt','r')
def oselo(y,x,dir,player,step):
    if step > 0 and pan[y][x] == player:
        direction[dir] = 0
        return
    if step == 0:
        pan[y][x] = player
    ny = y + movy[dir]
    nx = x + movx[dir]
    if step == 0:
        direction[dir] = 1
    if direction[dir] == 0:
        return
    if 0 <= ny < n and 0 <= nx < n:
            if pan[ny][nx] == 0:
                direction[dir] = 0
                return
            else:
                oselo(ny,nx,dir,player,step+1)
            if player == 1:
                pan[ny][nx] = 1
            else:
                pan[ny][nx] = 2



T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    pan = [[0] * n for _ in range(n)]
    pan[n//2-1][n//2-1], pan[n//2][n//2] = 2, 2
    pan[n//2-1][n//2], pan[n//2][n//2-1] = 1, 1 ## 흰색은 2 흑색은 1

    direction = [0] * 8
    movy = [-1, 0, 1, 0, -1, 1, 1, -1]
    movx = [0, 1, 0, -1, 1, 1, -1, -1]

    for _ in range(m):
        x, y, player = map(int,input().split())
        for i in range(8):
            oselo(y-1, x-1, i, player, 0)

    print(f'#{tc}')
    print(pan, sep=' ')

