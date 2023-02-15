## 자기자리 찾기
#
# lst = list(map(int,input().split()))
#
# pv = lst[0]
#
# a = 1
# b = 7
#
# while a <= b:
#     if lst[a] < pv:
#         a += 1
#
#     if lst[b] > pv:
#         b -= 1
#     if a > b:
#         break
#
#     if lst[a] >= pv and lst[b] <= pv:
#         lst[a],lst[b] = lst[b],lst[a]
#
#
# lst[0], lst[b] = lst[b], lst[0]
#
# print(*lst)

## 황금좌표 찾기

# llst = [list(input()) for _ in range(4)]
#
# rlst = [['A','B','C','D'],
#         ['B','B','A','B'],
#         ['C','B','A','C'],
#         ['B','A','A','A']]
#
# dic = {}
#
# for i in range(4):
#     for j in range(4):
#         if llst[i][j] == rlst[i][j]:
#             if llst[i][j] not in dic:
#                 dic[llst[i][j]] = 1
#             else:
#                 dic[llst[i][j]] +=1
#
# ans = list(dic.items())
#
# maxV = 0
# maxi = 0
# for i in range(len(ans)):
#     if ans[i][1] > maxV:
#         maxV = ans[i][1]
#         maxi = i
# print(ans[maxi][0])


## 삼각관계

# name = ['Amy','Bob','Chloe','Diane','Edger']
#
# arr = [[0,0,0,0,1],
#        [1,0,0,0,0],
#        [0,1,0,0,0],
#        [0,1,0,0,0],
#        [0,0,0,0,0]]
#
# for i in range(5):
#     for j in range(5):
#         if i > j:
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
# maxV=0
# maxj = 0
# for i in arr:
#     for j in range(5):
#         if maxV < i[j]:
#             maxV = i[j]
#             maxj = j
#
# print(name[maxj])

## 보스와 부하들

# n = int(input())
#
# arr = [list(map(int,input().split())) for _ in range(n)]
#
# under = []
# cnt = 0
#
# for i in range(n):
#     if arr[i][0] == 1:
#         boss = i
#     if arr[0][i] == 1:
#         under.append(i)
# under =' '.join(map(str,under))
# print(f'boss:{boss}')
# print(f'under:{under}')

## 잃어버린 가족상봉
name = ['A','B','C','D','E','F','G','H']
arr = [[0,1,1,0,0,0,0,1],  #a
       [0,0,0,0,0,0,0,0], #b
       [0,0,0,1,1,0,1,0],#c
       [0,0,0,0,0,1,0,0],#d
       [0,0,0,0,0,0,0,0],#e
       [0,0,0,0,0,0,0,0],#f
       [0,0,0,0,0,0,0,0],#g
       [0,0,0,0,0,0,0,0]]#h

n = input()    # h
for i in range(8):
    if name[i] == n:
        idx = i   #idx == 7
        break
if idx != 0:
    for i in range(8):
        if arr[i][idx] == 1:
            mi = i  ## mi = 0
            break

    for i in range(8):
        if i != idx and arr[mi][i] == 1:
            print(name[i], end=' ')
else:
    print('없음')