# n = int(input())
# arr = [list(m(int,input().split())) for _ in range(n)]


# def dfs(idx):
#     print(idx, end=' ')
#     for j in range(n):
#         if arr[idx][j] == 1:
#             dfs(j)
            
# dfs(0)

## 2층에서 경로 출력

# n = int(input())
# arr = [list(m(int,input().split())) for _ in range(n)]
# path = [0] * 3

# def dfs(level,idx):
#     if level == 2:
#         print(*path)
#         return
#     for j in range(n):
#         if arr[idx][j] == 1:
#             path[level+1] = j
#             dfs(level+1,j)
            
# dfs(0,0)

## 문자열 노드 DFS

# st = input()
# arr = [list(m(int,input().split())) for _ in range(8)]

# def dfs(level,idx):
#     print(st[idx],end='')
#     for i in range(8):
#         if arr[idx][i] == 1:
#             dfs(level+1,i)

# dfs(0,0)

## DFS 시작하기

# n = int(input())
# arr = [list(m(int,input().split())) for _ in range(n)]
# def dfs(idx):
#     print(idx, end=' ')
#     for i in range(n):
#         if arr[idx][i] == 1:
#             dfs(i)
#
# dfs(0)
#


# ## 최소이동 네비게이션
# arr = [[0,0,1,0,1,1],
#        [1,0,0,1,0,0],
#        [0,0,0,0,1,0],
#        [1,0,0,0,0,0],
#        [1,0,0,0,0,0],
#        [0,0,0,0,0,0]]
#
# A, B = m(int,input().split())
# used = [0]*6
# used[A-1] = 1
# minV = 21e8
# def dfs(st,step):
#     global minV
#     if st == B-1:
#         if minV > step:
#             minV = step
#         return
#
#     for i in range(6):
#         if arr[st][i] == 0: continue
#         if used[i] == 1: continue
#         used[i] = 1
#         dfs(i,step+1)
#         used[i] = 0
#
# dfs(A-1,0)
# if minV == 21e8:
#     print(0)
# else:
#     print(minV)

## 징검다리 돌아오기

# n = int(input())
#
# lst = [0,3,1,2,1,3,2,1,2,1]
#
# def jump(now):
#
#     if now >= len(lst):
#         print('도착', end=' ')
#         return
#     print(lst[now], end=' ')
#     jump(now+lst[now])
#     print(lst[now], end=' ')
# print('시작', end=' ')
# jump(n)
# print('시작')

## 범인의 흔적

# evid = [-1,0,0,1,2,4,4]
# timeStamp = [8,3,5,6,8,9,10]
# idx = int(input())
#
# def trace(idx):
#     if idx == 0:
#         print(f'{idx}번index(출발)')
#         return
#
#     trace(evid[idx])
#     print(f'{idx}번index({timeStamp[idx]}시)')
# trace(idx)

## 모두 같은 숫자일까?
#
# arr = [list(m(int,input().split())) for _ in range(3)]
# temp = [0] * 3
#
#
# for i in range(3):
#     cnt = 0
#     for j in range(2):
#         if arr[i][j] == arr[i][j+1]:
#             cnt += 1
#     if cnt == 2:
#         print(arr[i][j])
#     else:
#         print('x')

## 두 정렬되어있는 배열을 하나로





# lst1 = list(m(int,input().split()))
# lst2 = list(m(int,input().split()))
# rst = []
# a = b = 0
# while 1:
#     if lst1[a] > lst2[b]:
#         rst.append(lst2[b])
#         b += 1
#     elif lst1[a] <= lst2[b]:
#         rst.append(lst1[a])
#         a += 1
#
#     if a == 4:
#         rst += lst2[b:]
#         break
#     elif b == 4:
#         rst += lst1[a:]
#         break
#
# print(*rst)

## 블럭을 감싸는 사각프레임 좌표 구하기

# block = [list(m(int,input().split())) for i in range(4)]
# flag = 1
# for i in range(4):
#     for j in range(5):
#         if block[i][j] == 1:
#             print(f'({i},{j})')
#             flag = 0
#             break
#     if flag == 0: break
#
# for j in range(4,-1,-1):
#     for i in range(3,-1,-1):
#         if block[i][j] == 1:
#             print(f'({i},{j})')
#             flag = 1
#             break
#     if flag == 1: break

## 톱니바퀴

# def roll(x):
#     temp = []
#     result = [0,0,0]
#     for i in range(3):
#         temp.append(arr[i][x])
#     result[0] = temp[2]
#     result[1] = temp[0]
#     result[2] = temp[1]

#     for i in range(3):
#         arr[i][x] = result[i]

# arr = [[3,2,5,3],
#        [7,6,1,6],
#        [4,9,2,7]]
# lst = list(m(int,input().split()))

# for idx in range(4):
#     for r in range(lst[idx]):
#         roll(idx)


# for i in range(3):
#     for j in range(4):
#         print(arr[i][j], end='')
#     print()


# m = ['_'] * 5
# idx, life = map(int,input().split())

# def bug(i,life):
#     if i == 5:
#         return
#     if life == 0:
#         m[i] = '_'
#         print(''.join(m))
#         return

#     m[i] = str(life)
#     print(''.join(m))
#     m[i] = '_'
#     bug(i+1,life-1)
    

# bug(idx,life)

def monster_mov(sec,m,y,x):               ## 몬스터이동 (초, 몬스터 종류, y,x)
    movey = [0,1,0,-1]
    movex = [1,0,-1,0]
    idx = sec % 4         ## 시간초 % 4연산해서 방향 반복

    ny = y + movey[idx]
    nx = x + movex[idx]

    if 0 <= ny <= 3 and 0 <= nx <= 2:
        if map[ny][nx] == '_':
            map[ny][nx] = map[y][x]
            map[y][x] = '_'
            msidx[m] = (ny,nx)      ## 옮기고 몬스터 A,C,D 좌표 재설정

monster = ['A','C','D']
msidx = [0,0,0]
map = [list(input()) for _ in range(4)]

for m in range(3):
    for i in range(4):
        for j in range(3):
            if map[i][j] == monster[m]:
                msidx[m] = (i,j)

for i in range(5):
    for j in range(3):
        monster_mov(i,j, *msidx[j])

for i in range(4):
    for j in range(3):
        print(map[i][j], end='')
    print()