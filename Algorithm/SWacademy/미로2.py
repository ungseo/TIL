import sys
sys.stdin = open('input.txt','r')

from collections import deque
def bfs(v):
    q = deque()
    q.append(v)
    while q:
        now = q.popleft()
        for i in range(4):
            ny = now[0] + movy[i]
            nx = now[1] + movx[i]
            if 0 <= ny < 100 and 0 <= nx < 100 and maze[ny][nx] == 0:
                q.append((ny,nx))
                maze[ny][nx] = 1
            elif 0 <= ny < 100 and 0 <= nx < 100 and maze[ny][nx] == 3:
                return 1

movy = [-1, 0, 1, 0]
movx = [0, 1, 0, -1]
rst = 0
for _ in range(1,11):
    tc = int(input())
    maze = [list(map(int,map(str,input()))) for _ in range(100)]
    flag = 1
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                if bfs((i,j)) == 1:
                    print(f'#{tc} 1')
                else:
                    print(f'#{tc} 0')
                flag = 0
                break
        if flag == 0:
            break

