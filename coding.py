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

lst = [[1,3,6,2],[4,2,4,5],[6,3,7,3],[1,5,4,6]]

num = int(input())

select = []

for i in range(4):
      for j in range(4):
            if lst[i][j] > num:
                  select.append(lst[i][j])
                  print(lst[i][j],end = ' ')

a,b=map(int,input().split())

a,b = b,a
print(b,a)