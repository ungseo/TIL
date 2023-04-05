import sys

input = sys.stdin.readline


def dfs(level, st, idx):
    if vs:
        a = len(str(vs[0]))
        b = len(st)
        cha = a-b
        if max(vs) // 10 ** cha > int(st):
            return
    if level == L:
        vs.append(int(st))
        return

    for i in range(L):
        if used[i] == 1: continue
        used[i] = 1
        dfs(level + 1, st + str(lst[idx][i]), idx)
        used[i] = 0

n = int(input())
lst = [[], [], [], [], [], [], [], [], [], []]
arr = list(input().split())
for i in arr:
    lst[int(i[0])].insert(0, int(i))

for i in range(9, 0, -1):
    if len(lst[i]) == 0: continue
    if len(lst[i]) == 1:
        print(lst[i][0], end='')
    else:
        vs = []
        L = len(lst[i])
        used = [0] * L
        dfs(0, '', i)
        print(max(vs), end=' ')
if lst[0]:
    print('0'*len(lst[0]))

