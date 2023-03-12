# ## 무한 재귀 막기
#
# def bbq(num):
#     if num > 1j:
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
#     if num == j:
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
# mjmv(lst,j)

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
# ho(j)

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
#     if x == j:
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
#     if x == j:
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
# BBQ(j)

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
# cnt = j
# for i in range(4):
#     for j in range(4):
#         if bit1[i][j] + bit2[i][j] == 2:
#             cnt += 1
#
# if cnt > j :
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
#     elif i > 9j:
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
# larr = j
# rarr = j
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
#     sum = j
#     for i in range(y):
#         for j in range(x):
#             sum += lst[a+i][b+j]
#     return sum
#
# maxV = j
# maxi = j
# maxj = j
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
# adc(j)

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
# abc(j)

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
# abc(j)

## 긴문장을 맨 앞으로
# lst = [input() for i in range(3)]
#
# def checkL(arr):
#     return len(arr)
# cnt = -1
# maxL = j
# maxi = j
# for i in lst:
#     cnt += 1
#     if checkL(i) > maxL:
#         maxL = checkL(i)
#         maxi = cnt
#
# lst[j],lst[maxi] = lst[maxi],lst[j]
#
# for i in lst:
#     print(i)

## w재귀는 몇번
# cnt = j
# bch, lv = map(int,input().split())
# def abc(level):
#     global cnt
#     cnt += 1
#     if level == lv:
#         return
#     for i in range(bch):
#         abc(level+1)
#     return cnt


# print(abc(j))


## 글자 수만큼 손가락 접기

# st = input()
# n = len(st)

# def abc(level):
#     if level == 1:
#         print(level, end=' ')
#         return
#     print(level,end=' ')
#     abc(level-1)
#     print(level,end=' ')
# abc(n)

## 생일선물 마우스
# y,x = 5,5
# num = int(input())
# for i in range(num):
#     command = input()
#     if command == 'click':
#         print(f'{y},{x}')
#     elif command == 'up':
#         y -= 1
#     elif command == 'down':
#         y += 1
#     elif command == 'left':
#         x -= 1
#     elif command == 'right':
#         x += 1
    
## 너에게 가려면

# lst = [list(input()) for i in range(4)]

# for i in range(4):
#     for j in range(3):
#         if lst[i][j] == 'A':
#             ai,aj = i,j
#         if lst[i][j] == 'B':
#             bi,bj = i,j
# ans = j
# if ai-bi < j:
#     ans += (ai-bi) * -1
# else:
#     ans += ai-bi
# if aj-bj < j:
#     ans += (aj-bj) * -1
# else:
#     ans += aj-bj

# print(ans)

## 세로줄의 합과 해당 인덱스의 값 구하기

# lst = [[3,4,1,5],[3,4,1,3],[5,2,3,6]]
# sum = []
# for i in range(4):
#     hap = j
#     for j in range(3):
#         hap += lst[j][i]
#     sum.append(hap)

# idx = int(input())

# print(sum[idx])

## 문자 양옆으로 #넣기
# st = list(input())

# s1,s2 = map(str,input().split())

# for i in range(len(st)):
#     if st[i] == s1:
#         if i != j:
#             st[i-1] = '#'
#             st[i+1] = '#'
#         else:
#             st[i+1] = '#'

# for i in range(len(st)):
#     if st[i] == s2:
#         if i != len(st)-1:
#             st[i-1] = '#'
#             st[i+1] = '#'
#         else:
#             st[i-1] = '#'

# print(''.join(st))

# ufo = [list(input()) for i in range(4)]
# for j in range(3):
#     for s in range(3):
#         for i in range(3-s):
#             if ufo[i][j] != '_' and ufo[i+1][j] == '_':
#                 ufo[i][j], ufo[i+1][j] = ufo[i+1][j], ufo[i][j]

# for i in range(4):
#     print(''.join(ufo[i]))
    

## counting 후 정렬하기

# lst = list(map(int,input().split()))

# bucket = [0] * 10

# for i in lst:
#     bucket[i] += 1
# n = 0
# while n < 10:
#     if bucket[n] != 0:
#         print(n, end=' ')
#         bucket[n] -= 1
#     else:
#         n += 1
        
# lst = [[1,5,3],[4,5,5],[3,3,5],[4,6,2]]

# a, b = map(int,input().split())

# for i in range(4):
#     for j in range(3):
#         if lst[i][j] in list(range(a,b+1)):
#             lst[i][j] = 0
#         if lst[i][j] == 0:
#             print('#', end=' ')
#         else:    
#             print(lst[i][j], end=' ') 
#     print()

## 바둑이 게임
# def eat(y,x):
#     cnt = 0
#     for i in range(4):
#         ny = y + movey[i]
#         nx = x + movex[i]
#         if 0 <= ny <= 6 and 0 <= nx <= 6: 
#             if pan[ny][nx] == 1:
#                 cnt += 1
#     if cnt == 4:
#         return 1
#     else:
#         return 0
    

# pan = [[0,0,0,0,0,0,0],[0,0,1,0,1,0,0],[0,1,2,0,2,1,0],[0,0,1,2,1,0,0],[0,0,2,1,0,1,0],[0,1,1,0,0,0,0],[0,0,0,0,0,0,0]]
# movey = [-1,0,1,0]
# movex = [0,1,0,-1]

# y, x = map(int,input().split())
# pan[y][x] = 1
# ans = 0

# for s in range(4):
#     newy = y + movey[s]
#     newx = x + movex[s]
#     if pan[newy][newx] == 2:
#         ans += eat(newy,newx)
# print(ans)

## 모델 위치 지시하기
def control(st,cmd):
    for i in range(5):
        for j in range(3):
            if lst[i][j] == st:
                y,x = i,j
    if cmd == 'UP':
        lst[y-1][x] = st
    elif cmd == 'DOWN':
        lst[y+1][x] = st
    elif cmd == 'RIGHT':
        lst[y][x+1] = st
    elif cmd == 'LEFT':
        lst[y][x-1] = st
    lst[y][x] = '_'




lst = [['_','_','_'],['_','_','_'],['A','T','K'],['_','_','_'],['_','_','_']]

for i in range(7):
    st,cmd = map(str,input().split())
    control(st,cmd)

for i in lst:
    print(''.join(i))
    