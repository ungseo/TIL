# lst = [[3,5,9],
#        [7,-8,1],
#        [-10,2,3],
#        [5,1,2]]
# maxV = 0
# def bfs(level, gop):
#     global maxV
#     if level == 4:
#         if maxV < gop:
#             maxV = gop
#         return
#
#     for i in range(3):
#         bfs(level+1, gop * lst[level][i])
#
# bfs(0,1)
# print(maxV)
#

# arr = [[3,5,9,6],
#        [7,-8,1,6],
#        [-10,2,3,9],
#        [5,1,2,8],
#        [4,7,1,8]]
#
#
# cnt = 0
# def bfs(level,sum):
#     global cnt,can
#     if level == 5:
#         if sum > 30:
#             cnt += 1
#         return

# cnt = 0
# def dfs2(now,level,sum):
#     global cnt
#     if level == 5:
#         if sum > 30:
#             cnt += 1
#         return
#     for i in range(3):
#         direct = [-1,0,1]
#         dy = level
#         dx = now+direct[i]
#         if dx < 0 or dx > 3: continue
#         dfs2(dx,level+1,sum+arr[dy][dx])
# for i in range(4):
#     dfs2(i,0,0)
# print(cnt)

# map = [[0,0,0,0],
#        [1,0,1,0],
#        [1,0,1,0],
#        [0,0,1,0]]
#
# used = [[1,0,0,0],
#        [0,0,0,0],
#        [0,0,0,0],
#        [0,0,0,0]]
#
# movey = [-1,0,1,0]
# movex = [0,1,0,-1]
# flag = 0
# def move(y,x):
#     global flag
#     if y == 3 and x == 3:
#         map[3][3] = 100
#
#     for i in range(4):
#         ny = y + movey[i]
#         nx = x + movex[i]
#         if 0 <= ny <= 3 and 0 <= nx <= 3:
#             if map[ny][nx] == 1:
#                 continue
#             if used[ny][nx] == 1:
#                 continue
#             used[ny][nx] = 1
#             move(ny, nx)
#             used[ny][nx] = 0
#
#         else:
#             continue
#
# move(0,0)
# if map[3][3] == 100:
#     print('가능')
# else:
#     print('불가능')

##

map = [[0,0,0,0,1],
       [1,0,1,'ed',1],
       [1,0,1,0,1],
       [1,0,1,0,1],
       [0,0,0,0,0]]

used = [[1,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]


my = [1,-1,0,0]
mx = [0,0,-1,1]
minC = 21e8
def go(y,x,cnt):
    global minC
    if map[y][x] == 'ed':
        if minC > cnt:
            minC = cnt
        return

    for i in range(4):
        ny = y + my[i]
        nx = x + mx[i]
        if ny > 4 or ny < 0 or nx > 4 or nx < 0: continue
        if map[ny][nx] == 1: continue
        if used[ny][nx] == 1: continue
        used[ny][nx] = 1
        go(ny,nx,cnt+1)
        used[ny][nx] = 0

go(0,0,0)

print(minC)





[0,0,1,1,0]
[1,0,0,0,0]
[1,0,1,0,0]
[1,0,1,1,0]
[1,0,0,1,e]

















