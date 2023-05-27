from collections import deque


def bfs():
    q = deque()
    q.append((st, 0))
    maxStep = 0

    while q:
        node, step = q.popleft()
        if maxStep <= step:
            maxStep = step
            if maxPP[maxStep] < node:
                maxPP[maxStep] = node

        for i in graph[node]:
            if visited[i] == 1: continue
            visited[i] = 1
            q.append((i, step + 1))


for tc in range(1, 11):
    pp, st = map(int, input().split())
    ppList = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, pp, 2):
        graph[ppList[i]].append(ppList[i + 1])
    visited = [0] * 101
    visited[st] = 1
    maxPP = [0] * 101
    bfs()
    for i in maxPP[::-1]:
        if i > 0:
            print(f'#{tc} {i}')
            break

