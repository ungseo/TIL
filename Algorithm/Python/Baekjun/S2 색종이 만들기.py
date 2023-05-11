import sys

input = sys.stdin.readline


def check(y, x, size):
    cnt = 0
    for i in range(size):
        for j in range(size):
            if paper[i+y][x+j] == 0: return 0
            cnt += 1
    if cnt == size ** 2:
        for i in range(size):
            for j in range(size):
                paper[y+i][x+j] = 0
        return 1

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

small_paper = 0
x = N
while x != 0:
    for i in range(0, N, x):
        for j in range(0, N, x):
            if paper[i][j] == 1:
                small_paper += check(i, j, x)
    x //= 2

print(small_paper)
