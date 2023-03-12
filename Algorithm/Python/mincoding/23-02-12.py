# lst = [input() for i in range(4)]
# temp = []
# for i in range(3):
#     for j in range(3-i):
#         if len(lst[j]) > len(lst[j+1]):
#             lst[j],lst[j+1] = lst[j+1],lst[j]

# for i in range(4):
#     print(lst[i])

## 이니셜 뽑기

# lst = [[[' ','#',' '],['#',' ','#'],['#','#','#'],['#',' ','#'],['#',' ','#']],[['#','#','#'],['#',' ','#'],['#','#','#'],['#',' ','#'],['#','#','#']],[['#','#','#'],['#',' ','#'],['#',' ',' '],['#',' ','#'],['#','#','#']],[['#','#',' '],['#',' ','#'],['#',' ','#'],['#',' ','#'],['#','#',' ']]]

# num = int(input())

# for i in range(5):
#     for j in range(3):
#         print(lst[num][i][j], end='')
#     print()

## 스도쿠 검증
# def csort(point, direction):
#     DAT = [0] * 9
#     temp = [0] * 9
#     if direction == 0:
#         data = sdoku[point]
    
#     else:
#         data = []
#         for i in range(9):
#             data.append(sdoku[i][point])
    
#     for i in data:
#         DAT[i-1] += 1
#     for i in range(1,9):
#         DAT[i] += DAT[i-1]
#     for i in data[::-1]:
#         temp[DAT[i-1]-1] = i
#         DAT[i-1] -= 1
#     if temp == [1,2,3,4,5,6,7,8,9]:
#         return 0
#     else:
#         return 1
# def sort33(y,x):
#     data = []
#     DAT = [0] * 9
#     temp = [0] * 9
#     for i in range(3):
#         for j in range(3):
#             data.append(sdoku[y+i][x+j])
#     for i in data:
#         DAT[i-1] += 1
#     for i in range(1,9):
#         DAT[i] += DAT[i-1]
#     for i in data[::-1]:
#         temp[DAT[i-1]-1] = i
#         DAT[i-1] -= 1
#     if temp == [1,2,3,4,5,6,7,8,9]:
#         return 0
#     else:
#         return 1




# T = int(input())

# for tc in range(1,1+T):
#     sdoku = [list(map(int,input().split())) for i in range(9)]
#     cnt = 0
#     for i in range(9):
#         cnt += csort(i, 0)
#         cnt += csort(i, 1)
#     for i in [0,3,6]:
#         for j in [0,3,6]:
#             cnt += sort33(i,j)
    
#     if cnt > 1:
#         print(f'#{tc} 0')
#     else:
#         print(f'#{tc} 1')


## 배열 회전하기

# def turn90(arr):
#     ans = []
#     for j in range(N):
#         temp = []
#         for i in range(N-1,-1,-1):
#             temp.append(arr[i][j])
#         ans.append(temp)
#     return ans




# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     lst = [list(map(int,input().split())) for i in range(N)]
#     t90 = turn90(lst)
#     t180 = turn90(t90)
#     t270 = turn90(t180)
#     rst = t90 + t180 + t270
    

#     print(f'#{tc}')
#     for i in range(N):
#         for j in range(i,N*3,N):
#             print(''.join(map(str,rst[j])), end=' ')
#         print()
## 회문

# import sys
# sys.stdin = open('input.txt','r')
#
# for i in range(10):
#     tc = int(input())
#     lst = [list(input()) for _ in range(100)]
#
#     maxL = 1             # 회문 없을시 1 출력
#     for i in range(100):
#         for st in range(100):
#             for ed in range(99,st,-1):       # st는 0~99까지 ed는 99~st 까지
#                 if lst[i][st] == lst[i][ed]:  # st와 ed가 같은문자이면 실행
#                     temp = lst[i][st:ed+1]    #리스트에 문자 담고 역슬라이싱해서 회문 판독
#                     if temp == temp[::-1]:
#                         if maxL < len(temp):  # 회문이면 길이 최댓값 구하기
#                             maxL = len(temp)
#     for i in range(100):                     ## 리스트 뒤집기?? (세로줄 구하려고)
#         for j in range(100):
#             if i < j:
#                 lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
#
#     for i in range(100):              # 같은작업 반복
#         for st in range(100):
#             for ed in range(99, st, -1):
#                 if lst[i][st] == lst[i][ed]:
#                     temp = lst[i][st:ed+1]
#                     if temp == temp[::-1]:
#                         if maxL < len(temp):
#                             maxL = len(temp)
#
#
#     print(f'#{tc} {maxL}')  ## 맥스값 출력
#
# ##

# ..#...#...#...#...#..  ..# 후 ...# * len(st
# .#.#.#.#.#.#.#.#.#.#.
# #.A.#.P.#.P.#.L.#.E.#
# .#.#.#.#.#.#.#.#.#.#.
# ..#...#...#...#...#..

# def bids(level,st):
#     if level == 2:
#         for i in st:
#             print(f'#.{i}.', end='')
#         print('#')
#         return
#     if level == 0:
#         print('..#.'* len(st),end ='.')
#         print()
#     if level == 1:
#         print('.#.#' * len(st),end='.')
#         print()
#
#     bids(level+1,st)
#
#     if level == 0:
#         print('..#.'* len(st),end ='.')
#         print()
#     if level == 1:
#         print('.#.#' * len(st),end='.')
#         print()
#
#
#
#
# T = int(input())
# for tc in range(T):
#     st = input()
#     bids(0,st)


## Ladder 2
# import sys
# sys.stdin = open('input.txt','r')
# def down(x):  ## 내려가는 함수 좌우 탐색후 있으면 좌/우함수로 진입
#     global cnt
#     y = 0
#     while y < 99:
#         if ladder[y][x - 1] == 0 and ladder[y][x + 1] == 0:
#             y += 1
#             cnt += 1
#         elif ladder[y][x - 1] == 1:
#             y, x = left(y, x)
#
#             continue
#         elif ladder[y][x + 1] == 1:
#             y, x = right(y, x)
#
#             continue
#     return cnt
#
#
# def left(y, x):  # 좌로 진입
#     global cnt
#     while 1:
#         if ladder[y][x - 1] == 0:  # 가다가 벽 만나면 한칸 내려가고 종료
#             y += 1
#             cnt += 1
#             return [y, x]
#         else:
#             x -= 1
#             cnt += 1
#
#
# def right(y, x):  # 우로 진입
#     global cnt
#     while 1:
#         if ladder[y][x + 1] == 0:
#             y += 1
#             cnt += 1
#             return [y, x]
#         else:
#             x += 1
#             cnt += 1
#
#
# minX = 0
# for _ in range(1, 11):
#     tc = int(input())
#     ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]  # 맨 끝에 벽생성
#     minS = 21e8
#     for i in range(1, 100 + 1):
#         cnt = 0
#         if ladder[0][i] == 1:
#             step = down(i)
#             if minS > step:
#                 minS = step
#                 minX = i
#     print(f'#{tc} {minX - 1}')  # -1 해서 벽값 빼주기

## 파리잡기
# def swing(y,x):
#     kill = 0
#     for i in range(M):
#         for j in range(M):
#             kill += lst[y+i][x+j]
#     return kill
#
# T = int(input())
# for tc in range(1,T+1):
#     N, M = map(int,input().split())
#     lst = [list(map(int,input().split())) for _ in range(N)]
#
#     maxKill = 0
#     for i in range(N - M + 1):
#         for j in range(N - M + 1):
#             kill = swing(i,j)
#             if maxKill < kill:
#                 maxKill = kill
#
#     print(f'#{tc} {maxKill}')

## 파리잡기3
def cross(y,x):   ## 십자모양 분사
    sum = 0
    movey = [-1, 0, 1, 0]
    movex = [0, 1, 0, -1]
    for i in range(4):
        for j in range(1, M):
            ny = y + movey[i] * j
            nx = x + movex[i] * j
            if 0 <= ny < N and 0 <= nx < N:
                sum += lst[ny][nx]
    sum += lst[y][x]

    return sum

def X(y,x):   ## x자모양 분사
    sum = 0
    movey = [-1, -1, 1, 1]
    movex = [-1, 1, 1, -1]
    for i in range(4):
        for j in range(1, M):
            ny = y + movey[i] * j
            nx = x + movex[i] * j
            if 0 <= ny < N and 0 <= nx < N:
                sum += lst[ny][nx]
    sum += lst[y][x]
    return sum

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]
    maxkill = 0

    for i in range(N):
        for j in range(N):
            p = cross(i,j)
            x = X(i,j)
            if p > maxkill:
                maxkill = p
            if x > maxkill:
                maxkill = x
    print(f'#{tc} {maxkill}')