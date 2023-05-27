import sys
from queue import PriorityQueue

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    p_q = PriorityQueue()
    q_p = PriorityQueue()
    for i in range(N):
        cmd, x = input().split()
        x = int(x)
        x_ = x * (-1)
        if cmd == 'I':
            p_q.put(x)
            q_p.put(x_)
        else:
            if x == 1 and q_p:
                q_p.get()
            elif x == -1 and p_q:
                p_q.get()

    maxV = q_p.get() * (-1)
    minV = p_q.get()
    if maxV == minV:
        print('EMPTY')
    else:
        print(maxV)
        print(minV)