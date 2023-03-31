def bfs(y, x):
    q = []
    q.append((y, x, 0))

    while q:
        nowy, nowx, step = q.pop(0)
        if nowy == edy and nowx == edx:
            ans.append(step)

        for i in range(4):
            ny = nowy + movy[i]
            nx = nowx + movx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if maze[ny][nx] == 1: continue
                q.append((ny, nx, step + 1))
                maze[ny][nx] = 1


movy = [-1, 0, 1, 0]
movx = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, list(input()))) for _ in range(n)]
    ans = []
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 0: continue
            if maze[i][j] == 1: continue
            if maze[i][j] == 2:
                sty, stx = i, j
            else:
                edy, edx = i, j
    bfs(sty, stx)
    if ans:
        print(f'#{tc} {ans[0] -1 }')
    else:
        print(f'#{tc} 0')