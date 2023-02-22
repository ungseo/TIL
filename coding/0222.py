# arr = [0] * 200
# def findboss(member):
#     if arr[ord(member)] == 0:
#         return member
#     else:
#         rst = findboss(arr[ord(member)])
#         return rst
#
# def setunion(a,b):
#     fa, fb = findboss(a), findboss(b)
#     if fa == fb:
#         return
#     else:
#         arr[ord(fb)] = fa
#
# setunion('a','b')
# setunion('d','e')
# setunion('b','e')
# setunion('b','d')
# setunion('e','f')
#
# y,x = input().split()
# if findboss(y) == findboss(x):
#     print('같은그룹')
# else:
#     print('다른그룹')
# def findboss(member):
#     if arr[ord(member)] == 0 :
#         return member
#     else:
#         ret = findboss(arr[ord(member)])
#         arr[ord(member)] = ret
#         return ret
#
# def setunion(a,b):
#     global flag
#     fa, fb = findboss(a), findboss(b)
#     if fa == fb:
#         print('cycle발견')
#         flag = 0
#         return
#     else:
#         arr[ord(fb)] = fa
#
#
# flag = 1
# arr = [0] * 200
# n = int(input()) # 간선의 개수
# for l in range(n):
#     a, b  = input().split()
#     setunion(a,b)
# if flag == 1:
#     print('cycle 미발견')
#


# Queue
from collections import deque
q=deque()
q.append(5)
q.append(6)
q.append(7)
q.append(8)
q.append(9)
print(q)
print([*q])
q.popleft()
q.popleft()
print(*q)



from collections import deque
# name=list(input().split())  # A B C D E F
# arr=[[0,1,1,0,0,0],
#      [0,0,0,1,1,0],
#      [0,0,0,0,0,1],
#      [0,0,0,0,0,0],
#      [0,0,0,0,0,0],
#      [0,0,0,0,0,0]]
# answer=[]  # 탐색순서 저장 후 출력
#
#
# def bfs(st):  # 0 (출발점)
#     global answer
#     q=deque()
#     q.append(st)
#     while q:
#         now=q.popleft()
#         answer.append(name[now])
#
#         for i in range(6):
#             if arr[now][i]==1:
#                 q.append(i)
#
# bfs(0)
# print(*answer)



name = ['A','B','C','E','F','G','H','Z']
#######[ 0   1   2   3   4   5   6   7
ans = []
arr = [[0,1,0,0,1,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,1,0,1],
       [1,0,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],#
       [0,0,0,0,0,0,1,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0]]#

def bfs(start): #e(3)
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        ans.append(name[now])
        for i in range(8):
            if arr[now][i] == 1:
                q.append(i)

bfs(3)

print(*ans)


print()


name = ['A','B','C','D']

arr = [[0,1,1,0],
       [0,0,1,1],
       [0,1,0,1],
       [0,0,0,0]]
answer = []
used = [0] * 4
def bfs(start):
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        answer.append(name[now])
        for i in range(4):
            if arr[now][i] == 0:continue
            if used[i] == 1: continue
            used[i] = 1
            q.append(i)
used[0] = 1
bfs(0)
print(*answer)


name=['A','B','C','D']
arr=[[0,1,1,0],
     [0,0,1,1],
     [0,1,0,1],
     [0,0,0,0]]
answer=[]  # 탐색순서 저장 후 출력
used=[0]*4

def bfs(st):
    q=deque()
    q.append(st)
    while q:
        now=q.popleft()
        answer.append(name[now])
        for i in range(4):
            if arr[now][i]==1:
                if used[i]==0:
                    used[i]=1
                    q.append(i)

used[0]=1
bfs(0)
print(*answer)


























