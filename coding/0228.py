#
# def make_team(level):
#     global minP,total_power
#     if level == 6:
#         sum = 0
#         for i in range(7):
#             if bit[i] == 1:
#                 sum += power[i]
#         if abs(total_power-2*sum) < minP:
#             minP = abs(total_power-2*sum)
#         return
#
#     for i in range(2):
#         bit[level] = i
#         make_team(level+1)
#         bit[level] = 0
#
#
# lst = ['a','b','c','d','e','f','g']
# power = [49,6,54,80,3,18,71]
# bit = [0,0,0,0,0,0,0]
# total_power = sum(power)
# minP = 21e8
# make_team(0)
#
# print(minP)
#

# def go(y,x):
#     if y == 3 and x == 3:
#         print('가능')
#         return 1
#
#
#     for i in range(4):
#         ny = y + movy[i]
#         nx = x + movx[i]
#
#         if 0 <= ny < 4 and 0 <= nx < 4:
#             if maze[ny][nx] == 0:
#                 maze[ny][nx] = 1
#                 go(ny,nx)
#
# movy = [-1, 0, 1, 0]
# movx = [0, 1, 0, -1]
#
# maze = [[0, 0, 0, 0],
#         [1, 0, 1, 0],
#         [1, 0, 1, 0],
#         [0, 0, 0, 0]]
# maze[0][0] = 1
# go(0,0)
#
#























