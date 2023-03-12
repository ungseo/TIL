from collections import deque

def bfs(y,x,step):
    q = deque()
    q.append((y,x,step))

    while q:



T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    # 시작점 찾기
    flag = 1
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                sty, stx = i, j
                flag = 0
                break
        if flag == 0: break

    # bfs로 최단거리 계산
