# n = int(input())
# ans = []
# flag = 0
#
#
# for i in range(n, 0, -1):
#     a = str(i)
#     sum = 0
#     for j in a:
#         sum += int(j)
#     if i + sum == n:
#         flag = 1
#         ans.append(i)
# if flag == 0:
#     print(0)
# else:
#     print(min(ans))

N = int(input())
ans = 0
for i in range(max(0,N-len(str(N))*9),N):
    if sum(map(int,str(i))) + i == N:
        ans = i
        break
print(ans)