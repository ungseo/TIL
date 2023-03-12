#
# name = '1234'
# cnt = 0
# path = ['']*3
#
# def abc(level,start):
#     global cnt
#     if level == 3:
#         cnt += 1
#         for i in range(3):
#             print(path[i],end = ' ')
#
#         print()
#         return
#     for i in range(start, 4):
#         path[level] = name[i]
#         abc(level+1,i)
#         path[level] = 0
#
# abc(0,0)# level, start
#
#
# print(cnt)
#

# pp = ['A','B','C','D']
#
# used = [0,0,0,0]
# cnt = 0
# def dfs(level):
#     global cnt
#     if level == 4:
#         for i in range(4):
#             if used[i] == 1:
#                 print(pp[i],end =' ')
#         print()
#         cnt += 1
#         return
#
#     for i in range(2):
#         used[level] = i
#         dfs(level+1)
# dfs(0)
# print(cnt)

# cnt = 0
# name = ['A','B','C','D']
# path = ['','','','']
# def dfs(level, idx):
#     global cnt
#     print(''.join(path))
#     cnt += 1
#     if level == 4:
#         return
#
#     for i in range(idx,4):
#         path[level] = name[i]
#         dfs(level+1, i+1)
#         path[level] = ''
#
# dfs(0,0)
# print(cnt)


# line1 = [-2,3,4,9,-5,2]
# line2 = [4,7,-3,-6,-1,2]
#
# lst1 = []
# lst2 = []
# used = [0,0,0,0,0,0]
# path = [0,0,0,0,0,0]
#
# def dfs(level, ratio, arr,inst):
#     global path
#     if level == 6:
#         inst.append(path[:])
#         return
#
#     for i in range(6):
#         if used[i] == 1: continue
#         used[i] = 1
#         path[level] = arr[i] * ratio
#         dfs(level+1,ratio+2,arr,inst)
#         path[level] = 0
#         used[i] = 0
#
# dfs(0,1,line1,lst1)
# dfs(0,0,line2,lst2)
#
# rst = []
# for i in range(len(lst1)):
#     rst.append(sum(lst1[i]) + sum(lst2[i]))
#
# minV = 21e8
# for i in rst:
#     if abs(minV) > abs(i):
#         minV = i
#
# print(minV)
