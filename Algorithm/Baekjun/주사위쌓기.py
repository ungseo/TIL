# n = int(input())
# dice_lst = [list(map(int, input().split())) for _ in range(n)]
#
# for i in range(n):
#     dice_lst[i][5], dice_lst[i][1] = dice_lst[i][1], dice_lst[i][5]
#     dice_lst[i][3], dice_lst[i][4] = dice_lst[i][4], dice_lst[i][3]
#
# start = []
# for i in range(0,6,2):
#     if dice_lst[0][i] == 6 or dice_lst[0][i+1] == 6:
#         continue
#     else:
#         start.append(dice_lst[0][i])
#         start.append(dice_lst[0][i+1])
#
# maxSum = 0
# for st in range(4):
#     sum = 6
#     stack = []
#     stack.append(start[st])
#     for i in range(1, n):
#         for j in range(0, 6, 2):
#             if dice_lst[i][j] == stack[-1]:
#                 stack.append(dice_lst[i][j])
#                 stack.append(dice_lst[i][j+1])
#                 if dice_lst[i][j] == 6 or dice_lst[i][j+1] == 6:
#                     sum += 5
#                 else:
#                     sum += 6
#             elif dice_lst[i][j+1] == stack[-1]:
#                 stack.append(dice_lst[i][j+1])
#                 stack.append(dice_lst[i][j])
#                 if dice_lst[i][j] == 6 or dice_lst[i][j+1] == 6:
#                     sum += 5
#                 else:
#                     sum += 6
#         if maxSum < sum:
#             maxSum = sum
# print(maxSum)


n = int(input())
dice_lst = [list(map(int, input().split())) for _ in range(n)]  # 입력

for i in range(n):  # 마주보는 면끼리 2개씩 붙여서 정렬
    dice_lst[i][5], dice_lst[i][1] = dice_lst[i][1], dice_lst[i][5]
    dice_lst[i][3], dice_lst[i][4] = dice_lst[i][4], dice_lst[i][3]

maxSum = 0
for st in range(6):   # 맨 밑에 주사위 들어갈 수있는 모든 경우의 수 입력
    temp = dice_lst[0][:]    # temp 배열을 이용해 stack에 들어간 주사위 눈금 빼고 최댓값을 구하는 방법 생각
    stack = []
    if st % 2 == 0:
        stack.append(temp.pop(st))   # temp배열로 값을 빼고 주사위 배열은 건들지않음.
        stack.append(temp.pop(st))
    else:
        stack.append(temp.pop(st))
        stack.append(temp.pop(st-1))
    sum = max(temp)   # 밑과 윗면에 주사위가 빠진 temp배열이 옆면이 됨. 그중 최댓값 sum에 더하기

    for i in range(1, n):         # 2번주사위부터 윗면과 같으면 위의 방식과 비슷하게 stack에 쌓아줌
        temp = dice_lst[i][:]  #옆면 최댓값 구하기위해 복사함
        for j in range(0, 6, 2):
            if temp[j] == stack[-1]:  # 스택의 맨위와 들어갈 주사위의 면이 같으면
                stack.append(temp.pop(j))  # 밑면 추가
                stack.append(temp.pop(j))  # 윗면 추가
                sum += max(temp)
                break

            elif temp[j+1] == stack[-1]:
                stack.append(temp.pop(j+1))
                stack.append(temp.pop(j))
                sum += max(temp)
                break
        if maxSum < sum:  # sum 최댓값 구하기
            maxSum = sum
print(maxSum)


def find(top, bottom):
	num = [i for i in range(1,7) if i!=top and i!=bottom]
	return max(num)

n = int(input())
dices = [list(map(int,input().split())) for _ in range(n)]
rule = {0:5,1:3,2:4,3:1,4:2,5:0}
dice = dices[0]
result = 0

for idx in range(len(dice)):
	top, bottom = dice[idx], dice[rule[idx]]
	res = find(top,bottom)
	for d in dices[1:]:
		top, bottom = d[rule[d.index(top)]], d[d.index(top)]
		res += find(top, bottom)
	result = max(result, res)
print(result)