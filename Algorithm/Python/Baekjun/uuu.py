import sys
from collections import deque
input = sys.stdin.readline

me, bro = map(int, input().split())

q = deque()
q.append((me, 1, bro))
flag = 0
while q:
    cur_me, sec, cur_bro = q.popleft()
    cur_bro += sec
    if cur_bro > 500000:
        print(-1)
        break
    if cur_me < cur_bro - 1:
        rst1 = cur_me * 2
        if rst1 == cur_bro:
            flag = 1
            print(sec)
            break
        else:
            q.append((rst1, sec + 1, cur_bro))
    else:
        rst1 = cur_me * 2
        rst2 = cur_me - 1
        rst3 = cur_me + 1
        if rst1 == cur_bro or rst2 == cur_bro or rst3 == cur_bro:
            flag = 1
            print(sec)
            break
        else:
            q.append((rst1, sec + 1, cur_bro))
            q.append((rst2, sec + 1, cur_bro))
            q.append((rst3, sec + 1, cur_bro))


