def cycle():
    global flag
    for i in range(n):
        if cook[i] != 0:
            cook[i][1] //= 2
            if cook[i][1] == 0:
                cook[i] = 0
            if not cs and cook.count(0) == n-1:
                for i in range(n):
                    if cook[i] == 0: continue
                    flag = 0
                    print(f'#{tc} {cook[i][0]+1}')
                    return

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    cs = list(map(int, input().split()))
    cook = [0] * n
    for i in range(len(cs)):
        cs[i] = [i, cs[i]]

    for i in range(n):
        cook[i] = cs.pop(0)
    flag = 1
    while 1:
        if flag == 0:
            break
        cycle()


        while 0 in cook and cs:
            for i in range(n):
                if cook[i] == 0 and cs:
                    cook[i] = cs.pop(0)
                elif not cs:
                    break
        # if cook.count(0) == n-1:
        #     for i in range(n):
        #         rst = cook.pop(0)
        #         if rst == 0: continue
        #         else:
        #             print(f'#{tc} {rst[0]}')