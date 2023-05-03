import sys
from collections import deque

input = sys.stdin.readline


# D
def cmdD(reg):
    rst = reg * 2 % 10000
    return rst

# S
def cmdS(reg):
    rst = reg - 1
    if rst < 0:
        rst = 9999
    return rst

# L
def cmdL(reg):
    if len(str(reg)) != 4:
        rst = reg * 10
    else:
        temp = list(str(reg)) + ['']
        temp[0], temp[-1] = temp[-1], temp[0]
        rst = ''.join(temp)
    return int(rst)

# R
def cmdR(reg):
    if len(str(reg)) != 4:
        zero = len(str(reg))
        temp = [''] + ['0'] * (4 - zero) + list(str(reg))
        temp[0], temp[-1] = temp[-1], temp[0]

    else:
        temp = [''] + list(str(reg))
        temp[0], temp[-1] = temp[-1], temp[0]
    rst = ''.join(temp)
    return int(rst)


def bfs():
    q = deque()
    q.append((a, ''))
    while q:
        nownum, cmd = q.popleft()
        if nownum == b:
            print(cmd)
            return

        if nownum != 0:
            newnum = cmdD(nownum)
            if numlst[newnum] != 1:
                q.append((newnum, cmd + 'D'))

        newnum = cmdS(nownum)
        if numlst[newnum] != 1:
            q.append((newnum, cmd + 'S'))

        if nownum != 0:
            newnum = cmdL(nownum)
            if numlst[newnum] != 1:
                q.append((newnum, cmd + 'L'))
            newnum = cmdL(nownum)
            if numlst[newnum] != 1:
                q.append((newnum, cmd + 'R'))


T = int(input())
cmdlst = ['D', 'S', 'L', 'R']
for tc in range(T):
    a, b = map(int, input().split())
    numlst = [0] * 10000
    numlst[a] = 1
    bfs()

