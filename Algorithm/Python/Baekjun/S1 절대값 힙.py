import sys
from queue import PriorityQueue

input = sys.stdin.readline
n = int(input())
pQueue = PriorityQueue() # 우선순위 큐 생성

for i in range(n):
    x = int(input())
    if x == 0:
        if pQueue.empty():
            print(0)
        else:

            temp = pQueue.get()
            print(str(temp[1]))
    else:
        pQueue.put((abs(x), x))