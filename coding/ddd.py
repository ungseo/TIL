# arr = [2,7,1,4,3]
# n = int(input())
# branch = 5
# cnt = 0
# def hap(level,sum):
#     global cnt
#     if level == n:
#         if sum > 20:
#             cnt += 1
#         return
#     for i in range(5):
#         hap(level+1,sum+arr[i])
#
# hap(0,0)
# print(cnt)

# cnt = 0
# n = int(input())
# arr = [2, 7, 1, 4, 3]
# def asdf(sum, level):
#     global cnt
#     if level == n:
#         if sum > 20:
#             cnt += 1
#         return
#     for i in arr:
#         asdf(sum + i, level + 1)
#
# asdf(0, 0)
# print(cnt)

# n = int(input())
# coin = [110,70,10]
# minL = 999
#
# def abc(level,changes):
#     global minL
#     if changes == 0:
#         if minL > level:
#             minL = level
#
#     if changes < 0:
#         return
#     for i in range(3):
#         abc(level+1, changes-coin[i])
#
#
# abc(0,n)
# print(minL)

# lev = int(input())
# branch = 6
# dice = [1,2,3,4,5,6]
# path = [0] * 10000
# def roll(level):
#
#     if level == lev:
#         print(path[0:level])
#         return
#
#     for i in range(6):
#         path[level] = dice[i]
#         roll(level+1)
#
# roll(0)

## 선택정렬
lst = [1, 7, 2, 9, 3, 3, 2, 10]

for i in range(len(lst)):
    min_i = i
    for j in range(1+i,len(lst)):
        if lst[min_i] > lst[j]:
            min_i = j
    lst[i], lst[min_i] = lst[min_i], lst[i]

print(lst)

arr = [9,2,3,1,22,3,4,1,0]

for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)