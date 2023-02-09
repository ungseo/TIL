 #이 모양으로 땅을 갖을 수 있다고 할때 어느 땅을 갖어야 할까요?
 #2*3 배열만큼 잘라서 합을 구할떄 최대값은 몇 일까요? !!

 #***
 #***
#
# arr=[[1, 5, 4, 2],
#     [1, 3, 4, 2],
#     [3, 5, 3, 2],
#     [2, 6, 4, 1]]
#
# lst = []
#
# def hap(x,y):
#     rst = 0
#     for i in range(x,x+2):
#         for j in range(y,y+3):
#             rst += arr[i][j]
#     return rst
#
# maxv = 0
# for i in range(3):
#     for j in range(2):
#         result =  hap(i,j)
#         if maxv < result:
#             maxv = result
#
# print(maxv)

## direct 배열을 활용하기  //델타배열

# arr = [[3, 5, 4],
#        [1, 1, 2],
#        [1, 3, 9]]
#
# x, y = map(int,input().split())
#
# id = [-1, 1, 0, 0]
# jd = [0, 0, -1, 1]
# sum = 0
# for i in range(4):
#         dx = x + id[i]
#         dy = y + jd[i]
#
#
#         if 0 <= x+id[i] <= 2 and 0 <= y+jd[i] <= 2:
#
#             sum += arr[dx][dy]
#
# print(sum)


# arr = [[3, 5, 4],
#        [1, 1, 2],
#        [1, 3, 9]]
#
# movey = [-1,1,0,0]
# movex = [0,0,-1,1]
#
#
# y,x = map(int,input().split())
# sum = 0
#
# if y > 2 or x > 2:
#     for i in range(4):
#         newy = y + movey[i]
#         newx = x + movex[i]
#         if 0 <= newy <= 2 and 0 <= newx <= 2:
#             sum += arr[newy][newx]
#
#     print(sum)

# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
#
# ## 좌표값 하나 입력 받아주세요
# ## 입력받은 좌표로부터 대각선에 있는곳의 값들의 곱을 구해서 출력해주세요!!
#
# ##  ex input : 1 2
#     ##  output :
#
# y, x = map(int,input().split())
#
# movey = [-1, -1, 1, 1]
# movex = [-1, 1, 1, -1]
# gop = 1
# for i in range(4):
#     newy = y + movey[i]
#     newx = x + movex[i]
#
#     if 0 <= newy <= 4 and 0 <= newx <= 4:
#         gop *= arr[newy][newx]
#
# print(gop)

# arr = [[3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
#
# y, x = map(int,input().split())
#
# movey = [-1, 0, 1, 0]
# movex = [0, 1, 0, -1]
#
# sum = 0
# for i in range(4):
#     for j in range(1,3):
#         newy = y + movey[i] * j
#         newx = x + movex[i] * j
#
#         if 0 <= newy <= 4 and 0 <= newx <= 4:
#             sum += arr[newy][newx]
#
# print(sum)

# lst = [[3,5,4],
#        [1,1,2],
#        [1,3,9]]
#
# y, x = map(int,input().split())
# movey = [-1,0,1,0]
# movex = [0,1,0,-1]
# sum = 0
#
# for i in range(4):
#     newy = y + movey[i]
#     newx = x + movex[i]
#     if 0 <= newy <= 2 and 0 <= newx <= 2:
#         sum += lst[newy][newx]
#
# print(sum)

## 가장 큰 곳 찾기
# #
# map = [[3,3,5,3,1],
#        [2,2,4,2,6],
#        [4,9,2,3,4],
#        [1,1,1,1,1],
#        [3,3,5,9,2]]
#
# maxV = 0
#
# def sum(a,b):
#     movey = [-1, -1, 1, 1]
#     movex = [-1, 1, 1, -1]
#     sum = 0
#     for i in range(4):
#         newy = a + movey[i]
#         newx = b + movex[i]
#         if 0 <= newy <= 4 and 0 <= newx <= 4:
#             sum += map[newy][newx]
#     return sum
# maxV = 0
# maxi = 0
# maxj = 0
# for i in range(5):
#     for j in range(5):
#         if sum(i,j) > maxV:
#             maxV = sum(i,j)
#             maxi = i
#             maxj = j
#
# print(maxi,maxj)
## 정수값 10을 이진수로 표현하기

# a= 10
# print(bin(a))
#
# ## 2진수의 값을 정수로 표현하기
#
# b = 0B1111
# print(b)  ## 자동으로 10진수로 표현
#
# ## 2진수(문자) 값을 정수로 출력하기
#
# c = '0B1111'
# print(int(c,2))
#
# ## 비트연산할때 and, or, >>, <<
#
# ## and
# a = 0B0001
# b = 0B1001
# print(a&b)
#
# ## or 연산
#
# a = 0B0011
# b = 0B1001
# print(a|b)
#
# ## shift 연산
#
# a = 0b0011
# b = 0b00101001
# print(a<<2)
# print(b<<3)
# print(a>>1)
# print(b>>3)

# arr=[[1, 2, 3, 4],
#     [1, 2, 9, 4],
#     [1, 9, 3, 9],
#     [1, 2, 9, 4]]

## 위 아래 좌 우 좌표들의 합이 가장 큰 곳의 합과
## 그 기준 좌표 값을 출력하기!!


# def hap(a,b):
#     sum = 0
#     movey = [-1, 0, 1, 0]
#     movex = [0, 1, 0, -1]
#
#     for i in range(4):
#         newy = a + movey[i]
#         newx = b + movex[i]
#
#         if 0 <= newy <= 3 and 0 <= newx <= 3:
#             sum += arr[newy][newx]
#
#     return sum
#
# maxV = 0
# for i in range(4):
#     for j in range(4):
#         rst = hap(i,j)
#         if maxV < rst:
#             maxV = rst
# flag = 0
# for i in range(4):
#     for j in range(4):
#         rst = hap(i,j)
#         if rst == maxV:
#             print(maxV,i,j)
#             flag = 1
#             break
#     if flag:
#         break

## 폭탄투하

# lst = [['_' for i in range(5)] for j in range(4)]
#
# def boom(a,b):
#     for i in range(a-1,a+2):
#         for j in range(b-1,b+2):
#             if 0 <= i <= 3 and 0 <= j <= 4:
#                 if i != a or j != b:
#                     lst[i][j] = '#'
#
# for i in range(2):
#     y, x = map(int,input().split())
#     boom(y,x)
#
# for i in range(4):
#     for j in range(5):
#         print(lst[i][j],end =' ')
#     print()

## 용의자의 GPS
#
# lst = [tuple(map(int,input().split())) for i in range(4)]
# vect = [[0 for i in range(3)] for j in range(4)]
#
# for i in range(4):
#     vect[lst[i][0]][lst[i][1]] = 5
#
# for i in range(4):
#     for j in range(3):
#         print(vect[i][j], end =' ')
#     print()

# lst = [list(map(int,input().split())) for j in range(4)]
#
# def rectSum(y,x):
#     sum = 0
#     for i in range(2):
#         for j in range(3):
#             sum += lst[y+i][x+j]
#     return sum
#
# maxV = 0
# maxi = 0
# maxj = 0
# for i in range(3):
#     for j in range(2):
#         rst = rectSum(i,j)
#         if rst > maxV:
#             maxV = rst
#             maxi = i
#             maxj = j
#
# print(f'({maxi},{maxj})')

## 함수와 포인터

# def BBQ():
#     lst = list(map(int,input().split()))
#     a = lst[0]
#     b = lst[0]
#     for i in lst:
#         if i > a:
#             a = i
#     for j in lst:
#         if j < b:
#             b = j
#     return a, b
#
# a, b = BBQ()
#
# print(f'a={a}')
#
# print(f'b={b}')

# lst = [list(map(int,input().split())) for i in range(5)]
#
# def check(y,x):
#     for i in range(y-1,y+2):
#         for j in range(x-1,x+2):
#             if 0 <= i <= 4 and 0 <= j <= 3:
#                 if i != y or j != x:
#                     if lst[i][j] == 1:
#                         return 0
#     return 1
#
# flag = 1
# for i in range(5):
#     for j in range(4):
#         if lst[i][j] == 1:
#             rst = check(i,j)
#             if not rst:
#                 flag = 0
#                 break
#             else:
#                 continue
#
# if flag:
#     print('안정된 상태')
# else:
#     print('불안정한 상태')

# lst = list(map(int,input().split()))
#
# arr = [[0 for i in range(4)] for j in range(4)]
# temp = [[0 for i in range(4)] for j in range(4)]
# n = 1
# for i in range(4):
#     for j in range(4):
#         temp[i][j] = n
#         n += 1
#
# def check(x):
#     for i in range(4):
#         for j in range(4):
#             if temp[i][j] == x:
#                 return [i,j]
# n = 1
# for it in lst:
#     i, j = check(it)
#     arr[i][j] = n
#     n += 1
#
# for i in range(4):
#     for j in range(4):
#         print(arr[i][j], end =' ')
#     print()

#
# lst = [[0 for i in range(4)] for j in range(4)]
#
# for i in range(3):
#     L, N = input().split()
#     N = int(N)
#
#     if L == 'G':
#         for i in range(4):
#             lst[N][i] = 1
#
#     else:
#         for i in range(4):
#             lst[i][N] = 1
#
# for i in range(4):
#     for j in range(4):
#         print(lst[i][j],end = ' ')
#     print()

##

