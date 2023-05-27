import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
S = int(input())

arr = [[] for _ in range(V + 1)]
DAT = [21e8] * (V + 1)
for i in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((w, v))

q = []
heapq.heappush(q, (0, S))
DAT[S] = 0
while q:
    time, node = heapq.heappop(q)

    if DAT[node] < time:
        continue

    for i in arr[node]:
        dis, des = i[0] + time, i[1]
        if DAT[des] < dis: continue
        DAT[des] = dis
        heapq.heappush(q, (dis, des))

for i in range(1, 1 + V):
    if DAT[i] == 21e8:
        print('INF')
    else:
        print(DAT[i])
```
