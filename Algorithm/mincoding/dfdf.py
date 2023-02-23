lst = [1,2,3]
path= [0] * 3
used = [0] * 3
cnt = 0
def dfs(level,idx):
    for i in range(level):
        print(path[i],end=' ')
    print()
    global cnt
    cnt += 1
    if level == 3: return

    for i in range(idx, 3):
        path[level] = lst[i]
        dfs(level+1,i+1)
        path[level] = 0

dfs(0,0)
print(cnt)