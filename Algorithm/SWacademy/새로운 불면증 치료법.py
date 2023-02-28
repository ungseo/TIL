T = int(input())
for tc in range(1, T + 1):
    nlst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = int(input())
    m = 0
    while nlst:
        m += 1
        num = list(map(int,map(str,str(n*m))))
        for i in range(len(num)):
            if num[i] in nlst:
                nlst.remove(num[i])

    print(f'#{tc} {m*n}')
