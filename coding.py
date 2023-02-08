# # 2023-01-17 Home study

# #Call by value 
# # def main():
# #     a,b =map(int,input().split())
# #     BBQ(a,b)

# # def BBQ(x,y):
# #     print(f'합:{x+y}')
# #     print(f'차:{x-y}')
# #     print(f'곱:{x*y}')
# #     print(f'몫:{x//y}')

# # main()

# # #Call by value2
# # global lst
# # lst = [['F', 'E', 'W'], ['D', 'C', 'A']]

# # def main():
# #     s = input()
# #     findCh(s)

# # def findCh(x):
# #     if lst[0].count(x) >= 1 or lst[1].count(x) >= 1:
# #         print('발견')
# #     else:
# #         print('미발견')

# # main()

# #탐색하며 호출하기

# # lst = input().split()

# # def checkChar(Char):
# #     if 65 <= ord(Char) <= 90:
# #         print('대', end = '')
# #     elif 97 <= ord(Char) <=122:
# #         print('소', end = '')

# # for i in lst:
# #     checkChar(i)

# # 구조체 변수 어러개 만들기

# # class Person():
# #     age = int()
# #     height = int()

# # a = Person()
# # b = Person()

# # def Input():
# #     a.age ,a.height, b.age, b.height = list(map(int,input().split()))


# # def Output():
# #     age_avg = (a.age + b.age)//2
# #     height_avg = (a.height + b.height)//2
# #     print(age_avg,height_avg)

# # Input()
# # Output()


# #어디에 숨었을까?

# # lst = [2,1,2,4,5]
# # arr = [[2,5,3],[4,5,7],[8,7,2]]

# # num = int(input())
# # ea = 0

# # ea += lst.count(num)

# # for i in range(3):
# #     ea += arr[i].count(num)

# # print(ea)

# #Index 찾아내기

# # lst = list(input().split())
# # idx = list(filter(lambda x : lst[x] == 'A', range(5)))
# # A_ea = lst.count('A')
# # print(f'문자A는 {A_ea}개발견')

# # for i in idx:
# #     print(f'{i}번')

# #2차배열에서 좌표 출력하기

# # arr = [['D','A','A'],['B','C','D'],['E','F','A'],['A','A','D'],['F','G','E']]

# # s = input()

# # for i in range(5):
# #     for j in range(3):
# #         if arr[i][j] == s :
# #             print(f'({i},{j})')

# # 2차배열에서 범위안에 있는 값 세기

# # arr = [[10,3,20],[60,30,40],[20,30,40]]

# # a, b = list(map(int,input().split()))
# # result = 0
# # for i in range(3):
# #     for j in range(3):
# #         if a <= arr[i][j] <= b:
# #             result += 1
# # print(result)

# #각 함수에서 대소문자 찾기

# # def Input():
# #     global arr
# #     arr = [[0,0,0],[0,0,0]]
# #     lst = input().split()
# #     s = 0
# #     for i in range(2):
# #         for j in range(3):
# #             arr[i][j] = lst[s]
# #             s += 1
    


# # def findUpper():
# #     Uc = 0
# #     for i in arr:
# #         for j in range(3):
# #             if 65 <= ord(i[j]) <= 90:
# #                 Uc += 1
# #     print(f'대문자{Uc}개')

# # def findLower():
# #     Lc = 0
# #     for i in arr:
# #         for j in range(3):
# #             if 97 <= ord(i[j]) <= 122:
# #                 Lc += 1
# #     print(f'소문자{Lc}개')

# # def main():
# #     Input()
# #     findUpper()
# #     findLower()

# # main()

# #N의배수인 숫자 찾기

# # arr = [[3,5,14],[2,3,9],[6,2,7]]

# # num = int(input())
# # sum = 0
# # if num != 0 :
# #     for i in arr:
# #         a = list(filter(lambda x : i[x] % num == 0, range(3)))
# #         sum += len(a)
# # else:
# #     print(0)

# # print(sum)

# #함수에 숫자 주고 출력하기

# # num = int(input())
# # def BBQ(x):
# #     for i in range(1,x+1):
# #         print(i, end ='')

# # def KFC(x):
# #     for i in range(7):
# #         print(x*7)

# # if num % 2 == 1:
# #     num2 = int(input())
# #     BBQ(num2)

# # elif num == 0 :
# #     print(0)

# # else:
# #     string = input()
# #     KFC(string)


# #돌아오는 One Two

# # def one():
# #     num = int(input())
# #     return num

# # def two():

# #     string = input()
# #     return string

# # def main():
# #     a = one()
# #     b = two()
# #     return str(a)+b

# # print(main())

# #대각선 긋기

# # num = int(input())
# # lst = [[0]*4 for i in range(4)]


# # if num % 2 == 0 :
# #     j = 0
# #     for i in lst:
# #         i[j] = j+1
# #         j += 1
# # else:
# #     j, d = 3, 1
# #     for i in lst:
# #         i[j] = d
# #         j -= 1
# #         d += 1
        
# # for i in range(4):
# #     for j in range(4):
# #         print(lst[i][j], end = ' ')
# #     print()

# # KFC 주문하기


    
# # def KFC():
# #                               ##  80, Z
# #     a = chicken()             ##  90, Z
# #     b = coke()
# #     print(f'{a}{b}')

# # def chicken():
# #     num = int(input())
# #     return num + 10

# # def coke():
# #     string = input()
# #     return string

# # KFC()

# #사전순으로 큰 문자 찾기

# # def getChar():
# #     A, B = input().split()
# #     if ord(A) > ord(B) :
# #         return A
# #     else :
# #         return B

# # result = getChar()
# # print(result)

# #번호 순서대로

# # num = int(input()) # 숫자 한개를 입력 받아주세요
# # lst = [[0,0,0],[0,0,0],[0,0,0]]   ## 3x3 2차원배열 
# # arr = range(1,19)   ##  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]



# # if num % 5 == 1:
# #     idx = 8
# #     for i in range(3):
# #         for j in range(3):
# #             lst[i][j] = arr[idx]
# #             idx -= 1

# # elif num % 5 == 2 :
# #     idx2 = 6
# #     for i in range(3) :
# #         for j in range(3):
# #             lst[i][j] = arr[idx2]
# #             idx2 += 1
# #         idx2 -= 6
# # else :
# #     idx3 = 9
# #     for i in range(3):
# #         for j in range(3):
# #             lst[i][j] = arr[idx3]   ## 9번 넣고, 12번 넣고, 15번 넣고  인덱스 3씩증가
# #             idx3 += 3                ## 10번 넣고,13번 넣고, 16번 넣고  인덱스 -5 감소후 3씩증가
# #         idx3 -= 8                            

# # ## 출력
# # for i in range(3):
# #     for j in range(3):
# #         print(lst[i][j], end = ' ')
# #     print()

# # 짝수 홀수 함수

# # a, b = map(int,input().split())

# # def printData(x):
# #     print(x)

# # def even(x):
# #     return printData(x*2)

# # def odd(x):
# #     return printData(x-10)


# # if (a//b) % 2 == 0 :
# #     even((a//b))
# # else :
# #     odd((a//b))
    
# # printData(a+b)

# # lst1 = [1,2,3,4,5]
# # lst2 = [6,7,8,9,10]

# # a =lst1 + lst2 
# # print(a)

# st = input()
# for i in st:
#     print(i)

# number=[1,2,3]
# ## List comprehension 활용
# st = ''.join(list(map(str,number)))
# print(st)

# arr = [[1, 2, 3], 
#        [4, 5, 6],
#        [7, 8, 9],
#        [10, 11, 12],
#       ]

# narr =[[n**2 for n in row] for row in arr]
# sarr = [n for i in arr for n in i]
# print(sarr)

##암호문자 출력하기
# lst= []
# for i in range(4):
#       lst.append(list(map(int,input().split())))

# for i in range(4):
#       for j in range(4):
#             if lst[i][j] % 2 == 0 and lst[i][j] != 0 :
#                   lst[i][j] = '#'
#                   print(lst[i][j],end = '')
#             elif lst[i][j] == 0:
#                   lst[i][j] = '!'
#                   print(lst[i][j],end='')
#             else :
#                   lst[i][j] = '@'
#                   print(lst[i][j],end = '')
      
#       print()

## 함수안에서 CountDown
# def INPUT():
#       num = int(input())
#       return num
# def CountDown(num):
#       for i in range(num,0,-1):
#             print(i,end= ' ')

# CountDown(INPUT())

# lst = [[0 for i in range(5)] for j in range(5)]
# n = 1
# for j in range(4,-1,-1):
#       for i in range(5):
#             lst[i][j] = n
#             n += 1

# number = int(input())
# for i in range(5):
#       lst[number][i] = number


# for i in range(5):
#       for j in range(5):
#             print(lst[i][j],end = ' ')
#       print()

# class Fruit():
#       def size():
#             size = int(input('과일의 사이즈를 입력하세요.'))
#             return size
#       banana_price = 250
#       apple_prince = 500
# apple =Fruit()
# banana = Fruit()
# a = apple.size()
# b = banana.size()

# def INPUT():
#       st =input()
#       if CHECK(st) == 1:
      
#             print('있음')
#       else:
#             print('없음')

# def CHECK(x):
#       for i in lst:
#             if i.count(x) != 0:
#                   return 1
#             else :
#                   return 2

# lst = [['D','A','C','C','D'],['S','D','F','A','E'],['E','E','T','J','H']]

# INPUT()

# arr = list(map(int,input().split()))

# lst = [[0 for i in range(4)] for j in range(3)]

# for i in range(3):
#       n = arr[i]
      
#       for j in range(4):
#             lst[i][j] = n  ## arr j = A
#             n += 1
#             print(lst[i][j],end = ' ')
      
#       print()
# lst = [[0 for i in range(3)] for j in range(6)]
# n = 10
# for i in range(3):
#       for j in range(6):
#             lst[j][i] = n  ## lst[0~5][0]
#             n += 1
# a, b = map(int,input().split())

# for i in range(a,b+1):
#       for j in range(3):
#             lst[i][j] = 7

# for i in range(6):
#       for j in range(3):
#             print(lst[i][j],end=' ')
#       print()

# def aToZ():
#       st = ord(input())
#       if st > 77.5 :          ## ord('Z')- ord('A') = 25
#             return 'Z'        ## 65+ 25/2 == 중간값
#       else:
#             return 'A'

# print(aToZ())

# def Calculator():
#       score = int(input())
#       if score >= 90 :
#             return 'A'
#       elif score >= 80:
#             return 'B'
#       elif score >= 70:
#             return 'C'
#       else :
#             return 'D'

# print(Calculator())

# arr = [[1,0,0,0,0],[1,0,1,0,0],[1,1,0,1,0],[1,0,1,0,0],[0,1,0,0,1],[0,0,0,1,0],[1,1,0,0,0]]



# def INPUT():
#       num = int(input())
#       return num

# def PROCESS(x):
#       ea = 0
#       for i in range(7):
#             if arr[i][x] == 1:
#                   ea += 1
#       return ea
      
# def OUTPUT(x):
#       print(x)

# OUTPUT(PROCESS(INPUT()))

## run 함수에서 2차배열 값 채우기

# def main():
#       num = int(input())
#       return num

# def run(x):
#       lst = [[0 for i in range(3)] for j in range(3)]
#       n = 1
#       if x < 10 :
#             for i in range(3):
#                   for j in range(3):
#                         lst[i][j] = n
#                         n += 1
                 
#       else :
#             n = 1
#             for i in range(3):
#                   for j in range(2,-1,-1):
#                         lst[i][j] =n     
#                         n += 1
              
#       for i in range(3):
#             for j in range(3):
#                   print(lst[i][j],end ='')
#             print()
# run(main())


# def yesOrNo():
#       num = int(input())
#       if num % 3 == 0:
#             return 7
#       elif num % 3 == 1:
#             return 35
#       else :
#             return 50

# print(yesOrNo())

## 함수로부터 값 보내고 받기

# def Input():
#       num = int(input())
#       return num

# def calc (x,):
#       lst = list(map(int,input().split()))
#       return sum(lst)


# a = Input()
# b = Input()
# c = Input()

# def sum(a,b):
#       return a+b

# def comp(a,b):
#       return a-b

# def Print(a,b):
#       print(f'합:{a}')
#       print(f'차:{b}')

# a, b = map(int,input().split())

# hap =sum(a,b)
# cha = comp(a,b)
# Print(hap,cha)

# a, gd = map(str,input().split())
# a = int(a)
# gd = str(gd)


# p = a
# t = gd
# print(p, t)

# a,b,c = input().split()

# print(chr(ord(a)+1),chr(ord(b)+1),chr(ord(c)+1))
# # 
# lst = list(map(int,input().split()))

# print('''MAX={0}
# MIN={1}'''.format(max(lst),min(lst)))

# lst = list(input().split())

# big = []
# small =[]

# for i in lst:
#       if 65 <= ord(i) <= 90:
#             big.append(i)
#       elif 97 <= ord(i) <= 122:
#             small.append(i)
# a= ''.join(big)
# b = ''.join(small)


# print(f'big={a}')
# print(f'small={b}')

# lst = [[3,2,6,2,4],[1,4,2,6,5]]

# num = int(input())
# def KFC(x):
#       if x in lst[0] or x in lst[1]:
#             return 1
#       else :
#             return 0

# if KFC(num) == 1:
#       print('값이 존재합니다')
# else :
#       print('값이 없습니다')

# lst = list(map(str(input().split(''))))
# print(lst)

# lst = [[1,3,6,2],[4,2,4,5],[6,3,7,3],[1,5,4,6]]

# num = int(input())

# select = []

# for i in range(4):
#       for j in range(4):
#             if lst[i][j] > num:
#                   select.append(lst[i][j])
#                   print(lst[i][j],end = ' ')

# a,b=map(int,input().split())

# a,b = b,a
# print(b,a)

## 범위에 드는 문자 찾기

# lst = ['D','F','G','D','A','Q']

# a, b = input().split()
# scope = range(ord(a),ord(b)+1)
# ea = 0
# for i in lst:
#       if ord(i) in scope:
#             print('발견!!!')
#             break
#       else:
#             ea += 1
# if ea == 6 :
#       print('미발견!!!')


## 배열에 숫자 Counting 하기
# lst = [[1,1,1],[1,2,1],[3,6,3]]

# def Count(x):
#       ct = 0
#       for i in lst:
#             ct += i.count(x)
#       return ct
# num = int(input())
# print(Count(num))

# lst =list('A1115Awz')

# st = input()

# num = lst.count(st)

# if num == 3 :
#       print('THREE')
# elif num == 2:
#       print('TWO')
# elif num == 1:
#       print('ONE')
# else :
#       print('NOTHING')

## 입력받은 글자를 세밀히 세보기

# lst = [['a','b','a','c','z'],['c','t','a','c','d'],['c','c','c','c','a']]

# st = input()
# ea = 0 
# for i in lst:
#       ea += i.count(st)

# if ea >= 7 :
#       print('세상에')
# elif ea >= 5 :
#       print('와우')
# elif ea >= 3 :
#       print('이야')
# else : 
#       print('이런')

## 글자 바꾸어서 출력하기

# lst = list(map(int,input().split()))

# arr = [[0 for i in range(3)] for j in range(2)]
# n = 0
# for i in range(2):
#       for j in range(3):
#             arr[i][j] = lst[n]
#             if lst[n] == 0:
#                   print('#',end='')
#             else :
#                   print(lst[n],end='')
#             n += 1
#       print()            
            
# lst = [['a','b','E'],['E','2','W'],['3','2','4']]

# for i in range(3):
#       for j in range(3):
#             if lst[i][j].islower():
#                   print(lst[i][j].upper(),end = ' ')
            
#             elif lst[i][j].isupper():
#                   print(lst[i][j].lower(),end = ' ')
            
#             else:
#                   print(chr(ord(lst[i][j])+5),end = ' ')
#       print()

# lst = [['a','b','d'],['e','w','z'],['q','v','a']]

# def Input():
#       st = input()
#       Process(st)

# def Process(x): 
#       low_x = x.lower()
#       ea = 0
#       for i in lst:
#             ea += i.count(low_x)
#       if ea != 0:
#             print('존재')
#       else:
#             print('없음')
# Input()

##배열값을 바꾼 후 MAX + MIN 구하기

# lst =[[3,1,6],[7,8,4],[9,2,3]]

# a,b,c = map(int,input().split())

# lst[a][b] = c


# maxlst = []
# for i in lst:
#       maxlst.append(max(i))
#       M = max(maxlst)

# minlst =[]
# for i in lst:
#       minlst.append(min(i))
#       m = min(minlst)

# print(M+m)

## 다른 배열에 값 옮기기
# default_lst = [[0 for i in range(3)] for j in range(2)]
# lst = list(map(int,input().split()))
# idx = 0
# new_lst = []
# for i in range(1,-1,-1):
#       for j in range(2,-1,-1):
#             default_lst[i][j] = lst[idx]
#             idx += 1
# idx = 0
# for i in range(2):
#       for j in range(3):
#             new_lst.append(default_lst[i][j])
#             idx += 1

# new_lst[0],new_lst[5] = new_lst[5],new_lst[0]

# print(*new_lst)


## 문장 입력받고 출력하기

# st =input()

# for i in range(5):
#       print(st)

## 두 문장의 길이는?

# char1, char2 = input(), input()

# print(len(char1),len(char2))

## 네 줄 카운트다운

# num = int(input())

# for i in range(4):
#       for j in range(4):
#             print(num,end='')
#       num -= 1      
#       print()

## one two three 빌딩

# num = int(input())
# a = 1
# for i in range(num):
#       for j in range(3):
#             print(a,end='')
#             a += 1
#       a = 1
#       print()

## 중첩 for문 활용하기

# num = int(input())

# lst = [[0 for i in range(4)] for j in range(3)]

# for i in range(3):
#       for j in range(4):
#             if  (i == 0 and (j == 0 or j == 1)) or (i == 1 and j == 0) :
#                   print(' ',end ='')
#                   continue
#             lst[i][j] = num
#             print(lst[i][j],end ='')
#             num += 1
#       print()

## 문자의 위치를 구해주는 함수 만들기

# lst = list('MINQUEST')

# def Length(x):
#       return lst.index(x)

# a1 = input()
# a2 = input()
# a3 = input()

# print(f'{a1}={Length(a1)}')
# print(f'{a2}={Length(a2)}')
# print(f'{a3}={Length(a3)}')

## 문장에서 세 문자 counting
# st = input()

# s1 = input()
# s2 = input()
# s3 = input()

# res1 = st.count(s1)
# res2 = st.count(s2)
# res3 = st.count(s3)

# print(f'{s1}={res1}')
# print(f'{s2}={res2}')
# print(f'{s3}={res3}')

## 범위 내 문자들 따로 빼두기

# lst = list('DATAPOWER')
# arr = []

# a, b = list(map(int,input().split()))
# flag = a <= b

# if flag:
#       arr.append(lst[a:b+1])

# print(''.join(arr[0]))

## 중첩 2중 FOr문으로 배열 채우기

# lst = [[0 for i in range(3)] for j in range(3)]

# num = input()

# if num.isdigit() == True :
#       start = 6
#       for i in range(3):
#             for j in range(3):
#                   if (i == 1 and j == 0) or (i == 2 and (j == 0 or j == 1)):
#                         continue
#                   lst[i][j] = start
#                   start -= 1

# elif num.isupper():
#       start = 1
#       for i in range(2,-1,-1):
#             for j in range(3):
#                   if (i == 0 and (j == 1 or j == 2)) or (i == 1 and j == 2):
#                         continue
#                   lst[i][j] = start
#                   start += 1

# for i in range(3):
#       for j in range(3):
#             if lst[i][j] == 0 :      
#                   print(' ',end = '')
#             else :
#                   print(lst[i][j],end ='')
#       print()

## 한줄로 문자 채우기

# a,b = list(input().split())

# I =int(a)-1
# S_num = ord(b)
# lst = [[0 for i in range(5)] for j in range(5)]

# for i in range(4,-1,-1):
#       lst[I][i] = chr(S_num)
#       S_num += 1

# for i in range(5):
#       for j in range(5):
#             print(lst[i][j],end='')
#       print()

## 배열에서 입력받은 값 찾아내기

# lst = [['D','A','D'],['Q','W','Q'],['A','S','D'],['A','S','D']]

# st = input()


# def Find(x):
#       not_in = 0
#       for i in lst:
#             if x not in i:
#                   not_in += 1
#                   continue
#             else :
#                   print('존재')
#                   break
#       if not_in == 4 :
#             print('없음')

# Find(st)

## 테두리 채우기

# lst = [[0 for i in range(5)] for j in range(5)]

# num = int(input())

# for i in range(5):
#       for j in range(5):
#             if (j in range(1,4)) and (i in range(1,4)):     ## 1,2,3행의 1,2,3열일때
#                   print('_',end ='')
#             else:
#                   lst[i][j] = num
#                   print(num,end='')
            
            
            
#       print()

## 마법의 현황판  

# 좌표입력 값에 1더하고 만약 좌표값이 10이되면 0으로 초기화. (5번반복)

# magic_lst = [[4,5,4,5,4],[8,9,8,9,8],[1,2,1,2,1],[4,5,4,5,4],[6,7,6,7,6]]

# for i in range(5):
#       y,x = list(map(int,input().split()))
#       magic_lst[y][x] = magic_lst[y][x] + 1
      
#       if magic_lst[y][x] == 10 :
#             magic_lst[y][x] = 0           ## 좌표값 초기화

# for i in range(5):
#       for j in range(5):
#             print(magic_lst[i][j],end='')
#       print()

# st =input()

# print(len(st))
# print(st.count(st[-1]))

# a1 = input()
# a2 = input()
# a3 = input()
# lst = [a1,a2,a3]

# def INdex():
#       temp = []
#       for i in lst:
            
#             temp.append(len(i))
#       return temp.index(max(temp))

# print(lst[INdex()])

## 중첩 2중으로 배열 채우기

# lst = [[0 for i in range(3)] for i in range(3)]
# num = int(input())

# for i in range(3):
#       for j in range(3):
#             if (i == 0 and (j == 0 or j == 1)) or (i == 1 and j == 0):
#                   print(lst[i][j],end='')
#                   continue
#             else :
#                   lst[i][j] = num
#                   print(lst[i][j],end='')
#                   num += 1
#       print()

# def getName():
#       st1,st2 = input().split()
#       return st1,st2
# st1, st2 = getName()
# if ord(st1) < ord(st2) :
#       print(st1)
# else:
#       print(st2)

## Call by reference 저주의 점술사

# def moom(x):
#       return x-4, x+3,x*2

# age = int(input())

# a,b,c = moom(age)

# print(a,b,c)

# st = input()

# def stringLen(x):
#       return len(x)
# print(f'{stringLen(st)}글자')

# a, b = map(int,input().split())

# def ABC(x,y):
#       return x+y,x*y

# print(*ABC(a,b))

## 문자 개수 세 주는 함수 만들기

# def KFC():
#       st = input()
#       uc = 0
#       lc = 0
#       for i in st:
#             if i.isupper():
#                   uc += 1
#             elif i.islower():
#                   lc += 1
#       return uc,lc

# uppercase, lowercase = KFC()

# print(f'대문자{uppercase}개\n소문자{lowercase}개')


## 좋아하는 숫자 찾기

# lst = [[4,5,6,1,3,1],[2,1,3,6,3,6]]

# def Input():
#       global num
#       num = list(map(int,input().split()))
#       return num

# def Process(x):
#       temp = []
      
#       for i in x:
#             cot = 0
#             for j in lst:
#                   cot += j.count(i)
#             temp.append(cot)
#       return temp

# def Output(x):
#       print(f'{num[0]}={x[0]}개')
#       print(f'{num[1]}={x[1]}개')
#       print(f'{num[2]}={x[2]}개')

# Output(Process(Input()))

## 좌표값 찾아주는 함수 만들기

# lst = [['A','D','F'],['Q','W','E'],['Z','X','C']]

# def Find(x):
#       i_idx = -1
#       for i in lst:
#             i_idx += 1
#             for j in i:
#                   if st in i:
#                         j_idx = i.index(st)
#                         return i_idx,j_idx
                  

# st = input()

# print(f'{Find(st)[0]},{Find(st)[1]}')

# lst = [3,5,1,2,7]

# arr = list(map(int,input().split()))

# def CompareGo(x,y):
#       flag = x == y
#       if flag:
#             print('두배열은완전같음')
#       else:
#             print('두배열은같지않음')


# CompareGo(lst,arr)

# T,M = list(map(int,input().split()))
# cook = int(input())
# Time = T * 60 + M + cook
# if Time >= 24*60 :
#       print(0,Time % 60)
# else :
#       print(f'{Time//60} {Time%60}')



## 너와 나의 거리 구하기

# lst = input().split()
# st1 = max(lst)
# st2 = min(lst)
# distance = [4,2,5,1,6,7,3]

# idx1 = ord(st1) - 65
# idx2 = ord(st2) - 65


# result = sum(distance[idx2+1:idx1])

# print(result)

# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# C = list(map(int,input().split()))
# new = []
# for i in range(5):
#       new.append(A[i]*B[i]+C[i])

# print(*new)

# lst = [[3,4,1,6],[3,5,3,6],[0,0,0,0],[5,4,6,0]]

# arr = list(map(int,input().split()))
# lst[2] = arr
# Max = 0 
# Min = 99999 
# for i in lst:
#       for j in i:
#             if j >= Max :
#                   Max = j
#             elif j <= Min:
#                   Min = j

# break_point = False
# for i in range(4):
#       for j in range(4):
#             if lst[i][j] == Max:
#                   Mi = i
#                   Mj = j
#                   break_point = True
#                   break
#       if break_point == True:
#             break

# break_point = False
# for i in range(4):
#       for j in range(4):
#             if lst[i][j] == Min:
#                   mi = i
#                   mj = j
#                   break_point = True
#                   break
#       if break_point == True:
#             break
      
            

# print(f'MAX={Max}({Mi},{Mj})\nMIN={Min}({mi},{mj})')


# def abc():
#       print('#')
#       for i in range(114):
#             print('@')

# a=3
# b=3
# a=7
# a=78
# b=2
# abc()
# a=64
# b=12

# lst = [['4','5','7','1','3','2'],['D','F','Q','W','G','Z']]

# num = int(input())

# num = str(num)

# idx = lst[0].index(num)
# print(lst[1][idx])

# def FindABC(sen1,sen2):
#       nA = sen1.count('A') + sen2.count('A')
#       nB = sen1.count('B') + sen2.count('B')
#       nC = sen1.count('C') + sen2.count('C')
      
#       return nA,nB,nC

# def main():
#       sent1 = input()
#       sent2 = input()
#       A,B,C = FindABC(sent1,sent2)

#       print(f'A:{A}')
#       print(f'B:{B}')
#       print(f'C:{C}')

# main()

## 좌표를 지정하면 값 반환하기

# lst = [['D','A','S'],['Q','W','V'],['R','T','Y']]



# def Find(y,x,z,r):
#       return lst[y][x], lst[z][r]

# def main():
#       y1,x1 = map(int,input().split())
#       y2,x2 = map(int,input().split())

#       print(*Find(y1,x1,y2,x2))

# main()

# person1 = input()
# person2 = input()
# person3 = input()

# flag = person1 == person2 == person3

# if flag:
#       print('YES')
# else :
#       print('NO')


# a, b = map(int,input().split())

# while a <= b:
#       print(a,end = ' ')
#       a += 1


# apartment = []

# for i in range(5):
#       F = list(map(int,input().split()))
#       temp = []
#       for j in F:
#             temp.append(j)
#       apartment.append(temp)


# result = []
# for i in range(5):
#       hap = 0 
#       for j in range(4):
#             hap += apartment[i][j]
#       result.append(hap)

# print(*result)

# lst = list(map(str,input().split()))
# n = 0
# for i in range(1):
#       for j in range(5):
#             print(*lst[n:])
#             n += 1


# waffle = []
# for i in range(3):
#       temp = list(map(int,input().split()))
#       waffle.append(temp)
# n = 0 
# res = 0
# for i in waffle:
#       res += sum(i[:n+1]) 
#       n += 1
      

# print(res)

# vect =  [3,5,1,1,2,3,2]

# lst = list(map(int,input().split()))

# for i in lst:
#       temp = vect.count(i)
#       print(f'{i}={temp}개')

# lst = list(map(int,input().split()))

# lst.sort(reverse=True)


# print(''.join(map(str,lst)))

# sen = input()

# new_sen = sorted(sen)

# print(''.join(new_sen))

# lst = [10,50,40,20,30,40]

# arr = list(map(int,input().split()))
# res = 0
# for i in arr:
#       temp = list(filter(lambda x:x>i,lst))
#       print(f'{i}={len(temp)}개')

# tri = int(input())

# lst = []

# for i in range(5):
#       temp = list(map(int,input().split()))
#       lst.append(temp)

# if tri == 1:
#       n = 0
#       for i in lst:
#             print(*i[:n+1])
#             n += 1

# elif tri == 2:
#       n = 5
#       for i in lst:
#             print(*i[:n])
#             n -= 1

# num = int(input())
# i = 0

# while i < 3:
#       j = 0
#       while j < 5:
#             print(num,end='')
#             j += 1
#       print()
#       i += 1

# a = input()
# b = input()

# sen1 = list(a)
# sen2 = list(b)
# sen1.sort()
# sen2.sort()
# dic_sen1 = ''.join(sen1)
# dic_sen2 = ''.join(sen2)


# print(dic_sen1+dic_sen2)

# lst = [[0 for i in range(3)] for j in range(3)]

# Magic(*lst)

# Output(*lst)


# def Magic(*arr_txt):
#       num = 1
#       for i in range(3):
#             for j in range(3):
#                   arr_txt[i][j]=num
#                   num += 1 
            

# lst = list(input().split())
# lst2 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

# for i in range(5):
#     for j in range(5):
#         lst2[i][j-i] = lst[j]  ##lst2[1][j-1] = lst[j]

# for i in range(1, 5):
#     for j in range(4-i+1, 4+1):
#        lst2[i][j] = ''

# for i in lst2:
#     print(*i)


# st = list(map(str,input().split()))

# for i in range(5):
#       for j in range(5):
#             st[i][j-i]


# lst = [[' ' for i in range(3)] for j in range(3)]


# def Magic(arr):
#       num = 1

#       for i in range(3):
#             for j in range(3):
#                   if (i == 1 and j == 0) or (i == 2 and (j == 0 or j == 1)):
#                         continue
#                   else:
#                         arr[i][j] = num
#                         num += 1
#       return arr

# def Output(arr):
#       for i in range(3):
#             for j in range(3):
#                   print(arr[i][j], end ='')
#             print()

# Output(Magic(lst))

# sen1 = input()
# sen2 = input()

# if sen1 == sen2 :
#       print('같음')
# else :
#       print('다름')


# sen1 = input()
# sen2 = input()
# break_point = True
# if len(sen1) == len(sen2):
#       for i in range(len(sen1)):
#             if sen1[i] == sen2[i]:
#                   continue
#             else:
#                   print('다름')
#                   break_point = False
#                   break
# else:
#       print('다름')
#       break_point = False

# if break_point == True:
#       print('같음')

## 숫자 쪼개기


'''## 찬석님 코드 mincoding 14- waffle 전문제
lst = list(map(int,list(input())))

print(lst)

def main():
    arr = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    result = Magic(arr)
    Output(result)

def Magic(arr):
    num = 1
    x = 0
    for i in range(len(arr)):
        for j in range(len(arr[i]) - x):
            arr[i][j + x] = num
            num += 1
        x += 1
    return arr

def Output(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            print(x[i][j], end = '')
        print('')

main()

'''

# lst = list(map(int,list(input())))

# for i in range(len(lst)):
#       print(f'숫자{lst[i]}')

## 너와 나와의 거리

# scores_list = list(map(int,input().split()))

# temp = 0
# for i in range(len(scores_list)-1):
#       if abs(scores_list[i]-scores_list[i+1]) < 3:
#             temp += 1
#       else :
#             print('재배치필요')
#             break

# if temp == len(scores_list)-1:
#       print('완벽한배치')
      
# st1 = input()
# st2 = input()

# if st1[::-1] == st2:
#       print('거울문장')
# else:
#       print('거울문장아님')
      

## 문장의 길이를 정렬하기

## 문장의 길이를 정렬하기

# lst = [[input()] for i in range(4)]        

# len_list = []

# for i in lst:
#       len_list.append(len(i[0]))

# len_list.sort()

# print(*len_list)

## 개구리문장 판별하기

# sen = input()
# temp1=str()
# temp2=str()
# for i in sen[::2]:
#     temp1 += i
# for i in sen[1::2]:
#     temp2 += i

# if temp1.isupper() and temp2.islower():
#     print('개구리문장')
# elif temp1.islower() and temp2.isupper():
#     print('개구리문장')
# else:
#     print('일반문장')

## 범죄자 찾아내기

# lst = list('ABCZETQ')

# black_list = list(input())

# for i in black_list:
#     if i in lst:
#         print(f'{i}=마을사람')
#     else:
#         print(f'{i}=외부사람')

## 다섯 문장 중 가장 긴 문장 찾기

# lst = [[input()] for i in range(5)]


# max_len = lst[0][0]
# for i in range(5):
#     if len(max_len) <= len(lst[i][0]):
#         max_len = lst[i][0]
    
# print(max_len)

# st1 = "BBQWORLD"
# st2 = "KFCAPPLE"
# st3 = "LOT"

# st = input()
# sum = 0
# for i in [st1,st2,st3]:
#     sum += i.count(st)

# print(sum)

# def main():
#     a = list(input())
#     b = list(input())
#     c = list(input())
#     CountLine(a,b,c)

# def CountLine(x,y,z):
#     for i in [x,y,z]:
#         a= ''.join(i)
#         print(f'{len(i)}={a}')

# main()



# a = input()
# lst = [[a for i in range(4)] for j in range(4)]

# print(lst)

# lst = [[input()] for i in range(4)]

# temp = []
# for i in lst:
#     temp.append(i[0])

# sumstring = ''.join(temp)

# if 'A' in sumstring and 'B' in sumstring:
#     print('대발견')
# elif 'A' in sumstring or 'B' in sumstring:
#     print('중발견')
# else:
#     print('미발견')

# lst = [[input()] for i in range(2)]

# char = [] 
# for i in lst :
#     for j in range(len(i[0])):
#         char.append(i[0][j])
    
# print(''.join(char))

# lst = [list('DATAW'),list('BBQK')]

# num = int(input())
# if num % 2 == 1:
#     lst[0].sort()
# else:
#     lst[1].sort()

# fline = ''.join(lst[0])
# sline = ''.join(lst[1])
# print(f'{fline}\n{sline}')

##

# lst = [list('POTIO'),list('ABCDE'),list('YOURE')]

# a, b = map(int,input().split())

# for i in range(3):
#     st = ''.join(lst[i][a:b+1])
#     print(st,end ='')

## 두 문장 중 같은 문장의 갯수 세기

# lst = [[input()] for i in range(2)]

# len_lst =[len(lst[0]),len(lst[1])]
# max_len = max(len_lst)

        


# lst = [[' ' for i in range(8)] for j in range(2)]

# diff = 0 

# for i in range(2):
#     st = list(input())
#     for j in range(len(st)):
#         lst[i][j] = st[j]


# for j in range(8):
#     if lst[0][j] != lst[1][j]:
#         diff += 1

# print(diff)

## 이중 while로 배열에 값 채우기

# st = input()
# 

# i = -1

# x = 3
# y = 0
# while i < x:
#     i += 1
#     j = 2
#     while j >= y:
        
#         lst[i][j] = st
#         j -= 1
#     y -= 1
    
    

# print(lst)
# lst = [[0 for i in range(3)] for j in range(3)]
# st = input()
# num = ord(st)
# i = 3

# x = 0
# while i >= 1:
#     j = 0
#     i -= 1
#     while j <= x:
#         lst[i][j] = chr(num)
#         j += 1
#         num += 1
#     x += 1

# i = -1

# while i < 2:
#     i += 1
#     j = 0
#     while j <= 2:
#         if lst[i][j] == 0 :
#             print(' ',end ='')
#             j += 1
#         else:    
#             print(lst[i][j],end = '')
#             j += 1
#     print()

# print('HELLO WORLD')

# lst = [[5,1,4,2,6],[3,5,0,0,7],[9,9,8,3,1]]

# num = int(input())
# res = 0
# for i in lst:
#     res += len(list(filter(lambda x:x>num,i)))

# print(f'{res}개')

# lst = [[0 for i in range(4)] for j in range(3)]

# num = int(input())
# n = 1
# for i in range(2,-1,-1):
#     for j in range(3,-1,-1):
#         lst[i][j] = n
#         n += 1


# for j in range(4):
#     if num == 1:
#         lst[0][j] = 7
#     elif num == 2:
#         lst[1][j] = 7
#     elif num == 3:
#         lst[2][j] = 7
    
# for i in range(3):
#     for j in range(4):
#         print(lst[i][j],end = ' ')
#     print()
        

## 그가 사는 그집

# juso =[[402],[401],[302],[301],[202],[201],[102],[101]]
# name = [['K','I','M'],['T','E','A'],['S','O','M'],['O','P','P','O'],['T','O','M'],['G','D','K'],['J','A','M','E'],['M','I','N']]

# num = int(input())

# ho = juso.index([num])
# people = ''.join(name[ho])
# print(people)

# a,b,c = map(int,input().split())

# for i in range(c):
#     for j in range(b):
#         print(a,end=' ')
#         a += 1
#     print()
#     a -= b

# lst = [0 for i in range(9)]
# for i in range(3):
#     start_index,end_inedx = map(int,input().split())
    
#     for idx in range(start_index,end_inedx+1):
#         lst[idx] += 1

# print(*lst)

# lst = [list(map(int,input().split())) for i in range(2)]

# arr = [0 for i in range(6)]
# idx = 0
# for i in range(2):
#     for j in range(3):
#         arr[idx] = lst[i][j]
#         idx += 1

# arr.sort()

# idx = 0
# for i in range(2):
#     for j in range(3):
#         lst[i][j] = arr[idx]
#         print(lst[i][j],end = ' ')
#         idx += 1
#     print()


## 선택한 칸 모두 출력하기

# lst = [list('FRQWT'),list('GASYQ'),list('ASADB')]

# num = int(input())

# join = lst[0][num],lst[1][num],lst[2][num]

# v_str = ''.join(join)
# print(v_str)

## 알파벳 퀴즈
# correct = list('APPLET')

# answer = input().split()

# bingo = 0
# for i in answer:
#     bingo += correct.count(i)

# print(f'{bingo}개 맞추었습니다')

## 번호 순서대로 배열 채우기

# lst = [[0 for i in range(4)] for j in range(4)]
# num = int(input())
# x =range(4)
# y =range(3,-1,-1)
# for i in range(4):
#     for j in x:
#         lst[i][j] = num       
#         num += 1
#     x,y=y,x

# for i in range(4):
#     for j in range(4):
#         print(lst[i][j], end = ' ')
#     print()

## 꼬리찾기
# lst = []
# for i in range(3):
#     temp = list(input())
#     lst.append(temp)
    
# for i in lst:
#     print(i[-1], end ='')


## 내가 좋아하는 문자의 수

# lst = [['A','B','K','T'],['K','F','C','F'],['B','B','Q','Q'],['T','P','Z','F']]
# st1, st2 = map(str,input().split())

# st_lst = ''.join([''.join(i) for i in lst])

# cnt = 0 

# cnt += st_lst.count(st1)
# cnt += st_lst.count(st2)

# print(cnt)

## 문장 A 추가하기

# st = list(input())
# num = int(input())

# st.insert(num,'A')

# print(''.join(st))

## 두 개의 배열의 누적의 합

# A = list(map(int,input().split()))
# B = list(map(int,input().split()))

# result = []
# for i in range(1,5):
#     result.append(A[i-1] + B[-i])
#     print(result[i-1], end = ' ')

## 잡초문자 제거하기

# st = list(input())
# idx = int(input())

# st.remove(st[idx])

# print(''.join(st))

## 배열의 누적합 구하기

# lst = list(map(int,input().split()))

# for i in range(len(lst)-1):
#     hap = lst[i]+lst[i+1]
#     lst[i+1] = hap
    
# print(*lst)
    
## M이 존재합니까?

# no_cnt = 0
# for i in range(3):
#     st = input()
#     flag = 'M' in st
#     if flag:
#         print('M이 존재합니다')
#         break
#     else:
#         no_cnt += 1
#
# if no_cnt == 3:
#     print('M이 존재하지 않습니다')

# a, b, c = map(int,input().split())
#
# for i in range(c):
#     for j in range(a, b+1):
#         print(j, end=' ')
#     print()


# arr = [4,7,3,1,2]
# lst = []

# for i in range(5):
#     lst.append(arr[i])
#     for j in range(i):
#         if lst[i] < lst[j]:
#             lst[i],lst[j] = lst[j],lst[i]

# print(lst)

# lst = [[0 for i in range(3)] for j in range(6)]
# st_num = 65
# for j in range(2,-1,-1):
#     for i in range(5,-1,-1):
#         lst[i][j] = chr(st_num)
#         st_num += 1

# i, j = map(int,input().split())

# print(lst[i][j])


## 함수에 주소 넘기기 복습!

# lst = [[0 for i in range(3)] for j in range(2)]
# arr = list(map(int,input().split()))
# idx = 0
# for i in range(2):
#     for j in range(3):
#         lst[i][j] = arr[idx]
#         idx += 1

# def maxV(arr):
#     maxv = arr[0]
#     for i in range(len(arr)):
#         if maxv < arr[i]:
#             maxv = arr[i]
#         return maxv
    
# def minV(arr):
#     minv = arr[0]
#     for i in arr:
#         if minv > i:
#             minv = i
#         return minv

# for i in range(2):
#     for j in range(3):
#         if lst[i][j] == maxV(arr):
#             MaxV = (i,j)
            
#         elif lst[i][j] == minV(arr):
#             MinV = (i,j)
            
# print(MaxV)
# print(MinV)


# lst= [[4, 5, 2, 6, 7],
#       [2, 9, 9, 6, 1],
#       [2, 9, 9, 6, 1]]

# def isin(x):
#     cnt = 0
#     for i in lst:
#         if x in i:
#             cnt += 1
#     if cnt > 0 :
#         print('Y',end =' ')
#     else:
#         print('N',end =' ')



# for i in range(2):
#     a, b = map(int,input().split())
#     isin(a)
#     isin(b)
#     print()

'''이차원 배열에 패턴이 몇개 존재 하는지 출력하기

AB
TT
발견2개
'''
# board = [
#     ['A','B','G','K'],
#     ['T','T','A','B'],
#     ['A','C','T','T']]

# st = [list(input()) for i in range(2)]
# print(st)
# def check(x,y):
#     if board[x][y:y+2] == st[0]:
#         return 1
#     else:
#         return 0
    

# cnt = 0
# for i in range(3):
#     for j in range(3):
#         cnt += check(i,j)
        
# if cnt > 0 :
#     print(f'발견{cnt}개')
# else:
#     print(f'미발견')
# def findptn(by,bx):
#     for dy in range(2):
#         for dx in range(2):
#             if board[by+dy][bx+dx]!=st[dy][dx]:
#                 return 0
#     return 1
            
# cnt = 0 
# for i in range(2):
#     for j in range(3):
#         if findptn(i,j):
#             cnt += 1 

# if cnt:
#     print(f'발견 {cnt}개')
# else:
#     print('미발견')

## 성실한 직원 찾기

# bucket = [0 for i in range(65535)]

# arr = [[65000,35,42,70],[70,35,65000,1300],[65000,30000,38,42]]

# for i in range(3):
#     for j in range(4):
#         bucket[arr[i][j]] += 1

# maxV = bucket[0]           ## 제일 큰 번호 찾기
# for i in range(65535):
#     if maxV < bucket[i]:
#         maxV = bucket[i]
        
        
# for i in range(65535):     ## 제일 큰 번호 인덱스 찾고 프린트
#     if bucket[i] == maxV:
#         print(i)
#         break

## 안나오는 숫자는?

# lst  = [list(map(int,input().split())) for i in range(3)]

# bucket = [0 for i in range(10)]

# def check(x,y):
#     bucket[lst[x][y]] += 1
    
# for i in range(3):
#     for j in range(3):
#         check(i,j)
        

# for i in range(1,10):
#     if bucket[i] == 0 :
#         print(i, end=' ')

# lst = [[1,3,3,5,1],
#        [3,6,2,4,2],
#        [1,9,2,6,5]]

# N = int(input())

# bucket = [0 for i in range(10)]


# def check(x,y):
#     bucket[lst[x][y]] += 1
    
# for i in range(3):
#     for j in range(5):
#         check(i,j)

# for i in range(10):
#     if bucket[i] == N:
#         print(i,end=' ')

## 카드 종류 알아내기

# cardlist = list(input())

# DAT = [0 for i in range(26)]

# for i in range(len(cardlist)):
#     DAT[ord(cardlist[i])-65] += 1

# cnt = 0 
# for i in range(26):
#     if DAT[i] > 0:
#         cnt += 1

# print(f'{cnt}개')

## 인기 많은 알파벳

# st = list(input())

# DAT = [0 for i in range(26)]

# for i in st:
#     DAT[ord(i)-65] += 1

# maxV = 0    
# for i in DAT:
#     if maxV < i:
#         maxV = i

# for i in range(26):
#     if DAT[i] == maxV:
#         print(chr(i+65))
        
## 블랙리스트

# town = [['C','D','A'],
#         ['B','M','Z'],
#         ['Q','P','O']]

# black = list(input())

# cnt = 0
# for i in black:
#     for j in town:
#         if i in j:
#             cnt += 1
#             break

# print(f'{cnt}명')

## 한줄로 알파벳 정렬하기

# lst = [['A','B','C'],
#        ['A','G','H'],
#        ['H','I','J'],
#        ['K','A','B'],
#        ['A','B','C']]

# DAT = [0 for i in range(26)]

# for i in range(5):
#     for j in range(3):
#         DAT[ord(lst[i][j])-65] += 1
        
# alst = []
# for i in range(26):
#     if DAT[i] != 0:
#         alst.append(chr(65+i)*DAT[i])
    
# print(''.join(alst))

## 기차에서 우리팀 찾기

# train = [3,7,6,4,2,9,1,7]
# team = list(map(int,input().split()))
# for i in range(6):
#     if train[i:i+3] == team:
#         print(f'{i}번~{i+2}번 칸')

## 몇층에 있으세요?

# apt = [[15,18,17],
#        [4,6,9],
#        [10,1,3],
#        [7,8,9],
#        [15,2,6]]

# family = list(map(int,input().split()))

# def isPattern(num):
#     if family == apt[num]:
#         return 1
#     else:
#         return 0
    
# for i in range(5):
#     if isPattern(i):
#         print(f'{5-i}층')

## 가족을 찾아라

# lst = [['G','K','G'],input().split()]

# DAT = [0 for i in range(26)]

# for i in range(2):
#     for j in range(3):
#         DAT[ord(lst[i][j])-65] += 1

# cnt = 0
# for i in range(26):
#     if DAT[i] >= 3:
#         cnt += 1
    
# if cnt >= 1:
#     print('있음')
# else:
#     print('없음')

## 도플갱어

# lst = list(map(int,input().split()))

# maxV = 0
# for i in range(len(lst)):
#     if maxV < lst[i]:
#         maxV = lst[i]
        
# DAT = [0 for i in range(maxV+1)]

# for i in range(len(lst)):
#     DAT[lst[i]] += 1

# for i in DAT:
#     if i > 1:
#         print('도플갱어 발견')
#         break
# else:
#     print('미발견')

## 알파벳 카운팅

# st = input()
# lst = list(st)

# DAT = [0 for i in range(26)]

# for i in range(len(lst)):
#     DAT[ord(lst[i])-65] += 1

# maxV = DAT[0]
# for i in range(26):
#     if DAT[i] > maxV:
#         maxV = DAT[i]

# for i in range(26):
#     if DAT[i] == maxV:
#         print(chr(i+65))
    

## 하마의 충치

# teeth = [list(map(int,input().split())) for i in range(2)]
# cnt = 0

# for i in range(len(teeth[0])):
#     if teeth[0][i] == 1:
#         if teeth[1][i] == 1:
#             cnt += 1

# print(f'{cnt}개')

## 양쪽에서 아이찾기

# lst = list('ATKPTCABC')

# a, b = input().split()

# def lcheck(idx):
#     for i in range(len(lst)):
#         if lst[i] == idx:
#             return i
        
# def rcheck(idx):
#     for i in range(len(lst)-1,-1,-1):
#         if lst[i] == idx:
#             return i
        
# print(rcheck(b)- lcheck(a))
        

## 사법고시 합격자 발표

# win = [[3,5,1],
#        [4,2,1]]

# people = list(map(int,input().split()))


# for i in people:
#     cnt = 0
#     for j in win:
#         if i in j:
#             cnt += 1
#     if cnt > 0:
#         print(f'{i}번 합격')
#     else:
#         print(f'{i}번 불합격')
        
        
## 민코딩 찾기

# vect = list('MINCODING')

# n = int(input())
# st = list(input().split())
# DAT = [0 for i in range(26)]

# for i in vect:
#     DAT[ord(i)-65] += 1
    
# for i in range(n):
#     if DAT[ord(st[i])-65] > 0:
#         print('O',end='')
#     else:
#         print('X',end='')

## 다른 문장 입력 하기

# lst = [list(input()) for i in range(3)]

# DAT = [0 for i in range(26)]

# def check(str):
#     DAT[ord(str)-65] += 1
    
    
# for i in lst:
#     for j in range(len(i)):
#         check(i[j])

# for i in DAT:
#     if i > 1:
#         print('No')
#         break
# else:
#     print('Perfect')

## 중복 제거하기

# st = input()
# DAT = [0 for i in range(6)]

# for i in st:
#     DAT[ord(i)-65] += 1

# for i in range(6):
#     if DAT[i] >= 1:
#         print(chr(i+65),end='')

## 각 글자수 세기

# st = list(input())
# DAT = [0 for i in range(26)]

# for i in st:
#     DAT[ord(i)-65] += 1

# for i in range(26):
#     if DAT[i] != 0:
#         print(f'{chr(i+65)}:{DAT[i]}')
        
## 유령은 존재 할까?

# st = input()

# if 'GHOST' in st:
#     print('존재')
# else:
#     print('존재하지 않음')

# st = list(input())

# for i in range(len(st)):
#     idx = i
#     if st[idx] == 'G':
#         idx += 1
#         if st[idx] == 'H':
#             idx += 1
#             if st[idx] == 'O':
#                 idx += 1
#                 if st[idx] == 'S':
#                     print('존재')

## Direct 사용하기

# lst = [[3,5,4],[1,1,2],[1,3,9]]

# y,x = map(int,input().split())

# ii = [0,1,0,-1]
# ji = [1,0,-1,0]
# temp = [] 
# for i in range(4):
    