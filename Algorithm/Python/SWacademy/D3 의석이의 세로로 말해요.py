import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    lst = [list(input()) for _ in range(5)]
    print(f'#{tc}', end=' ')
    for i in range(15):
        for j in range(5):
            try:
                print(lst[j][i], end='')

            except:
                continue
    print()
