def bfs(st):
    q = []
    q.append(st)
    while q:
        now = q.pop(0)
        print(name[now])
        for i in range(4):
            if arr[now][i] == 1:
                if used[i] == 0:
                    used[i] = 1
                    q.append(i)


name = ['A', 'B', 'C', 'D']

arr = [[0, 1, 1, 0],
       [0, 0, 1, 1],
       [0, 1, 0, 1],
       [0, 0, 0, 0]]
used = [1, 0, 0, 0]
bfs(0)