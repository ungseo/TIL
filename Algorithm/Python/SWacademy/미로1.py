def go(y, x):
    global flag
    for i in range(4):
        ny = y + movy[i]
        nx = x + movx[i]
        if 0 <= ny < 16 and 0 <= nx < 16:
            if maze[ny][nx] == 1: continue
            if ny == endy and nx == endx:
                flag = 1
                return
            maze[ny][nx] = 1  ## 예외 : 시작지점 처리안함 그냥함
            go(ny, nx)


movy = [-1, 0, 1, 0]
movx = [0, 1, 0, -1]
for i in range(1, 11):
    tc = int(input())
    maze = [list(map(int, map(str, input()))) for _ in range(16)]
    flag = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                starty, startx = i, j
            if maze[i][j] == 3:
                endy, endx = i, j
    go(starty, startx)

    if flag == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')