h, w = map(int, input().split())
sky = [list(input()) for _ in range(h)]

for i in range(h):
    now_cloud = -1
    for j in range(w):
        if sky[i][j] == 'c':
            print(0, end=' ')
            now_cloud = j
        elif sky[i][j] == '.' and now_cloud >= 0:
            print(j - now_cloud, end=' ')
        elif sky[i][j] == '.' and now_cloud == -1:
            print(-1, end=' ')
    print()