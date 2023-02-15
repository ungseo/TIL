# TREE dfs 탐색 순서 출력하기

# name = list(input().split())

# arr = [[0,1,1,0,0,0],
#        [0,0,0,1,1,0],
#        [0,0,0,0,1,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0]]

# answer = []
# def dfs(now):
#     global answer
#     answer.append(name[now])
    
#     for i in range(6):
#         if arr[now][i] == 1:
#             dfs(i)
            
# dfs(0)
# print(*answer)


# lst = ['K','F','C','D','M','G','A']
# ans = []
# arr = [[0,1,1,1,0,0,0],
#        [0,0,0,0,1,1,0],
#        [0,0,0,0,0,0,1],
#        [0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0]]

# def dfs(now):
#     ans.append(lst[now])
#     for i in range(7):
#         if arr[now][i] == 1:
#             dfs(i)

# dfs(0)
# print(*ans)


# lst = ['B','A','C','D']
# used = [1] + [0] * 3
# path = []
# arr = [[0,0,1,1],
#        [1,0,0,0],
#        [0,1,0,1],
#        [0,0,0,0]]

# def dfs(now):
#     path.append(lst[now])
    
#     for i in range(4):
#         if arr[now][i] == 1:
#             if used[i] == 0:
#                 used[i] = 1
#                 dfs(i)

# dfs(0)
# print(*path)


#
# lst = list(input().split())  ## B A C D
# used = [0,0,0,0]
# used[1] = 1
# path = []
# cnt = 0
# arr = [[0,0,1,1],
#        [1,0,1,0],
#        [1,0,0,1],
#        [0,0,0,0]]
#
# def dfs(now):
#     global cnt
#     path.append(lst[now])
#     if now == 3:
#         cnt += 1
#         print(*path)
#         return
#     for i in range(4):
#         if arr[now][i] == 1:
#             if used[i] == 0:
#                 used[i] = 1
#                 dfs(i)
#                 used[i] = 0
#                 path.pop()
#
# dfs(1)
# # print(*path)
#
# name = list(input().split()) # B A C D
# arr = [[0,0,3,14],
#         [7,0,19,0],
#         [3,0,0,1],
#         [0,0,0,0]]
# used = [0] * 4
# used[1] = 1
# minV = 21e8
# def abc(now, sum):
#     global minV
#     if now == 3 and sum < minV:
#         minV = sum
#
#     for i in range(4):
#         if used[i] == 0 and arr[now][i] > 0:
#             used[i] = 1
#             abc(i,sum+arr[now][i])
#             used[i] = 0
#
# abc(1,0)
#
# print(minV)
#
# sum = 0
# minV = 21e8
# def abc(now):
#     global sum, minV
#     if now == 3 and sum < minV:
#         minV = sum
#
#
#     for i in range(4):
#         if arr[now][i] > 0 and used[i] == 0:
#             used[i] = 1
#             sum += arr[now][i]
#             abc(i)
#             used[i] = 0
#             sum -= arr[now][i]
#
# abc(1)
# print(minV)
#

## 퀴즈 출발점을 입력받습니다.
# 입력받은 출발점 알파벳 부터 E가 써있는 곳 까지 갈 수 있는 방법이 몇가지 있는 지 출력 해 주세요

stp = input()
name = ['A','B','C','D','E']
for i in range(5):
    if name[i] == stp:
        sti = i
        break
arr = [[0,4,0,0,0],
       [0,0,1,2,9],
       [5,0,0,7,0],
       [0,0,0,0,1],
       [0,0,0,0,0]]

used = [0] * 5
used[sti] = 1
minV = 21e8

def dfs(now,sum):
    global minV
    if now == 4 and minV > sum:
        minV = sum

    for i in range(5):
        if used[i] == 0 and arr[now][i] > 0:
            used[i] = 1
            dfs(i,sum+arr[now][i])
            used[i] = 0
dfs(sti,0)
print(minV)





















