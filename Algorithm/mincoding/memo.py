import sys
sys.stdin = open('input.txt','r')

def down(x):
    global cnt
    y = 0
    while y < 99:
        if ladder[y][x-1] == 0 and ladder[y][x+1] == 0:
            y += 1
            cnt += 1
        elif ladder[y][x-1] == 1:
            y, x = left(y,x)
            
            continue
        elif ladder[y][x+1] == 1:
            y, x = right(y,x)
            
            continue
    return cnt
def left(y,x):
    global cnt
    while 1:
        if ladder[y][x-1] == 0:
            y += 1
            cnt += 1
            return [y, x]
        else:
            x -= 1
            cnt += 1

def right(y,x):
    global cnt
    while 1:
        if ladder[y][x+1] == 0:
            y += 1
            cnt += 1
            return [y, x]
        else:
            x += 1
            cnt += 1


minX = 0
for _ in range(1, 11):
    tc = int(input())
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    minS = 21e8
    for i in range(1,100+1):
        cnt = 0
        if ladder[0][i] == 1:
            cnt = down(i)
            if minS > cnt:
                minS = cnt
                minX = i
    print(f'#{tc} {minX-1}')
