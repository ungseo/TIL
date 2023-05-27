import sys
from collections import deque
import copy

def burn():

    while fire_list:
        cy, cx, time = fire_list.popleft()

        for i in range(4):
            ny = cy + my[i]
            nx = cx + mx[i]

            if ny < 0 or nx < 0 or ny >= Y or nx >= X: continue
            if type(maze[ny][nx]) == int(): continue
            maze[ny][nx] = time
            fire_list.append((ny, nx, time + 1))






input = sys.stdin.readline


my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
Y, X = map(int, input().split())
maze = [list(input()) for _ in range(Y)]

# fire_check = copy.deepcopy(maze)

fire_list = deque()
jihun = 0
for i in range(Y):
    for j in range(X):
        if maze[i][j] == 'J':
            jihun = (i, j)
        elif maze[i][j] == 'F':
            fire_list.append((i, j, 1))
            maze[i][j] = 0

burn()

print(fire_list)
