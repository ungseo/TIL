# # arr = [3, 4, 5, 1, 6, 9]
# # ## 누적합 출력하기!!
# # # 출력결과 : 3 7 12 13 19 28 19 13 12 7 3
# # #
# # def abc(sum,n):
# #
# #     if n == 5:
# #         print(sum, end=' ')
# #         return
# #     print(sum, end=' ')
# #     abc(sum+arr[n],n+1)
# #     print(sum, end=' ')
# #
# # abc(3,0)
# #
# # # def adc(level,sum):
# # #     print(sum,end=' ')
# # #     if level == 5:
# # #         return
# # #     adc(level+1,sum+arr[level+1])
# # #     print(sum,end=' ')
# # # adc(0,3)
# #
# # sum = arr[0]
# # def abc(level):
# #     global sum
# #     print(sum, end=' ')
# #     if level == 5:
# #         return
# #     sum += arr[level + 1]
# #     abc(level+1)
# #     sum -= arr[level+1]
# #     print(sum, end=' ')
# #
# # abc(0)
#
# # arr = [2, 0, 1, 1, 3, 5, 1]
# #
# # def jump(st):
# #     if st > 6:
# #         return
# #     jump(st+arr[st])
# #     print(arr[st], end=' ')
# #
# # jump(0)
# card = [3,7,1,2]
# sum = 0
# def getsum(level):
#     global sum
#
#     if level == 3:
#         print(sum,end=' ')
#         return
#
#     for i in range(4):
#         sum += card[i]
#         getsum(level+1)
#         sum -= card[i]
#
# getsum(0)

arr = [2,7,1,4,3]
n = int(input())
branch = 5
cnt = 0
def hap(level,sum):
    global cnt
    if level == n:
        if sum > 20:
            cnt += 1
        return
    for i in range(5):
        hap(level+1,sum+arr[i])

hap(0,0)
print(cnt)