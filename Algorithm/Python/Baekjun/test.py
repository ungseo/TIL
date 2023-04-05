def dfs(level, st):
    if level == 3:
        print(st, end=' ')
        return

    for i in range(3):
        if used[i] == 1: continue
        used[i] = 1
        dfs(level + 1, st+str(lst[i]))
        used[i] = 0

lst = [34, 3, 30]
used = [0] * 3
path = [0] * 3
dfs(0, '')
