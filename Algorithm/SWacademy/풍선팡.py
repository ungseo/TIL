import sys

sys.stdin = open('input.txt', 'r')


def Pop(y, x, rg):
    sum = arr[y][x]
    for i in range(4):
        for dr in range(1, rg + 1):
            ny = y + movy[i] * dr
            nx = x + movx[i] * dr
            if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
            sum += arr[ny][nx]
    return sum


movy = [-1, 0, 1, 0]
movx = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    maxP = 0
    for i in range(n):
        for j in range(m):
            rst = Pop(i, j, arr[i][j])
            if rst > maxP:
                maxP = rst

    print(f'#{tc} {maxP}')
