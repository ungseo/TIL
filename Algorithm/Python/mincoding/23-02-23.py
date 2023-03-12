'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

'''


# V = int(input())
# arr = list(map(int,input().split()))
# E = V - 1
# print(E)
# left = [0] * (V+1)
# right = [0] * (V+1)
# par = [0] * (V+1)
# for i in range(E):
#     p,c= arr[i*2], arr[i*2+1]
#     if left[p] == 0:
#         left[p] = c
#     else:
#         right[p] = c
#     par[c] = p
# print(left, right)
# print(par)
# root = 1
# while par[root] != 0:
#     root += 1
# print(root)

## 다시 풀어보는 출동 순서
#
# hero = ['B','I','A','H']*20
# num = int(input())
# go = []
# pointer = -1
#
# while len(go) != 4:
#     for i in range(num):
#         pointer += 1
#         if hero[pointer] in go:
#             while hero[pointer] in go:
#                 pointer += 1
#     go.append(hero[pointer])
#
# print(*go)
from collections import deque
T =int(input())
for tc in range(1,1+T):
    V, E = map(int,input().split())
    arr = [[0] * V for _ in range(V)]
    que = deque()
    for _ in range(E):
        m,s = map(int,input().split())
        for i in range(V):
            arr[m-1][s-1] = 1
            arr[s-1][m-1] = 1


    start, end = map(int,input().split())
    used = [0] * V
    answer = []
    que.append(start-1)
    cnt = 0

def bfs(level,n):
    while que:
        now = que.popleft()
        used[now] = 1

        for i in range(V):
            if used[i] == 1: continue
            if arr[now][i] == 1:
                que.append((i, level)
        cnt += 1
        if end-1 in que:
            break

    print(f'#{tc} {cnt}')


'''
1
7 4
1 6
2 3
2 6
3 5
1 5

'''


