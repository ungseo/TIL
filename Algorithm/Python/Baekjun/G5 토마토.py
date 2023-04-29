# import sys
#
# input = sys.stdin.readline
#
# def check(y, x, f, day):
#     global min_D
#     for i in range(4):
#         ny = y + mvy[i]
#         nx = x + mvx[i]
#         if ny < 0 or nx < 0 or ny >= M or nx >= N: continue
#         if tomato[f][ny][nx] != 0: continue
#         tomato[f][ny][nx] = day
#         min_D = day - 1
#
#     if f+1 < H and tomato[f+1][y][x] == 0:
#         tomato[f+1][y][x] = day
#         min_D = day - 1
#
#     if f-1 >= 0 and tomato[f-1][y][x] == 0:
#         tomato[f-1][y][x] = day
#         min_D = day - 1
#
#
#
# N, M, H = map(int, input().split())
# tomato = []
# ans = 0
# mvy = [-1, 0, 1, 0]
# mvx = [0, 1, 0, -1]
#
# ck = 0
# for h in range(H):
#     temp = []
#     for i in range(M):
#         a = list(map(int, input().split()))
#         temp.append(a)
#         if 0 not in a:
#             ck += 1
#     tomato.append(temp)
# if ck == M * H:
#     print(0)
#
# else:
#     n = 0
#     min_D = 99999
#     while 1:
#         n += 1
#         cnt = 0
#         for h in range(H):
#             for i in range(M):
#                 for j in range(N):
#                     if tomato[h][i][j] == n:
#                         check(i, j, h, n + 1)
#
#                     else:
#                         cnt += 1
#         if cnt == H * M * N:
#             break
#     flag = 0
#     for h in range(H):
#         for i in range(M):
#             for j in range(N):
#                 if tomato[h][i][j] == 0:
#                     flag = 1
#                     break
#         if flag == 1:
#             break
#
#     if flag == 0:
#         print(min_D)
#     else:
#         print(-1)
#


import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    while q:
        global day
        nowy, nowx, nowf, nowd = q.popleft()
        day = nowd
        for i in range(4):
            ny = nowy + mvy[i]
            nx = nowx + mvx[i]
            if ny < 0 or nx < 0 or ny >= M or nx >= N: continue
            if tomato[nowf][ny][nx] == 0:
                tomato[nowf][ny][nx] = nowd + 1
                q.append((ny, nx, nowf, nowd + 1))

        if nowf + 1 < H and tomato[nowf + 1][nowy][nowx] == 0:
            tomato[nowf + 1][nowy][nowx] = nowd + 1
            q.append((nowy, nowx, nowf + 1, nowd + 1))
        if nowf - 1 >= 0 and tomato[nowf - 1][nowy][nowx] == 0:
            tomato[nowf - 1][nowy][nowx] = nowd + 1
            q.append((nowy, nowx, nowf - 1, nowd + 1))


mvy = [-1, 0, 1, 0]
mvx = [0, 1, 0, -1]
N, M, H = map(int, input().split())
tomato = []
cnt = 0
for h in range(H):
    temp = []
    for i in range(M):
        a = list(map(int, input().split()))
        temp.append(a)
        if 0 not in a:
            cnt += 1
    tomato.append(temp)

if cnt == M * H:
    print(0)

else:
    q = deque()
    day = 0
    flag = 0
    for h in range(H):
        for i in range(M):
            for j in range(N):
                if tomato[h][i][j] == 1:
                    q.append((i, j, h, 1))
                    flag = 1
    bfs()

    if flag == 1:

        for h in range(H):
            for i in range(M):
                if 0 in tomato[h][i]:
                    print(-1)
                    flag = 0
                    break
            if flag == 0:
                break
        if flag == 1:
            print(day - 1)
    else:
        print(-1)