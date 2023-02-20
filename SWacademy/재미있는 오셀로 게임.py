import sys
sys.setrecursionlimit(10**6)
def go(x, y):
    if pan[y][x] == color:
        return
    if 0 <= x < n and 0 <= y < n:
        ny = y + movy[dr]
        nx = x + movx[dr]
        if 0 <= nx < n and 0 <= ny < n:
            if pan[ny][nx] != 0:
                go(ny, nx)
                if color == 1:
                    pan[y][x] = 1
                else:
                    pan[y][x] = 2

movy = [-1,0,1,0,-1,1,1,-1]
movx = [0,1,0,-1,1,1,-1,-1]

T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    pan = [[0 for i in range(n)] for j in range(n)]
    # 가운데 채우기
    for i in range(2):
        pan[n // 2 - 1 + i][n // 2 - 1 + i] = 2
    for i in range(2):
        pan[n // 2 - 1 + i][n // 2 - i] = 1
    for play in range(m):
        x, y, color = map(int,input().split())
        x -= 1
        y -= 1
        # 탐색하기
        for dr in range(8):
            ny = y + movy[dr]
            nx = x + movx[dr]
            if 0 <= ny < n and 0 <= nx < n and pan[ny][nx] > 0:
                if color != pan[ny][nx]: # 흑돌
                    go(nx,ny)
        pan[y][x] = color

    print(pan, sep=' ')