import sys

input = sys.stdin.readline


def spread_sand(y, x, d):
    global total_sand
    # 보는 방향으로 2칸 먼저하기
    tempS = desert[y][x]
    restS = desert[y][x]
    dr = d

    # 보는곳에서 왼쪽방향으로 2칸
    dr += 1
    dr %= 4
    for i in range(1, 3):
        ny = y + my[dr] * i
        nx = x + mx[dr] * i
        if i == 1:
            sand = int(tempS * 0.07)
        if i == 2:
            sand = int(tempS * 0.02)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand
            continue
        desert[ny][nx] += sand
        restS -= sand
    # 보는곳에서 오른쪽으로 2칸
    dr += 2
    dr %= 4
    for i in range(1, 3):
        ny = y + my[dr] * i
        nx = x + mx[dr] * i
        if i == 1:
            sand = int(tempS * 0.07)
        if i == 2:
            sand = int(tempS * 0.02)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand
            continue
        desert[ny][nx] += sand
        restS -= sand

    # 원래방향 대각선 설정

    if d == 0:
        ny = y + 1
        nx = x - 1
        sand = int(tempS * 0.1)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand
        else:
            desert[ny][nx] += sand
            restS -= sand


        ny = y - 1
        nx = x - 1
        sand = int(tempS * 0.1)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


        ny = y - 1
        nx = x + 1
        sand = int(tempS * 0.01)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


        ny = y + 1
        nx = x + 1
        sand = int(tempS * 0.01)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


    #아랫방향일때
    elif d == 1:
        ny = y - 1
        nx = x - 1
        sand = int(tempS * 0.1)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


        ny = y - 1
        nx = x + 1
        sand = int(tempS * 0.1)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


        ny = y + 1
        nx = x + 1
        sand = int(tempS * 0.01)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


        ny = y + 1
        nx = x - 1
        sand = int(tempS * 0.01)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


    # 오른쪽 방향일때
    elif d == 2:
        ny = y - 1
        nx = x + 1
        sand = int(tempS * 0.1)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


        ny = y + 1
        nx = x + 1
        sand = int(tempS * 0.1)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


        ny = y + 1
        nx = x - 1
        sand = int(tempS * 0.01)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


        ny = y - 1
        nx = x - 1
        sand = int(tempS * 0.01)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


    # 윗방향일때
    else:
        ny = y + 1
        nx = x - 1
        sand = int(tempS * 0.1)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


        ny = y + 1
        nx = x + 1
        sand = int(tempS * 0.1)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


        ny = y - 1
        nx = x + 1
        sand = int(tempS * 0.01)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand


        ny = y - 1
        nx = x - 1
        sand = int(tempS * 0.01)
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            restS -= sand

        else:
            desert[ny][nx] += sand
            restS -= sand

    ny = y + my[d] * 2
    nx = x + mx[d] * 2
    sand = int(tempS * 0.05)
    if ny < 0 or nx < 0 or ny >= N or nx >= N:
        if sand >= 1:
            restS -= sand
    else:
        desert[ny][nx] += sand
        restS -= sand

    ny = y + my[d]
    nx = x + mx[d]
    if ny < 0 or nx < 0 or ny >= N or nx >= N:
        pass
    else:
        desert[ny][nx] += restS

    # for i in range(1, 3):
    #     ny = y + my[dr] * i
    #     nx = x + mx[dr] * i
    #     if i == 1:
    #         sand = int(tempS * 0.55)
    #     if i == 2:
    #         sand = int(tempS * 0.05)
    #     if ny < 0 or nx < 0 or nx >= N or ny >= N:
    #         total_sand += sand + 1
    #         continue
    #     if i == 1:
    #         desert[ny][nx] += sand
    #     else:
    #         desert[ny][nx] += sand
    desert[y][x] = 0


total_sand = 0

my = [0, 1, 0, -1] # 좌 하 우 상
mx = [-1, 0, 1, 0]
N = int(input())
desert = [list(map(int, input().split())) for _ in range(N)]
sy, sx = N // 2, N // 2

d = 0
cnt = 1
flag = 1
while 1:
    for i in range(2):
        for j in range(cnt):
            sy = sy + my[d]
            sx = sx + mx[d]
            if sy < 0 or sx < 0 or sy >= N or sx >= N:
                flag = 0
                break

            if desert[sy][sx] == 0: continue
            spread_sand(sy, sx, d)
        d = (d+1) % 4
        if flag == 0:
            break
    if flag == 0:
        break
    cnt += 1

rst = 0
for i in range(N):
    rst += sum(desert[i])
    print(*desert[i])
print(rst)
