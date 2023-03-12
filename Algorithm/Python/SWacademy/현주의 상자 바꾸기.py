T = int(input())

for tc in range(1, T+1):
    n, q = map(int,input().split())
    lst = [0] * n
    num = 1
    for _ in range(q):
        l, r = map(int,input().split())
        for i in range(l-1,r):
            lst[i] = num

        num += 1

    print(f'#{tc}',end=' ')
    print(*lst)