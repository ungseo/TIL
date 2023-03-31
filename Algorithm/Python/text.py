def dfs(level):
    global cnt
    if level == n-1:
        cnt += 1
        return

    for i in range(n):
        if used[i] == 1:
            continue
        used[i] = 1
        dfs(level+1)
        used[i] = 0


n = int(input())
chess = [[0] * n for _ in range(n)]
used = [0] * n
cnt = 0
dfs(0)
print(cnt)

# def dfs(level):
#     global cnt
#     if level == n-1:
#         cnt += 1
#         return
#
#     for i in range(n):
#         if used[i] == 1: continue
#         if used_y[i + level] == 1: continue
#         if used_x[i - level + n - 1] == 1: continue
#         used[i] = 1
#         used_y[i + level] = 1
#         used_x[i - level + n - 1] = 1
#         dfs(level + 1)
#         used[i] = 0
#         used_y[i + level] = 0
#         used_x[i - level + n - 1] = 0
#
#
# n = int(input())
# chess = [[0] * n for _ in range(n)]
# used = [0] * n
# used_x = [0] * n ** 2
# used_y = [0] * n ** 2
# cnt = 0
#
# dfs(0)
# print(cnt)
