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



lst = list(input().split())  ## B A C D
used = [0,0,0,0]
used[1] = 1
path = []
cnt = 0
arr = [[0,0,1,1],
       [1,0,1,0],
       [1,0,0,1],
       [0,0,0,0]]

def dfs(now):
    global cnt
    path.append(lst[now])
    if now == 3:
        cnt += 1
        print(*path)
        return
    for i in range(4):
        if arr[now][i] == 1:
            if used[i] == 0:
                used[i] = 1
                dfs(i)
                used[i] = 0
                path.pop()

dfs(1)
# print(*path)



