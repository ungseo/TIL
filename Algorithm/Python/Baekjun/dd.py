import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    for i in range(n):
        if arr[1][i] == 1:
            q.append((1, i, 1))
    while q:
        pi, nowi, nows = q.popleft()
        if pi == s:
            print(nows)
            return
        for i in range(n):
            if arr[nowi][i] == 1:
                q.append((pi, i, nows+1))
    print(-1)
    return

n = int(input())
f, s = map(int,input().split())
m = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    mom, son = map(int,input().split())
     arr[mom][son] = 1

bfs()