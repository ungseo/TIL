import sys

input = sys.stdin.readline


def dfs(level, idx):
    global flag
    if flag == 1:
        return


    for i in range(n):
        if used[i] == 1: continue
        if arr[idx][i] == 0: continue
        if level == 4:
            flag = 1
            return
        used[i] = 1
        dfs(level + 1, i)
        used[i] = 0


n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]
used = [0] * n
flag = 0

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for i in range(n):
    if 1 in arr[i]:
        dfs(0, i)
    if flag == 1:
        break

print(flag)
