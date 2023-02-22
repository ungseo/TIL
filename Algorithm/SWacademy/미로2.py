import sys
sys.stdin = open('input.txt','r')
for _ in range(1,11):
    tc = int(input())
    maze = [list(map(int,map(str,input()))) for _ in range(100)]
    my = [-1,0,1,0]
    mx = [0,1,0,-1]
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                sty, stx = i, j
            if maze[i][j] == 3:
                edy, edx = i, j
    maze[sty][stx] = 1
    flag = 0
    while 1:
        for dr in range(4):
            py, px = sty, stx
            sty = sty + my[dr]
            stx = stx + mx[dr]
            if sty < 0 or stx < 0 or sty >= 100 or stx >= 100: continue
            if sty == edy and stx == edx:
                flag = 1
                break
            if 0 <= sty+my[0] < 100 and 0 <= sty+my[2] < 100 and 0<= stx+mx[1] < 100 and 0 <= stx+mx[3] < 100:
                if maze[sty+my[0]][stx+my[0]] == 1 and maze[sty+my[1]][stx+my[1]] == 1 and maze[sty+my[2]][stx+my[2]] == 1 and [sty+my[3]][stx+my[3]]== 1:
                    while sty != py and stx != px:
                        if dr == 0:
                            sty += 1
                        elif dr == 1:
                            stx -= 1
                        elif dr == 2:
                            sty -= 1
                        elif dr == 3:
                            sty += 1
            if maze[sty][stx] == 1: continue
            maze[sty][stx] = 1
        if flag == 1:
            break
    print(f'#{tc} {flag}')


