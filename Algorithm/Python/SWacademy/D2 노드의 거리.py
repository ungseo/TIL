import sys

sys.stdin = open('input.txt', 'r')
from collections import deque


def bfs(y, s):
    q = deque()
    q.append((y, s))
    while q:
        nowy, step = q.popleft()
        if nowy == g - 1:
            return step
        for i in range(v):
            if used[i] == 1:
                continue
            if arr[nowy][i] == 1:
                q.append((i, step + 1))
    return 0

T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    arr = [[0] * v for i in range(v)]
    used = [0] * v
    minD = []

    for i in range(e):
        a, b = map(int, input().split())
        arr[a - 1][b - 1] = 1
        arr[b - 1][a - 1] = 1
    s, g = map(int, input().split())
    rst = bfs(s - 1, 0)

    print(f'#{tc} {rst}')
