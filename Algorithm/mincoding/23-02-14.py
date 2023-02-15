# ## 다툰 친구 B와 T
# st = input()
# path = ['']*4
# cnt = 0
# def abc(level):
#     global path, cnt
#     if 2 <= level <= 4:
#         if ''.join(path[level-2:level]) == 'BT' or ''.join(path[level-2:level]) == 'TB':
#             return
#     if level == 4:
#         cnt += 1
#         return
#
#     for i in range(4):
#         path[level] = st[i]
#         abc(level+1)
#
# abc(0)
# print(cnt)

## ABC 초콜릿

# choco = ['A','B','C']
# n = int(input())
# path = [''] * n
# cnt = 0
# def dfs(level):
#     global cnt
#     if level == n:
#         cnt += 1
#         return
#
#     for i in range(3):
#         if level > 1 and path[level-2] == path[level-1]:
#             if path[level-1] == choco[i]: continue
#         path[level] = choco[i]
#         dfs(level+1)
#
# dfs(0)
# print(cnt)

## 산타소년단
# n = int(input())
# santa = ['B','T','S','K','R']
# path = [''] * n
# used = [0] * 5
# cnt = 0
# def pick(level):
#     global cnt
#     if level == n and 'S' in path:
#         cnt += 1
#     if level == n:
#         return
#
#     for i in range(5):
#         if used[i] == 0:
#             path[level] = santa[i]
#             used[i] = 1
#             pick(level+1)
#             used[i] = 0
# pick(0)
# print(cnt)

## 미안하다 친구야
# def pick(level):
#     if level == 4:
#         print(''.join(path))
#         return
#
#     for i in range(5):
#         if used[i] == 0:
#             used[i] = 1
#             path[level] = frd[i]
#             pick(level+1)
#             used[i] = 0
#
# frd = ['E','W','A','B','C']
# path = [0] * 4
# ext = input()
# used = [0] * 5
#
# for i in range(5):
#     if frd[i] == ext:
#         ei = i
#         break
# used[ei] = 1
#
# pick(0)

## 다섯종류의 숫자카드

# card = list(map(int,map(str,input())))
# path = [0] * 4
# cnt = 0
# def dfs(level):
#     global cnt
#     if level == 4:
#         cnt += 1
#         return
#
#     for i in range(5):
#         if level > 0 and (path[level-1] - card[i] > 3 or path[level-1] - card[i] < -3):
#             continue
#         path[level] = card[i]
#         dfs(level+1)
#
# dfs(0)
#
# print(cnt)

## 왼쪽, 오른쪽 이동
# def right():
#     global arr
#     arr = [0] + arr
#     arr[0] = arr[5]
#     arr = arr[0:5]
# def left():
#     global arr
#     arr = arr + [0]
#     arr[5] = arr[0]
#     arr = arr[1:6]
#
#
# arr = [3,5,1,9,7]
# for i in range(4):
#     drt = input()
#
#     if drt == 'R':
#         right()
#     else:
#         left()
#
# print(*arr)

## 암살자 존휙
# world = [[0]* 4 for _ in range(3)]
# for i in range(3):
#     y,x = map(int,input().split())
#     world[y][x] = 1
#
# flag = 0
# for i in range(3):
#     sum = 0
#     for j in range(4):
#         sum += world[i][j]
#     if sum > 1:
#         print('위험')
#         flag = 1
#         break
#
#
# for j in range(4):
#     sum = 0
#     for i in range(3):
#         sum += world[i][j]
#     if sum > 1:
#         print('위험')
#         flag = 1
#         break
# if flag == 0:
#     print('안전')


## 네모네모더하기

# lst = [[0] * 4 for _ in range(4)]
# for i in range(3):
#     temp = list(map(int,input().split()))
#     for j in range(3):
#         lst[i][j] = temp[j]
#
# for i in range(3):
#     sum = 0
#     for j in range(3):
#         sum += lst[i][j]
#     lst[i][3] = sum
#
# for j in range(3):
#     sum = 0
#     for i in range(3):
#         sum += lst[i][j]
#     lst[3][j] = sum
# sum = 0
# for i in range(3):
#     sum += lst[i][i]
# lst[3][3] = sum
#
# for i in range(4):
#     for j in range(4):
#         print(lst[i][j], end=' ')
#     print()

## 숫자 transformation

arr = [
        [3,5,4,1],
       [1,1,2,3],
       [6,7,1,2]
       ]

lst = list(map(int,input().split()))
temp = ['a','b','c','d']

for sc in range(4):
    for i in range(3):
        for j in range(4):
            if arr[i][j] == lst[sc]:
                arr[i][j] = temp[sc]

lst = lst + [lst[0]]
lst = lst[1:]

for s in range(4):
    for i in range(3):
        for j in range(4):
            if arr[i][j] == temp[s]:
                arr[i][j] = lst[s]

for i in range(3):
    for j in range(4):
        print(arr[i][j], end = ' ')
    print()