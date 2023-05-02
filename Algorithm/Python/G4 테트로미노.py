import sys

input = sys.stdin.readline

n, m = map(int, input().split())

tetris = [list(map(int, input().split())) for _ in range(n)]
maxSum = 0

# 가로긴거
for i in range(n):
    for j in range(m - 3):
        tsum = 0
        tsum += tetris[i][j] + tetris[i][j + 1] + tetris[i][j + 2] + tetris[i][j + 3]
        if maxSum < tsum:
            maxSum = tsum
# 세로긴거
for j in range(m):
    for i in range(n - 3):
        tsum = 0
        tsum += tetris[i][j] + tetris[i + 1][j] + tetris[i + 2][j] + tetris[i + 3][j]
        if maxSum < tsum:
            maxSum = tsum
# 정사각형

for i in range(n - 1):
    for j in range(m - 1):
        tsum = 0
        tsum += tetris[i][j] + tetris[i + 1][j] + tetris[i][j + 1] + tetris[i + 1][j + 1]
        if maxSum < tsum:
            maxSum = tsum

# 뻐큐 위아래
for i in range(n):
    for j in range(m - 2):
        tsum = 0
        if i != n - 1:
            tsum += tetris[i][j] + tetris[i][j + 1] + tetris[i][j + 2] + tetris[i + 1][j + 1]
            if maxSum < tsum:
                maxSum = tsum
        else:
            tsum += tetris[i][j] + tetris[i][j + 1] + tetris[i][j + 2] + tetris[i - 1][j + 1]
            if maxSum < tsum:
                maxSum = tsum
            continue
        if i != 0:
            tsum1 = tsum - tetris[i + 1][j + 1] + tetris[i - 1][j + 1]
            if maxSum < tsum1:
                maxSum = tsum1

# 뻐큐 오른쪽
for i in range(n - 2):
    for j in range(m - 1):
        tsum = 0
        tsum += tetris[i][j] + tetris[i + 1][j] + tetris[i + 2][j] + tetris[i + 1][j + 1]
        if maxSum < tsum:
            maxSum = tsum

# 뻐큐 왼쪽
for i in range(n - 2):
    for j in range(1, m):
        tsum = 0
        tsum += tetris[i + 1][j - 1] + tetris[i][j] + tetris[i + 1][j] + tetris[i + 2][j]
        if maxSum < tsum:
            maxSum = tsum

            


print(maxSum)
