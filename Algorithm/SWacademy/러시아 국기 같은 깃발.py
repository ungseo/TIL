def johap(level):
    global minC, cnt
    if level == n - 2:
        if cnt < minC:
            minC = cnt
        return

    for i in range(3):
        if level == 0 and i == 2: continue
        if level == n - 3 and i == 0: continue
        if level > 0:
            if path[level - 1] == 'W' and color[i] == 'R': continue
            if path[level - 1] == 'B' and color[i] == 'W': continue
            if path[level - 1] == 'R' and color[i] == 'W': continue
            if path[level - 1] == 'R' and color[i] == 'B': continue

        path[level] = color[i]
        temp = 0
        for j in range(m):
            if Flag[level+1][j] != color[i]:
                temp += 1
        cnt += temp
        if cnt > minC:
            return
        johap(level+1)
        cnt -= temp

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    Flag = [list(input()) for _ in range(n)]
    path = [0] * (n - 2)
    color = ['W','B','R']
    cnt = 0
    cng_cnt = 0
    minC = 21e8

    johap(0)

    for i in Flag[0]:
        if i != 'W':
            cng_cnt += 1
    for i in Flag[n - 1]:
        if i != 'R':
            cng_cnt += 1

    print(f'#{tc} {minC+cng_cnt}')


