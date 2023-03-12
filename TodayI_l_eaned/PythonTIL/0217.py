## Sliding window

# n, m = map(int, input().split())
# lst = list(map(int, input().split()))
# fsum = 0
# for i in range(m):
#     fsum += lst[i]
#
# maxS = fsum
# for i in range(n-m):
#     fsum -= lst[i]
#     fsum += lst[i+m]
#     if maxS < fsum:
#         maxS = fsum
#
# print(maxS)

## Two pointer

# n, m = map(int,input().split())
# lst = list(map(int,input().split()))
# cnt, st, ed = 0, 0, 0
# sum = 0
# while 1:
#     if sum > m or ed == n:
#         sum -= lst[st]
#         st += 1
#
#     elif sum < m:
#         sum += lst[ed]
#         ed += 1
#
#     else:
#         sum -= lst[st]
#         cnt += 1
#         st += 1
#     if st == n:
#         break
# print(cnt)
#

# from collections import deque
#
# q = deque()
# q.append(5)
# q.append(6)
# q.append(7)
# q.append(8)
# q.append(9)
#
# print(q)
# print([*q])
# q.popleft()
# q.popleft()
# print(*q)
#
# from collections import deque
# name = list(input().split()) #A B C D E F
#
# arr = [[0,1,1,0,0,0],
#        [0,0,0,1,1,0],
#        [0,0,0,0,0,1],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0]]
# answer = [] # 탐색순서 저장 후 출력
#
# def bfs(x):
#     a = deque()
#     a.append(x)
#
#     while a:
#         now = a.popleft()
#         answer.append(name[now])
#         for i in range(6):
#             if arr[now][i] == 1:
#                 a.append(i)
#
# bfs(0)
# print(answer)


## BFS

from collections import deque

# lst = ['A','B','C','E','D','F']
# arr = [[0,1,0,1,0,0],
#        [0,0,1,0,1,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,1],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0]]
# ans = []
# def bfs(st):
#     que = deque()
#     que.append(st)
#
#     while que:
#         now = que.popleft()
#         ans.append(lst[now])
#
#         for i in range(6):
#             if arr[now][i] == 1:
#                 que.append(i)
#
#
# bfs(0)
#
# print(ans)
#
#
from collections import deque

lst = ['A','B','C','D']
arr = [[0,1,1,0],
       [0,0,1,1],
       [0,1,0,1],
       [0,0,0,0]]
used = [0] * 4
used[0] = 1
ans = []

def bfs(x):
    que = deque()
    que.append(x)

    while que:
        now = que.popleft()
        ans.append(lst[now])
        for i in range(4):
            if arr[now][i] == 1:
                if used[i] == 0:
                    used[i] = 1
                    que.append(i)
bfs(0)
print(ans)






