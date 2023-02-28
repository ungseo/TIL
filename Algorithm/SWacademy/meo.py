def johap(level):
    if level == n - 2:

        print(path)
        return

    for i in range(3):
        if level == 0 and i == 2: continue
        if level == n - 3 and i == 0: continue
        if level > 0:
            if path[level - 1] == 'W' and color[i] == 'R': continue
            if path[level - 1] == 'B' and color[i] == 'W': continue
            if path[level - 1] == 'R' and color[i] == 'W': continue
            if path[level - 1] == 'R' and color[i] == 'B': continue

        path[level] = color[i]
n = 5
path = [0] * (n - 2)
color = ['W','B','R']

johap(0)