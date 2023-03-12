## 경로를 출력하자

# lst = ['A','B','C']
# path = [0] * 2
# def abc(level):
#     if level == 2:
#         print(''.join(path))
#         return
    
#     for i in lst:
#         path[level] = i
#         abc(level+1)
        
# abc(0)


## 같은 문장 찾기


# st1,st2,st3 = [input() for i in range(3)]
    
# if st1 == st2 and st2 == st3:
#     print('WOW')
# elif st1 == st2 or st2 == st3 or st1 == st3:
#     print('GOOD')
# else:
#     print('BAD')
    
    
## 경로이름은 BGTK

# lev = int(input())
# path = [0] * lev
# arr = ['B','G','T','K']

# def abc(level):
    
#     if level == lev:
#         print(''.join(path))
#         return
    
#     for i in range(len(arr)):
#         path[level] = arr[i]
#         abc(level+1)

# abc(0)

## Up & Down
# building = ['B5','B4','B3','B2','B1',1,2,3,4,5,6]
# character = 5
# for i in range(5):
#     cmd = input()
#     if cmd == 'up':
#         character += 1
#     else:
#         character -= 1
# print(building[character])

## 청소당번

# branch = int(input())
# path = [0] * 4
# people = [str(i) for i in range(1,branch+1)]
# def abc(level):
#     if level == 4:
#         print(''.join(path))
#         return
    
#     for i in range(branch):
#         path[level] = people[i] 
#         abc(level+1)
        
# abc(0)


## 가장 긴문장, 짧은 문장은 어디에

# string = [input() for i in range(4)]
# mini = 0
# maxi = 0
# maxL = 0
# minL = 21e8
# for i in range(len(string)):
#     if maxL < len(string[i]):
#         maxL = len(string[i])
#         maxi = i
    
#     if minL > len(string[i]):
#         minL = len(string[i])
#         mini = i

# print(f'긴문장:{maxi}\n짧은문장:{mini}')


## 몇번째 행운
# sc = input()
# arr = ['A','B','C','D']
# path = [0] *  3
# cnt = 0
# def abc(level):
#     global cnt
#     if level == 3:
#         cnt += 1
#         if ''.join(path) == sc:
#             print(f'{cnt}번째')
#         return
    
#     for i in range(4):
#         path[level] = arr[i]
#         abc(level+1)
        
# abc(0)

## 3차 배열에서 MAX MIN 찾기
# d3arr = [[[2,4],
#           [1,5]],
#          [[2,3],
#           [3,6]],
#          [[7,3],
#           [1,5]]]

# num = int(input())

# maxV=0
# minV=21e8
# for i in range(2):
#     for j in range(2):
#         if d3arr[num][i][j] > maxV:
#             maxV = d3arr[num][i][j]
#         if d3arr[num][i][j] < minV:
#             minV = d3arr[num][i][j]
            
# print(f'MAX={maxV}\nMIN={minV}')

# ## 암호 해독하기
# pword = ['Jason','Dr.tom','EXEXI','GK12P','POW']

# pw = input()

# if pw in pword:
#     print('암호해제')
# else:
#     print('암호틀림')

## 3차배열과 문자의 발견여부
# d3lst = [[['A','T','B'],['C','C','B']],[['A','A','A'],['B','B','C']]]

# st= input()

# bp1 = 1
# for z in range(2):
#     bp2 = 1
#     for i in range(2):
#         bp3 = 1
#         for j in range(3):
#             if d3lst[z][i][j] == st:
#                 bp3 = 0 
#                 break
#         if bp3 == 0:
#             bp2 = 0
#             break
#     if bp2 == 0:
#         bp1 = 0
#         break
# if bp1 == 0:
#     print('발견')
# else:
#     print('미발견')

## 바람둥이

# n = int(input())

# p = ['x','o']
# path = [0] * n
# def abc(level):
#     if level == n:
#         print(''.join(path))
#         return
    
#     for i in range(2):
#         path[level] = p[i]
#         abc(level+1)
        
# abc(0)

## 문자를 채우다

# lst = [[[0] * 3 for i in range(3)] for j in range(3)]
# st = input()
# stn = ord(st)-1

# for z in range(3):
#     stn += 1
    
#     for i in range(3):
#         for j in range(3):
#             if 65 <= stn <1= 90:
#                 lst[z][i][j] = chr(stn)
#                 print(lst[z][i][j], end='')
#             else:
#                 lst[z][i][j] = chr(stn-26)
#                 print(lst[z][i][j], end='')
#         print()
#     print()   

## 한놈a 한줄b

# arr = list(map(int,input().split()))

# lst = [[[0] * 3 for i in range(2)] for j in range(3)]

# for z in range(3):
#     for i in range(2):
#         for j in range(3):
#             lst[z][i][j] = arr[i]
#             print(lst[z][i][j], end=' ')
#         print()
#     print()

## Mapping

# st1, st2 = map(str,input().split())
# st2 = int(st2)

# MAP = [['A',3,5,4,2,2,3],['B',1,3,3,3,4,2],['C',5,4,4,2,3,5]]
# price = ['_','T','P','G','K','C']

# for i in range(3):
#     if MAP[i][0] == st1:
#         ni = i


# print(price[MAP[ni][st2]])

## 문장 정렬
dic = {}

for i in range(4):
    st = input()
    dic[len(st)] = st
print(dic)



