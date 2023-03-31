import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    ans = []
    n, m, l = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        ans.append([a, b])
    # ans.append([0, 0])
    ans.sort(reverse=True)
    if ans[0][0] % 2 == 0:
        a, b = ans.pop(0)
        if a == l:
            print(f'#{tc} {b}')
            break
        ans.append([a // 2, b])
        while 1:
            a, b = ans.pop(0)
            if a == l:
                print(f'#{tc} {b}')
                break
            c, d = ans.pop(0)
            if c == l:
                print(f'#{tc} {d}')
                break
            ans.append([a // 2, b + d])
    else:
        while 1:
            a, b = ans.pop(0)
            if a == l:
                print(f'#{tc} {b}')
                break
            c, d = ans.pop(0)
            if c == l:
                print(f'#{tc} {d}')
                break
            ans.append([a // 2, b + d])
