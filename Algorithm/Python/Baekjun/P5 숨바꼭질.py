from collections import deque
me, bro = map(int, input().split())

q = deque()
q.append((me, 1, bro))
DAT = [0] * 500001

if me == bro:
    print(0)
else:
    while q:
        cur_me, sec, cur_bro = q.popleft()
        cur_bro += sec


        rst1 = cur_me * 2
        rst2 = cur_me - 1
        rst3 = cur_me + 1
        if rst1 == cur_bro or rst2 == cur_bro or rst3 == cur_bro:
            print(sec)
            break

        if 500000 >= rst1 > sec != DAT[rst1]:
            DAT[rst1] = sec
            q.append((rst1, sec + 1, cur_bro))

        if 500000 >= rst3 > sec != DAT[rst3]:
            DAT[rst3] = sec
            q.append((rst3, sec + 1, cur_bro))

        if DAT[rst2] != sec and sec < rst2:
            DAT[rst2] = sec
            q.append((rst2, sec + 1, cur_bro))

        if cur_bro + sec + 1 > 500000:
            print(-1)
            break




