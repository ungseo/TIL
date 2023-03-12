'''난이도 D2'''
import sys
sys.stdin = open('input.txt','r')


def move(step,y,x):
    global flag
    if Map[y][x] == '3':
        flag = 1
        return
    my = [-1,0,1,0]
    mx = [0,1,0,-1]
    for i in range(4):
        ny = y + my[i]
        nx = x + mx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if Map[ny][nx] == '0':
                Map[ny][nx] = '1'
                move(step+1,ny,nx)
            elif Map[ny][nx] == '3':
                move(step+1,ny,nx)
        if flag:
            return

T = int(input())
for tc in range(1,1+T):
    n = int(input())
    Map = [list(input()) for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if Map[i][j] == '2':
                sty, stx = i, j

    move(0,sty,stx)

    print(f'#{tc} {flag}')