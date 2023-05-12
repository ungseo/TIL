import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    q = deque()
    q.append((start, 0))

    while q:
        cur_node, sec = q.popleft()  # 현재 도착노드, 도착노드에 걸린 시간
        if sec > DAT[cur_node]: continue
        DAT[cur_node] = sec
        for i in arr[cur_node]:
            q.append((i[0], sec + i[1]))


V, E = map(int, input().split())
K = int(input())
arr = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((v, w))

DAT = [9999] * (V + 1)

bfs(K)

for i in range(1, V + 1):
    if DAT[i] != 9999:
        print(DAT[i])
    else:
        print('INF')
