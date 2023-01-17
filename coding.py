# 2023-01-17 Home study

#Call by value 
# def main():
#     a,b =map(int,input().split())
#     BBQ(a,b)

# def BBQ(x,y):
#     print(f'합:{x+y}')
#     print(f'차:{x-y}')
#     print(f'곱:{x*y}')
#     print(f'몫:{x//y}')

# main()

# #Call by value2
# global lst
# lst = [['F', 'E', 'W'], ['D', 'C', 'A']]

# def main():
#     s = input()
#     findCh(s)

# def findCh(x):
#     if lst[0].count(x) >= 1 or lst[1].count(x) >= 1:
#         print('발견')
#     else:
#         print('미발견')

# main()

#탐색하며 호출하기

# lst = input().split()

# def checkChar(Char):
#     if 65 <= ord(Char) <= 90:
#         print('대', end = '')
#     elif 97 <= ord(Char) <=122:
#         print('소', end = '')

# for i in lst:
#     checkChar(i)

# 구조체 변수 어러개 만들기

# class Person():
#     age = int()
#     height = int()

# a = Person()
# b = Person()

# def Input():
#     a.age ,a.height, b.age, b.height = list(map(int,input().split()))


# def Output():
#     age_avg = (a.age + b.age)//2
#     height_avg = (a.height + b.height)//2
#     print(age_avg,height_avg)

# Input()
# Output()


#어디에 숨었을까?

# lst = [2,1,2,4,5]
# arr = [[2,5,3],[4,5,7],[8,7,2]]

# num = int(input())
# ea = 0

# ea += lst.count(num)

# for i in range(3):
#     ea += arr[i].count(num)

# print(ea)

#Index 찾아내기

# lst = list(input().split())
# idx = list(filter(lambda x : lst[x] == 'A', range(5)))
# A_ea = lst.count('A')
# print(f'문자A는 {A_ea}개발견')

# for i in idx:
#     print(f'{i}번')

#2차배열에서 좌표 출력하기

# arr = [['D','A','A'],['B','C','D'],['E','F','A'],['A','A','D'],['F','G','E']]

# s = input()

# for i in range(5):
#     for j in range(3):
#         if arr[i][j] == s :
#             print(f'({i},{j})')

# 2차배열에서 범위안에 있는 값 세기

# arr = [[10,3,20],[60,30,40],[20,30,40]]

# a, b = list(map(int,input().split()))
# result = 0
# for i in range(3):
#     for j in range(3):
#         if a <= arr[i][j] <= b:
#             result += 1
# print(result)

#각 함수에서 대소문자 찾기

# def Input():
#     global arr
#     arr = [[0,0,0],[0,0,0]]
#     lst = input().split()
#     s = 0
#     for i in range(2):
#         for j in range(3):
#             arr[i][j] = lst[s]
#             s += 1
    


# def findUpper():
#     Uc = 0
#     for i in arr:
#         for j in range(3):
#             if 65 <= ord(i[j]) <= 90:
#                 Uc += 1
#     print(f'대문자{Uc}개')

# def findLower():
#     Lc = 0
#     for i in arr:
#         for j in range(3):
#             if 97 <= ord(i[j]) <= 122:
#                 Lc += 1
#     print(f'소문자{Lc}개')

# def main():
#     Input()
#     findUpper()
#     findLower()

# main()

#N의배수인 숫자 찾기

# arr = [[3,5,14],[2,3,9],[6,2,7]]

# num = int(input())
# sum = 0
# if num != 0 :
#     for i in arr:
#         a = list(filter(lambda x : i[x] % num == 0, range(3)))
#         sum += len(a)
# else:
#     print(0)

# print(sum)

#함수에 숫자 주고 출력하기

num = int(input())
def BBQ(x):
    for i in range(1,x+1):
        print(i, end ='')

def KFC(x):
    for i in range(7):
        print(x*7)

if num % 2 == 1:
    num2 = int(input())
    BBQ(num2)

elif num == 0 :
    print(0)

else:
    string = input()
    KFC(string)


