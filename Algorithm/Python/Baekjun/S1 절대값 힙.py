import sys
from deque import 

input = sys.stdin.readline
lst = []
n = int(input())
for i in range(n):
    a = int(input())
    if a == 0:
        if lst:
            print(0)
        else:
            heapq.heappop(lst)

a =
