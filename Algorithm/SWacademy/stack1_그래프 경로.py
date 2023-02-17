'''난이도 D2'''
def can(level):
    global flag
    if level == g:
        flag = 1
        return
    for i in range(1,V+1):
        if arr[level][i] == 1:
            if used[i] == 0:
                used[i] = 1
                can(i)
                used[i] = 0

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    arr = [[0 for i in range(V+1)] for _ in range(V+1)]
    flag = 0
    used = [0] * (V+1)
    # 그래프 행렬 완성하기
    for s in range(E):
        i, j = list(map(int, input().split()))
        arr[i][j] = 1

    s, g = map(int, input().split())
    used[s] = 1
    # 재귀돌려서 탐색
    can(s)
    print(f'#{tc} {flag}')

