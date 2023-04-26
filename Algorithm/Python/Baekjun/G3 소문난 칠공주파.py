import sys

input = sys.stdin.readline


def dfs(y, x, level, Y):
    global path, cnt
    used[y][x] = 1
    path[level] = (y, x)
    if Y == 4:
        return
    if level == 6:
        path.sort(key=lambda x: x[0])
        if path not in ans:
            ans.append(path)
            cnt += 1
            print(path)
        path = [0] * 7
        return
1100
1010
----
0110


    for i in range(4):
        ny = y + my[i]
        nx = x + mx[i]
        if ny < 0 or nx < 0 or ny > 4 or nx > 4: continue
        if used[ny][nx] == 1: continue
        if seat[ny][nx] == 'Y':
            dfs(ny, nx, level + 1, Y + 1)
        else:
            dfs(ny, nx, level + 1, Y)
        used[ny][nx] = 0
        path[level + 1] = 0


cnt = 0
my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
seat = [list(input().rstrip()) for _ in range(5)]
path = [0] * 7
ans = []

for i in range(5):
    for j in range(5):
        used = [[0] * 5 for _ in range(5)]
        if seat[i][j] == 'Y':
            dfs(i, j, 0, 1)
        else:
            dfs(i, j, 0, 0)



print(cnt)