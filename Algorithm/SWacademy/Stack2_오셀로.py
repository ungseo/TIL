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
        x -= 1
        y -= 1
        for dr in range(8):
            ny = y + movy[dr]
            nx = x + movx[dr]
            flag = 1
            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            if pan[ny][nx] == 0: continue
            if pan[ny][nx] != player:
                while pan[ny][nx] != 0 or pan[ny][nx] == player:
                    ny += movy[dr]
                    nx += movx[dr]
                    if 0 <= ny < n and 0 <= nx < n:
                        if player == 1 and pan[ny][nx] == player:
                            while 1:
                                ny -= movy[dr]
                                nx -= movx[dr]
                                pan[ny][nx] = player
                                if y == ny and x == nx:
                                    flag = 0
                                    break
                        if flag == 0:
                            break
                        elif player == 2 and pan[ny][nx] == player:
                            while 1:
                                ny -= movy[dr]
                                nx -= movx[dr]
                                pan[ny][nx] = player
                                if y == ny and x == nx:
                                    flag = 0
                                    break
                        if flag == 0:
                            break
                    else: break

    black = 0
    white = 0
    for i in range(n):
        for j in range(n):
            if pan[i][j] == 1:
                black += 1
            elif pan[i][j] == 2:
                white += 1

    print(f'#{tc} {black} {white}')

