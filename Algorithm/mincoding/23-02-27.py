# n = int(input())
# lst = list(map(int,input().split()))
# sum = 0
# for i in range(4):
#     sum += lst[i]
# min_sum = sum
# for i in range(n-4):
#     sum -= lst[i]
#     sum += lst[i+4]
#     if min_sum > sum:
#         min_sum = sum
#
# print(min_sum)


## 세로 줄 변경
#
# arr = [list(input()) for _ in range(5)]
#
#
# for i in range(5):
#     arr[i][1], arr[i][3] = arr[i][3], arr[i][1]
#
# flag = 1
# for i in arr:
#     if ''.join(i) == 'MAPOM':
#         flag = 0
#         print('yes')
#         break
# if flag == 1:
#     print('no')

## HITS MUSIC
#
# n = int(input())
# slst = list(input().split())
# path = ['','']
# cnt = 0
# def dfs(level,start):
#     global cnt
#     if level == 2:
#         if ''.join(path) == 'HITSMUSIC':
#             cnt += 1
#         return
#
#     for i in range(start,n):
#         path[level] = slst[i]
#         dfs(level+1, i+1)
#
# dfs(0,0)
# print(cnt)

## 버스 주차요금 저렴한 곳 찾기

# road = [1, 2, 3, 3, 5, 1, 0, 1, 3]
#
# n = int(input())
#
# sum = 0
# for i in range(n):
#     sum += road[i]
# min_sum = sum
#
# for i in range(9-n):
#     sum -= road[i]
#     sum += road[i+n]
#     if min_sum > sum:
#         min_sum = sum
#
# print(min_sum)

## 복합 사전정렬

# n = int(input())
# lst = []
# for s in range(n):
#     lst.append(input())
#
# for i in range(n-1):
#     for j in range(n-1-i):
#         if len(lst[j]) > len(lst[j+1]):
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#         elif len(lst[j]) == len(lst[j+1]):
#             for s in range(len(lst[j])):
#                 if ord(lst[j][s]) > ord(lst[j+1][s]):
#                     lst[j], lst[j+1] = lst[j+1], lst[j]
#                     break
#                 elif ord(lst[j][s]) == ord(lst[j+1][s]):
#                     continue
#                 else:
#                     break
#
# for i in lst:
#     print(i, sep='')

## 숫자 부침개
def rvs(number):
    number = number[::-1]
    return int(number)




p = int(input())
n = int(input())

for cook in range(n):
    p *= 2
    p = rvs(str(p))

print(p)