# friends = list(input())
# ans = [''] * 3
# def abc(level):
#     ans
#     if level == 3:
#         pt = list(set(ans))
#         if len(pt) == 3:
#             print(''.join(ans))
#
#         return
#
#     for i in range(4):
#         ans[level] = friends[i]
#         abc(level + 1)
#
#
#
# abc(0)
# lv = int(input())
# branch = 4
#
# dice = [1,2,3,4]
# used = [0] * branch
# path = [0] * lv
#
# def abc(level):
#     if level == lv:
#         print(' '.join(map(str,path)))
#         return
#
#     for i in range(4):
#         if used[i] == 1:
#             continue
#         used[i] = 1
#         path[level] = dice[i]
#         abc(level+1)
#         used[i] = 0
#
# abc(0)

## 다음가지에 진입하지 않는 경우

# lv = 3
# lst = [1,2,3,4]
# path = [0] * lv
#
# def abc(level):
#     if level == lv:
#         print(' '.join(map(str,path)))
#         return
#
#     for i in range(4):
#         if level == 0 and i == 1:
#             continue
#         path[level] = lst[i]
#         abc(level+1)
#
# abc(0)

## 다음 가지 진입후 첫칸에 2가 들어있으면 리턴해버리기

# lv = 3
# lst = [1,2,3,4]
# path = [0] * lv
#
# def abc(level):
#     if path[0] == 2:
#         return
#     if level == lv:
#         print(' '.join(map(str,path)))
#         return
#
#     for i in range(4):
#         path[level] = lst[i]
#         abc(level+1)
#
# abc(0)


''' ABCD가 적혀있는 카드 3 묶음이 있습니다.
각 묶음에서 카드를 1장씩 뽑았을 때
C로  시작하는 경우는 다 제외하기
'''
# lv = 3
# branch = 4
# card = ['A','B','C','D']
# path = [''] * lv
#
# def pick(level):
#     if level == lv:
#         print(' '.join(path))
#         return
#
#     for i in range(branch):
#         if level == 0 and i == 2:
#             continue
#         path[level] = card[i]
#         pick(level+1)
#
# pick(0)



##
# lv = 3
# branch = 4
# card = ['A','B','C','D']
# path = [''] * lv
#
# def pick(level):
#     # if 'B' in path:
#     #     return
#     if level > 0 and path[level-1] == 'B' : return
#     if level == lv:
#         print(' '.join(path))
#         return
#
#     for i in range(branch):
#         path[level] = card[i]
#         pick(level+1)
#
# pick(0)
# #
# # lv = 3
# # branch = 4
# # card = ['A','B','C','D']
# # path = [''] * lv
# #
# # def pick(level):
# #
# #     if level == lv:
# #         print(' '.join(path))
# #         return
# #
# #     for i in range(branch):
# #         if i == 1: continue
# #         path[level] = card[i]
# #         pick(level+1)
# #
# # pick(0)
# #


# lev = 3
# branch =4
# pp = ['A','B','C','D']
# path = [0] * lev
# def abc(level):
#     if level > 1 and path[level-1] == path[level-2]: return
#     if level == lev:
#         print(' '.join(path))
#         return
#
#     for i in range(branch):
#         path[level] = pp[i]
#         abc(level+1)
#
# abc(0)


# lev = 3
# branch =4
# pp = ['A','B','C','D']
# path = [0] * lev
# def abc(level):
#
#     if level == lev:
#         print(' '.join(path))
#         return
#
#     for i in range(branch):
#         if level > 0 and pp[i] == path[level-1]: continue
#         path[level] = pp[i]
#         abc(level+1)
#
# abc(0)
# #
# lev = 3
# branch = 4
# pp = ['A','B','C','D']
# path = [0] * lev
#
# def abc(level,st):
#     if level == lev:
#         print(' '.join(path))
#         return
#
#     for i in range(st,4):
#         path[level] = pp[i]
#         abc(level+1,i+1)
#
# abc(0,0)
# print()
#
# frd = list(input())
# path = [0] * 3
# used = [0] * 4
#
# def pick(level):
#     if level == 3:
#         print(''.join(path))
#         return
#
#     for i in range(4):
#         if used[i] == 1: continue
#         used[i] = 1
#         path[level] = frd[i]
#         pick(level+1)
#         used[i] = 0
# pick(0)

## 그래프 표현하기

# 인접 행렬 (이차배열)

# people = ['Amy','Bob','Chloe','Diane','Edger']
#
# arr = [[0,0,1,0,1],
#        [1,0,0,0,0],
#        [0,1,0,0,0],
#        [0,1,0,0,0],
#        [0,0,0,1,0]]
#
# # 여기서  가장 인기가 많은 사람은 누구인지 출력
# maxV=0
# for j in range(5):
#     sum = 0
#     for i in range(5):
#         if arr[i][j] == 1:
#             sum += 1
#     if maxV < sum:
#         maxV = sum
#         pp = people[j]
# print(pp)
#

# st = input()

# arr = ['A','B','D','E','C','F']

# arr2 = [[0,1,0,0,1,0],
#         [0,0,1,1,0,0],
#         [0,0,0,0,0,0],
#         [0,0,0,0,0,0],
#         [0,0,0,0,0,1],
#         [0,0,0,0,0,0]]

# for i in range(6):
#     if arr[i] == st:
#         si = i

# for i in range(6):
#     if arr2[i][si] == 1:
#         mi = i

# flag = 1
# if si != 0:
#     for i in range(6):
#         if i != si and arr2[mi][i] == 1:
#             print(arr[i],end =' ')
#             flag = 0

# if flag:
#     print('형제없음')


## 다툰친구 B와 T

lst = list(input())
lev = 4
path = [0] * 4
used = [0] * 4
cnt = 0
def abc(level):
    
    
    if level == lev:
        print(''.join(path))
        return
    
    for i in range(4):
        if used[i] == 1:
            continue
        path[level] = lst[i]
        used[i] = 1
        abc(level+1)
        used[i] = 0
    if level == 0:
        print(cnt)
        
abc(0)