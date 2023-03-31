import sys
import copy

sys.stdin = open('input.txt', 'r')


def N_1down():
    for i in range(99, -1, -1):
        for j in range(100):
            if table[i][j] == 0: continue
            if table[i][j] == 2: continue
            if i == 99:
                if table[i][j] == 0: continue
                if table[i][j] == 2: continue
                table[i][j] = 0
            else:
                if table[i + 1][j] == 0:
                    table[i + 1][j] = 1
                    table[i][j] = 0


def S_2up():
    for i in range(100):
        for j in range(100):
            if table[i][j] == 0: continue
            if table[i][j] == 1: continue
            if i == 0:
                if table[i][j] == 0: continue
                if table[i][j] == 1: continue
                table[i][j] = 0
            else:
                if table[i - 1][j] == 0:
                    table[i - 1][j] = 2
                    table[i][j] = 0


# 바텀이 S 탑이 N// 1이면 아래로, 2면 위로 한칸
for tc in range(1, 11):
    dump = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]

    while 1:
        a = copy.deepcopy(table)
        N_1down()
        S_2up()

        if table == a:
            break

    used = [[0] * 100 for _ in range(100)]
    cnt = 0
    for i in range(99):
        for j in range(100):
            if table[i][j] == 0: continue
            if used[i][j] == 1: continue
            if table[i][j] == table[i + 1][j]: continue
            used[i][j] = 1
            used[i + 1][j] = 1
            cnt += 1

    print(f'#{tc} {cnt}')
