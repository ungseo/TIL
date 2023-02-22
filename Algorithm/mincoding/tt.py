lst = [3,1,2]

def dfs(level,idx):
    if level == 2:
        print(path)
        return

    for i in range(3):
        if used[i] == 1 : continue
        if i < idx : continue
        used[i] = 1
        path[level] = lst[i]
        dfs(level+1,i)
        used[i] = 0

path = [0]*2
used = [0] * 3
dfs(0,0)
