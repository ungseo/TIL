#
# # T = int(input())
#
# # for tc in range(1,T+1):
# #     N,M =list(map(int,input().split()))
#
# #     lst = list(map(int,input().split()))
#
# #     temp = []
#
# #     def getsum(stn):
# #         sum = 0
# #         for i in range(M):
# #             sum += lst[stn]
# #             stn += 1
# #         return sum
# #     for i in range(N-M+1):
# #         temp.append(getsum(i))
#
# #     minV = temp[0]
# #     maxV = temp[0]
#
# #     for i in range(len(temp)):
# #         if minV > temp[i]:
# #             minV = temp[i]
# #         if maxV < temp[i]:
# #             maxV = temp[i]
#
# #     print(f'#{tc} {maxV-minV}')
#
# ## 색칠하기
#
# # def redblock(st1,st2,ed1,ed2):   ## 빨간색 색칠하는 함수
# #     for i in range(ed1-st1+1):
# #         for j in range(ed2-st2+1):
# #             lst[st1+i][st2+j] += 1
#
# # def blueblock(st1,st2,ed1,ed2):  ## 파란색 색칠하는 함수
# #     for i in range(ed1-st1+1):
# #         for j in range(ed2-st2+1):
# #             lst[st1+i][st2+j] += 2
#
# # T = int(input())
#
# # for tc in range(1,T+1):
# #     N = int(input())
# #     lst = [[0 for i in range(10)] for j in range(10)]  ## 10x10 배열 만들기
#
# #     for s in range(N):
# #         s1,s2,e1,e2,color = map(int,input().split())  ## 시작값 끝값, 색깔 따로저장
# #         if color == 1:             ## 색값이 1일때(빨강일때)
# #             redblock(s1,s2,e1,e2)    ## 빨간색칠하기
# #         else:                       ## 색값이 2일때(파랑일때)
# #             blueblock(s1,s2,e1,e2)  ## 파란색 칠하기
# #     cnt = 0
# #     for i in range(10):           ## 색값이 1+2= 3(보라색)인것 찾고 개수 출력
# #         for j in range(10):
# #             if lst[i][j] == 3:
# #                 cnt += 1
#
# #     print(f'#{tc} {cnt}')
#
#
# ## 델타검색
#
# # def adc_hap(y,x):
# #     movey = [-1,0,1,0]
# #     movex = [0,1,0,-1]
# #     sum = 0
# #     for i in range(4):
# #         newy = y + movey[i]
# #         newx = x + movex[i]
# #         if 0 <= newy < N and 0 <= newx < N:
# #             cha = lst[newy][newx] - lst[y][x]
# #             if cha < 0:
# #                 cha *= -1
# #                 sum += cha
# #             else:
# #                 sum += cha
# #     return sum
# #
# # for tc in range(1,11):
# #     N = int(input())
# #     lst = [list(map(int,input().split())) for i in range(N)]
# #     answer = 0
# #     for i in range(N):
# #         for j in range(N):
# #             if i==0 and j == 4:
# #                 debug = 1
# #             answer += adc_hap(i,j)
# #
# #     print(f'#{tc} {answer}')
#
# ## 이진탑색 (list1)
#
#
# # def bs(page,t):
# #     cnt = 0
# #     st = 1
# #     ed = page
# #
# #     while st <= ed:
# #         mid = (st + ed) // 2
# #         if mid == t:
# #             cnt += 1
# #             return cnt
# #         elif mid < t:
# #             st = mid
# #             cnt += 1
# #         else:
# #             ed = mid
# #             cnt += 1
# #     return cnt
# #
# # T = int(input())
# # for tc in range(1,T+1):
# #     total, A, B = map(int, input().split())
# #     Acnt = bs(total,A)
# #     Bcnt = bs(total,B)
# #
# #     if Acnt == Bcnt:
# #         print(f'#{tc} 0')
# #     elif Acnt < Bcnt:
# #         print(f'#{tc} A')
# #     else:
# #         print(f'#{tc} B')
#
# # import sys
# # sys.stdin = open('input.txt', 'r')
#
#
#
# # def Garohap(x):
# #     sum = 0
# #     for i in range(100):
# #         sum += lst[x][i]
# #     return sum
# #
# # def Serohap(y):
# #     sum = 0
# #     for i in range(100):
# #         sum += lst[i][y]
# #     return sum
# #
# # def Lslashhap():
# #     sum = 0
# #     for i in range(100):
# #         sum += lst[i][i]
# #         return sum
# #
# # def Rslashhap():
# #     sum = 0
# #     for i in range(99,-1,-1):
# #         sum += lst[i][i]
# #         return sum
# #
# # for s in range(1,11):
# #     tc = int(input())
# #     lst = [list(map(int,input().split())) for i in range(100)]
# #     maxV = Rslashhap()
# #     if maxV < Lslashhap():
# #         maxV = Lslashhap()
# #
# #     for i in range(100):
# #         if Garohap(i) > maxV:
# #             maxV = Garohap(i)
# #         if Serohap(i) > maxV:
# #             maxV = Serohap(i)
# #     print(f'#{tc} {maxV}')
# # def bbsort():
# #     for i in range(N-1):
# #         for j in range(N-1):
# #             if lst[j] > lst[j+1]:
# #                 lst[j], lst[j+1] = lst[j+1], lst[j]
# #
# #
# #
# #
# # T = int(input())
# # for tc in range(1,T+1):
# #     N = int(input())
# #     lst = list(map(int, input().split()))
# #     bbsort()
# #     ans = []
# #     st = 0
# #     ed = N-1
# #     for i in range(N//2):
# #         ans.append(lst[ed])
# #         ans.append(lst[st])
# #         st += 1
# #         ed -= 1
# #     if N % 2:
# #         ans.append(lst[N//2])
# #
# #     print(f'#{tc}',end=' ')
# #     for i in range(10):
# #         print(ans[i],end=' ')
# #     print()
# # import sys
# # sys.stdin = open('input.txt','r')
#
# # def bbsort(arr):
# #     for i in range(N-1):
# #         for j in range(N-1):
# #             if arr[j] > arr[j+1]:
# #                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# # def check():
# #     for i in range(len(bbang)):
# #         if bbang[i] != 0:
# #             return i
#
# # T = int(input())
#
# # for tc in range(1,T+1):
# #     N, M, K = map(int, input().split())
# #     guest = list(map(int,input().split()))
# #     bbsort(guest)
# #     temp = '0' + ('0' * (M-1) + str(K)) * 1000
# #     bbang = list(map(int,map(str,temp)))
# #     flag = 1
# #     for i in range(N):
# #         idx = check()
# #         if idx <= guest[i]:
# #             bbang[idx] -= 1
# #             continue
# #         else:
# #             print(f'#{tc} Impossible')
# #             flag = 0
# #             break
# #     if flag:
# #         print(f'#{tc} Possible')
# T = int(input())
#
# for tc in range(1,T+1):
#     N, K = map(int,input().split())
#     lst = [list(map(int,input().split())) for i in range(N)]
#
# def garo(arr, i):
#     for i in arr:
#

def abc(level):
    if level == 2:
        return

    abc(level + 1)
    abc(level + 1)
    dummy = 1


abc(0)