# lst = [[0 for i in range(3)] for j in range(2)]
# arr = list(map(int, input().split()))
# idx = 0
# for i in range(2):
#     for j in range(3):
#         lst[i][j] = arr[idx]
#         idx += 1
#
#
# def maxV(arr):
#     maxv = arr[0]
#     for i in arr:
#         if maxv < i:
#             maxv = i
#     return maxv
#
#
# def minV(arr):
#     minv = arr[0]
#     for i in arr:
#         if minv > i:
#             minv = i
#     return minv
#
# for i in range(2):
#     for j in range(3):
#         if lst[i][j] == maxV(arr):
#             MAXi,MAXj = (i,j)
#         elif lst[i][j] == minV(arr):
#             MINi,MINj = (i,j)
#
# print(f'({MAXi},{MAXj})')
# print(f'({MINi},{MINj})')

## 누적점핑

# lst = [0 for i in range(6)]
#
# lst[0], lst[1] = map(int,input().split())
#
# for i in range(2,6):
#     lst[i] = lst[i-2] * lst[i-1]
#
# print(lst[5])

## 마음에 들지 않는 글자 바꾸기

# st = list(input())
#
# a = input()
# b = input()
#
# for i in range(len(st)):
#     if st[i] == a:
#         st[i] = b
#
# print(''.join(st))


## 함수를 이용하여 max, min 값 찾기

# def maxIndex(arr):
#     maxV = ord(arr[0])
#     for i in arr:
#         if maxV < ord(i):
#             maxV = ord(i)
#
#     cnt = -1
#     for i in arr:
#         cnt += 1
#         if chr(maxV) == i:
#             return cnt
#
#
# def minIndex(arr):
#     minV = ord(arr[0])
#     for i in arr:
#         if minV > ord(i):
#             minV = ord(i)
#
#     cnt = -1
#     for i in arr:
#         cnt += 1
#         if chr(minV) == i:
#             return cnt
#
# st = list(input())
#
# print(maxIndex(st))
# print(minIndex(st))

# lst = [[0 for j in range(4)] for i in range(7)]
#
# num = 1
# for i in range(7):
#     for j in range(4):
#         lst[i][j] = num
#         num += 1
#
# a, b, c = map(int, input().split())
#
# for i in range(7):
#     for j in range(4):
#         if i == a or i == b or i == c:
#             lst[i][j] = 0
#         print(lst[i][j], end=' ')
#     print()

## 두 글자의 존재 여부

# lst = [['A', '7', '9', 'T', 'K', 'Q'], ['M', 'I', 'N', 'C', 'O', 'D']]

# def isExist(arr):
#     a, b = input().split()
#     cntA = 0
#     cntB = 0
#     for i in lst:
#         for j in i:
#             if j == a:
#                 cntA += 1
#             elif j == b:
#                 cntB += 1
#     if cntA > 0:
#         print(f'{a} : 존재')
#     else :
#         print(f'{a} : 없음')
#
#     if cntB > 0 :
#         print(f'{b} : 존재')
#     else:
#         print(f'{b} : 없음')
#
# isExist(lst)
# #
#
# ## 동전
# coin=[500,100,50,10]  ## 동전 종류
# changes = int(input()) ## 거슬러 줄돈
# idx = 0  ## 인덱스  0 = 500, 1= 100, 2= 50, 3= 10
# coins = 0  ## 정답: 코인개수
# while 1:
#     coins += changes//coin[idx]  ## coin
#     changes = changes % coin[idx]
#     idx += 1
#     if idx == 4:
#         break
# print(coins)

## 연속되는 네모 세칸의 합이 가장 클 때의 값은?
# 연속되는 네모 세칸의 합이 가장 클 때 의 값은?
#
# lst= [[4, 5, 2, 6, 7, 3, 1],
#       [2, 9, 9, 6, 1, 6, 7]]
# temp = []
# for i in lst:
#     for j in range(len(i)-2):
#         sum = i[j]+i[j+1]+i[j+2]
#         temp.append(sum)
#
# maxi = temp[0]
# for i in temp:
#     if maxi < i:
#         maxi = i
# print(maxi)
#
#
# def getsum(a,b):
#     sum = 0
#     for i in range(3):
#         sum += lsta][b+i]
#     return sum
#
# for i in range(2):
#     for j in range(5):
#         ret =getsum(i,j)
#         if ret


'''
리스트에 숫자 4개 입력을 받은 후
입력받은 숫자라 lst 안에 존재하면 Y를
lst 안에 존재하지 않으면 N을 출력해 주세요


lst= [[4, 5, 2, 6, 7],
      [2, 9, 9, 6, 1],
      [2, 9, 9, 6, 1]]

5 3
8 2 입력시
Y N
N Y 출력

1 2
3 4 입력시
Y Y
N Y 출력
'''
#
# lst= [[4, 5, 2, 6, 7],
#       [2, 9, 9, 6, 1],
#       [2, 9, 9, 6, 1]]
#
# def isin(x):
#     cnt = 0
#     for i in lst:
#         if x in i:
#             cnt += 1
#     if cnt > 0 :
#         return 'Y'
#     else:
#         return 'N'
#
#
#
# for i in range(2):
#     a, b = map(int,input().split())
#     print(isin(a),end =' ')
#     print(isin(b),end =' ')

## 사각형 출력하기

# a, b, c  = map(str,input().split())
# a, b = int(a), int(b)
#
# for i in range(2):
#     for j in range(a):
#         for t in range(b):
#             print(c,end='')
#         print()
#     print()

## 좋아하는 메뉴 찾기

# lst = ['M','T','K','C']
#
# st = input()
#
# def isExist(x):
#     cnt = 0
#     if x in lst:
#         cnt += 1
#     if cnt > 0 :
#         print('발견')
#     else:
#         print('미발견')
#
# isExist(st)


'''정수 4개 입력받고
패턴 존재 여부 출력하기

1 1 2 1
없음

5 8 5 3
존재함
'''
# arr=[3,6,5,8,5,3,5,8,5,3,3,1,1,3]
# pattern = list(map(int,input().split()))
# cnt = 0
#
# for i in range(11):
#     if pattern == arr[i:i+4]:
#         cnt += 1
#
# if cnt > 1:
#     print('존재함')
# else:
#     print('없음')

## 네가 있는 거리에서

# lst = [5,9,4,6,1,5,8,9]
#
# index, target = map(int,input().split())
#
# offset = 0
# for i in range(index+1,8):  ## 1
#     if lst[i] != target:
#         offset += 1
#     else:
#         offset += 1
#         break
#
# print(offset)

## 비트배열 합 구하기

# lst = [[3,5,9],[4,2,1],[1,1,5]]
#
# bit = [list(map(int,input().split())) for i in range(3)]
#
# def check(x,y):
#     if bit[x][y] == 1:
#         return lst[x][y]
#     else:
#         return 0
#
# sum = 0
# for i in range(3):
#     for j in range(3):
#         sum += check(i,j)
#
# print(sum)


# lst = [list('ATKB'),list('CZFD'),list('HGEI')]
#
#
# st, y, x = input().split()
# st, y, x = ord(st), int(y), int(x)
#
#
# for i in range(3):
#     for j in range(4):
#         if ord(lst[i][j]) == st:
#             print(lst[i+y][j+x])
#             break

# lst = [[3,5,9],[4,2,1],[5,1,5]]
#
# arr = list(map(int,input().split()))
#
# def isExist(ls):
#
#     for i in ls:
#         cnt = 0
#         for j in lst:
#             if i in j:
#                 cnt += 1
#         if cnt > 0:
#             print(f'{i}:존재')
#         else:
#             print(f'{i}:미발견')
#
# isExist(arr)

## 합친 mask배열의 좌표 구하기
#
# mask1 = [[0,0,0,1],
#          [1,1,0,1],
#          [1,0,0,1],
#          [1,1,1,1]
#          ]
# mask2 = [[1,1,1,1],
#          [1,0,1,1],
#          [1,0,0,0],
#          [1,0,0,0]]
#
# def check(x,y):
#     result = mask1[x][y]+mask2[x][y]
#     if result >= 1:
#         return 1
#     else:
#         return 0
#
#
# for i in range(4):
#     for j in range(4):
#         if not check(i,j):
#             print(f'({i},{j})')

## 마스킹 처리후의 입력값 존재 여부

# mask = [[0,0,1,0,0],
#         [0,0,1,1,1]
#         ]
#
# lst = [[3,5,4,1,1],
#        [3,5,2,5,6]
#        ]
#
# num = int(input())
#
# temp = []
# def masking(x,y):
#     if mask[x][y] == 1:
#         temp.append(lst[x][y])
#
# for i in range(2):
#     for j in range(5):
#         masking(i,j)
#
# if num in temp:
#     print(f'{num} 존재')
# else:
#     print(f'{num} 없음')

## 마을사람들 찾기

# vect = ['B','T','K','I','G','Z']
#
# target = list(map(str,input().split()))
#
# cnt = 0
# for i in target:
#     for j in vect:
#         if i == j:
#             cnt += 1
#
# print(cnt)


## 인기투표

# vect = [[3,7,4],
#         [2,2,4],
#         [2,2,5]]
#
# target = list(map(int,input().split()))
# maxV= 0
# for i in target:
#     cnt = 0
#     for x in range(3):
#         for y in range(3):
#             if vect[x][y] == i:
#                 cnt += 1
#
#     if maxV < cnt :
#         maxV = cnt
#         t = i
#
# print(t)

## 저격 Sum

# lst = [3,4,1,1,2,6,8,7,8,9,10]
#
# def getSum(index):
#     sum = 0
#     for i in range(5):
#         sum += lst[index]
#         index += 1
#     return sum
#
# num = int(input())
#
# print(getSum(num))

## 합격자 발표일

lst = [3,7,4,1,2,6]

univer = [list(map(int,input().split()))]

def check(x,y):
    for i in lst:
        if univer[x][y] == i:
            return 1
    return 0

for i in range(2):
    for j in range(2):
        if check(i,j):
            print('OK',end=' ')
        else:
            print('NO',end=' ')
    print()