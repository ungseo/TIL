from collections import deque

#
# world = [[0, 0, 0, 0, 1],
#          [1, 0, 1, 0, 1],
#          [1, 0, 1, 0, 0],
#          [2, 0, 0, 0, 3]]
#
# my = [-1, 0, 1, 0]
# mx = [0, 1, 0, -1]
# st = 0
# def bfs(y,x,step):
#     global st
#     q = deque()
#     q.append((y,x,step))
#     while q:
#         nowy, nowx, Ns = q.popleft()
#         if world[nowy][nowx] == 2:
#             if Ns < mineat:
#                 mineat = Ns
#
#         for i in range(4):
#             ny = nowy + my[i]
#             nx = nowx + mx[i]
#             if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
#             q.append((ny,nx,step+1))


def bfs(sty, stx):
    cnt = 1
    q = deque()
    q.append((sty, stx))
    island[sty][stx] = 0
    while q:
        nowy, nowx = q.popleft()

        for i in range(4):
            ny = nowy + my[i]
            nx = nowx + mx[i]
            if ny < 0 or nx < 0 or ny >= 5 or nx >= 5: continue
            if island[ny][nx] == 0 : continue
            island[ny][nx] = 0
            cnt += 1
            q.append((ny,nx))
    if cnt == 0:
        return 1
    else:
        return cnt

island = [[0, 0, 1, 0, 1],
          [0, 0, 1, 0, 1],
          [0, 1, 1, 1, 0],
          [0, 0, 1, 0, 0],
          [1, 0, 0, 1, 1]]
my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
island_data = []
for i in range(5):
    for j in range(5):
        if island[i][j] == 1:
            island_data.append(bfs(i,j))

print(f'{len(island_data)}, {max(island_data)}, {min(island_data)}')

