# x, y = map(int,input().split())
#
# cut = int(input())
# garo = []
# sero = []
# wide = []
# height = []
# for c in range(cut):
#     direction, point = map(int, input().split())
#     if direction == 0:
#         garo.append((direction, point))
#     else:
#         sero.append((direction, point))
#
# sero.sort(key= lambda x: x[1])
# garo.sort(key= lambda x: x[1])
# start = 0
# if len(sero) >= 1:
#     for w in range(len(sero)):
#         wide.append(sero[w][1] - start)
#         start = sero[w][1]
#     wide.append(x-sero[len(sero)-1][1])
# else:
#     wide.append(x)
# start = 0
# if len(garo) >= 1:
#     for h in range(len(garo)):
#         height.append(garo[h][1] - start)
#         start = garo[h][1]
#     height.append(y-garo[len(garo)-1][1])
# else:
#     height.append(y)
#
# print(max(height)*max(wide))

rend, cend = map(int, input().split())
n = int(input())

rlst, clst = [0, rend], [0, cend] # 자를 위치를 넣을 리스트

for _ in range(n):
    line, num = map(int, input().split()) # 가로세로와 자를 곳 입력
    if line: # 자를 위치의 반대되는 리스트에 넣어준다.
        rlst.append(num)
    else:
        clst.append(num)

rlst.sort() # 간격을 구해야 하므로 순서에 맞게
clst.sort() # 두 리스트 모두 정렬해주어야한다.

rmax = cmax = -(21e8)
for i in range(len(rlst)-1):
    rlen = rlst[i+1] - rlst[i]
    if rmax < rlen:
        rmax = rlen

for i in range(len(clst)-1):
    clen = clst[i+1] - clst[i]
    if cmax < clen:
        cmax = clen

print(rmax*cmax) # 가로세로로 가장 큰 간격을 곱해주어 면적 출력