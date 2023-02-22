## 인접행렬 그래프 DFS

# arr = [[0,0,1,1,0,1],
#        [0,0,0,1,1,1],
#        [0,0,0,0,1,1],
#        [0,0,0,0,0,0],
#        [1,0,0,0,0,1],
#        [0,0,0,0,0,0]]
# used = [0] * 6
# st = int(input())
#
# def dfs(start):
#        print(start, end = ' ')
#        for i in range(6):
#               if used[i] == 1: continue
#               if arr[start][i] == 1:
#                      used[i] = 1
#                      dfs(i)
# used[st] = 1
# dfs(st)

## 가중치 인접행렬 DFS

# arr =[[0,0,1,0,2,0],
#       [5,0,3,0,0,0],
#       [0,0,0,0,0,7],
#       [2,0,0,0,8,0],
#       [0,0,9,0,0,0],
#       [4,0,0,7,0,0]]
# used = [0]*6
# k = int(input())
# sum = 0
# def dfs(start,s):
#     global sum
#     sum += s
#     print(f'{start} {sum}')
#     for i in range(6):
#         if used[i] == 1: continue
#         if arr[start][i] == 0 : continue
#         used[i] = 1
#         dfs(i,arr[start][i])
# used[k] = 1
# dfs(k,0)


## 트리 인접행렬 BFS
# from collections import deque
# arr = [[0,1,0,0,1,0],
#        [0,0,1,0,0,1],
#        [0,0,0,1,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0]]
# st = int(input())
#
# def bfs(start):
#     que = deque()
#     que.append(start)
#     while que:
#         now = que.popleft()
#         print(now, end=' ')
#         for i in range(6):
#             if arr[now][i] == 1:
#                 que.append(i)
#
# bfs(st)


## 그래프 BFS
# from collections import deque
#
# arr = [[0,0,0,0,1,0],
#        [1,0,1,0,0,1],
#        [1,0,0,1,0,0],
#        [1,1,0,0,0,0],
#        [0,1,0,1,0,1],
#        [0,0,1,1,0,0]]
# used = [0] * 6
# st = int(input())
#
# def bfs(start):
#     que = deque()
#     que.append(start)
#     while que:
#         now = que.popleft()
#         print(now)
#         for i in range(6):
#             if arr[now][i] == 0 : continue
#             if used[i] == 1: continue
#             used[i] = 1
#             que.append(i)
# used[st] = 1
# bfs(st)

## 원형시계 돌리기
# from collections import deque
# def roll():
#     f = clock.pop()
#     clock.appendleft(f)
#
# clock = deque()
# clock.append(12)
# clock.append(3)
# clock.append(6)
# clock.append(9)
#
# degree = int(input())
# n = degree//90
# for i in range(n):
#     roll()
#
# clock[3], clock[1] = clock[1], clock[3]
# clock[2], clock[3] = clock[3], clock[2]
# print(*clock)

# 번외
# from collections import deque
#
# clock = [12,9,3,6]
# arr = [[0,1,0,0],
#        [0,0,1,0],
#        [0,0,0,1],
#        [1,0,0,0]]
# degree = int(input())
# n = degree//90
# used = [0] * 4
# used[n] = 1
# def watch(start):
#     que = deque()
#     que.append(start)
#     while que:
#         now = que.popleft()
#         print(clock[now],end=' ')
#         for i in range(4):
#             if used[i] == 1: continue
#             if arr[now][i] == 1:
#                 used[i] = 1
#                 que.append(i)
#
# watch(n)
#

## 승부차기

# people = int(input())
# ox = [0] * people
# def soccer(seq):
#     if seq == people:
#         for i in ox:
#             if i == 0:
#                 print('o',end='')
#             else:
#                 print('x',end='')
#         print()
#         return
#     for i in range(2):
#         ox[seq] = i
#         soccer(seq+1)
# soccer(0)

## n번째로 큰 숫자 출력

# lst = [1,5,4,2,-5,-7]
# n = int(input())
#
# for i in range(5):
#     for j in range(5-i):
#         if lst[j] < lst[j+1]:
#             lst[j],lst[j+1] = lst[j+1],lst[j]
# print(lst[n-1])

## 2진수로 된 가장 큰 수를 찾아라
# def ten():
#     st = list(map(int,map(str,bist))) # bist 리스트화
#     rst = 0
#     n = 0
#     while st:
#         binum = st.pop()
#         if binum:
#             rst += 2**n
#         n += 1
#     return rst
#
# maxV = 0
# ans = ''
# for i in range(3):
#     bist = input()
#     rst = ten()
#     if rst > maxV:
#         maxV = rst
#         ans = bist
#
# print(ans)

## 후보 선출하기

# pp =list(map(str,input()))
# n = int(input())
# path = [0] * n
# def choice(level):
#     if level == n:
#         for i in range(n):
#             print(path[i], end='')
#         print()
#         return
#
#     for i in range(len(pp)):
#         path[level] = pp[i]
#         choice(level+1)
#
# choice(0)

## 자전거열쇠 비밀번호 맞추기
# def hacking(level):
#     global cnt,flag
#     if level == 4:
#         cnt += 1
#         if ''.join(check) == st:
#             flag = 1
#         return
#
#     for i in range(65,91):
#         check[level] = chr(i)
#         hacking(level+1)
#         if flag == 1:
#             return
#
# n = int(input())
#
#
# for tc in range(n):
#     st = input()
#     flag = 0
#     cnt = 0
#     check = [0] * 4
#     hacking(0)
#     print(cnt)
#

## 다섯형제 1020
def dfs(level, sum):
    global cnt
    if 10 <= sum <= 20:
        cnt += 1
        return
    if level == 5:
        return

    for i in range(0+level, 5):
        if used[i] == 1: continue
        dfs(level+1, sum+lst[i])
        sum -= lst[i]
lst = list(map(int,input().split()))
used = [0] * 5

cnt = 0
dfs(0,0)

print(cnt)









