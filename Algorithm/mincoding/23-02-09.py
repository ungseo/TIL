# ## 무한 재귀 막기
#
# def bbq(num):
#     if num > 10:
#         return
#     bbq(num+1)
#
# n = int(input())
# bbq(n)
#
#
# # n = int(input())
# # print(n)
#
# ## Title
#
# n = int(input())
# def ct(num):
#     print(num,end = ' ')
#     if num == 0:
#         return
#
#     ct(num-1)
#     print(num,end = ' ')
# ct(n)

## 마이클잭슨 무브먼트

# lst = list(map(int,input().split()))
#
# def mjmv(x,st):
#     print(x[st], end=' ')
#     if st == len(x)-1:
#         return
#     mjmv(x,st+1)
#     print(x[st], end = ' ')
#
# mjmv(lst,0)

## 두 칸씩 점프하기
# num = int(input())
#
# def abc(n):
#     if n == num+6:
#         print(n, end = ' ')
#         return
#     abc(n+2)
#     print(n, end = ' ')
#
# abc(num)

## 다섯글자 순차/역순으로 출력

# lst = list(input())
#
# def ho(x):
#     if x == 5:
#         print()
#         return
#     print(lst[x], end='')
#     ho(x+1)
#     print(lst[x], end='')
#
# ho(0)

## a, b 재귀호출

# a, b = map(int,input().split())
#
# def abc(x,y):
#     print(x, end=' ')
#     if x == y:
#         return
#     abc(x+1,y)
#     print(x, end=' ')
#
# abc(a,b)

## 재귀 부메랑

# num = int(input())
#
# lst = [3, 7, 4, 1, 9, 4, 6, 2]
#
# def pt(x):
#     print(lst[x], end=' ')
#     if x == 0:
#         return
#     pt(x-1)
#     print(lst[x], end=' ')
#
# pt(num)


## 없어질때까지 나눠먹기

# num = int(input())
#
# def abc(x):
#     s = x//2
#     if x == 0:
#         return
#     abc(s)
#     print(x, end=' ')
#
# abc(num)

## BBQ 갔다오기
#
# def BBQ(x):
#     if x == 3
#         return
#     BBQ(x+1)
#
#
# BBQ(0)

## 앞으로 돌진하는 계단
# st = input()
# ts = st[::-1]
# for i in range(len(st)):
#     for j in range(i,-1,-1):
#         print(ts[j],end='')
#     print()


## 절반 나누기

# st = input()
#
# idx = len(st)//2
#
# if st[:idx] == st[idx:]:
#     print('동일한문장')
# else:
#     print('다른문장')


## 겹치지 않도록
#
# bit1 = [list(map(int,input().split())) for i in range(4)]
# input()
# bit2 = [list(map(int,input().split())) for i in range(4)]
# cnt = 0
# for i in range(4):
#     for j in range(4):
#         if bit1[i][j] + bit2[i][j] == 2:
#             cnt += 1
#
# if cnt > 0 :
#     print('걸리다')
# else:
#     print('걸리지않는다')

## 일곱계단 만들기

# st = input()
# sp = ord(st) - 3
#
# for i in range(sp,sp+7):
#     if i < 65:
#         print(chr(i+26), end='')
#     elif i > 90:
#         print(chr(i-26), end='')
#     else:
#         print(chr(i), end='')


## 성 쌓기

# lst = list(map(int,input().split()))
#
# for i in range(4):
#     for j in range(4+i):
#         print(lst[j], end=' ')
#     print()

## 늘어나는 글자

# st = input()
#
# for i in range(len(st)):
#     for j in range(i+1):
#         print(st[j], end='')
#     print()

## 두 배열 머지(Merge)하기

# lst1 = list(map(int,input().split()))
# lst2 = list(map(int,input().split()))
#
# larr = 0
# rarr = 0
# ans = []
# while 1:
#     if larr == 4:
#         ans += lst2[rarr:]
#         break
#     if rarr == 4:
#         ans += lst1[larr:]
#         break
#     if lst1[larr] > lst2[rarr]:
#         ans.append(lst2[rarr])
#         rarr += 1
#     else:
#         ans.append(lst1[larr])
#         larr += 1
#
#
# print(*ans)


## 원하는 패턴의 크기 적용

# lst = [[3,5,4,2,5],[3,3,3,2,1],[3,2,6,7,8],[9,1,1,3,2]]
#
# y, x = map(int,input().split())
#
# def pat(a,b):
#     sum = 0
#     for i in range(y):
#         for j in range(x):
#             sum += lst[a+i][b+j]
#     return sum
#
# maxV = 0
# maxi = 0
# maxj = 0
#
# for i in range(4-y+1):
#     for j in range(5-x+1):
#         if maxV < pat(i,j):
#             maxV = pat(i,j)
#             maxi = i
#             maxj = j
#
# print(f'({maxi},{maxj})')
#

## 재귀호출이 3개일때

# def adc(level):
#     if level == 2:
#         return
#     for i in range(3):
#         adc(level+1)
#
# adc(0)

# id = 'qlqlaqkq'
# ps = 'tkaruqtkf'
#
# inid = input()
# inps = input()
#
# if id == inid and ps == inps:
#     print('LOGIN')
# else:
#     print('INVALID')

# lev = int(input())
# branch = int(input())
#
# def abc(level):
#     if level == lev:
#         return
#     for i in range(branch):
#         abc(level+1)
#
# abc(0)

## 입력받은 Level 까지 재귀함수 동작

# lev = int(input())
#
# def abc(level):
#     print(level, end='')
#     if level == lev:
#         return
#     for i in range(2):
#         abc(level+1)
#
# abc(0)

## 긴문장을 맨 앞으로
# lst = [input() for i in range(3)]
#
# def checkL(arr):
#     return len(arr)
# cnt = -1
# maxL = 0
# maxi = 0
# for i in lst:
#     cnt += 1
#     if checkL(i) > maxL:
#         maxL = checkL(i)
#         maxi = cnt
#
# lst[0],lst[maxi] = lst[maxi],lst[0]
#
# for i in lst:
#     print(i)
