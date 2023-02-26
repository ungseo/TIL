def swing(y,x):
    fly = 0
    for i in range(m):
        for j in range(m):
            fly += lst[i+y][j+x]
    return fly

T = int(input())

for tc in range(1, T+1):
    n, m = map(int,input().split())

    lst = [list(map(int,input().split())) for _ in range(n)]

    max_kill = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            rst = swing(i, j)
            if max_kill < rst:
                max_kill = rst
    print(f'#{tc} {max_kill}')
