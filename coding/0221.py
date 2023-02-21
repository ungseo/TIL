# # 전위 순회
# arr = ' abcdefg'
#
#
# def preorder(now):
#     if now> len(arr)-1:return
#     print(arr[now],end = ' ')
#     preorder(now*2)
#     preorder(now*2+1)
#
# def postorder(now):
#     if now> len(arr)-1:return
#     postorder(now*2)
#     postorder(now*2+1)
#     print(arr[now], end=' ')
#
# def inorder(now):
#     if now> len(arr)-1:return
#     inorder(now*2)
#     print(arr[now], end=' ')
#     inorder(now*2+1)
#
# preorder(1)
# print()
# postorder(1)
# print()
# inorder(1)
# print()
#
#
# lst = [4,7,1,9,3,1,6]
#
# arr = [0] * 20
#
# def insert(target):
#     now = 1
#     while 1:
#         if arr[now] == 0:
#             arr[now] =target
#             return
#         if arr[now]<target: now= now*2 +1
#         else: now = now*2
#
# def search(target):
#     now = 1
#     while 1:
#         if now >= 20: return 0
#         if arr[now] == 0 : return 0
#         if arr[now] == target: return 1
#         if arr[now] < target: now = now* 2+1
#         else : now= now* 2
#
# for i in range(len(lst)):
#     insert(lst[i])
#
# n = int(input())
# ret = search(n)
# if ret == 1:
#     print('존재함')
# else:
#     print('없는숫자')
#
#
# for i in range(len(lst)): #dd
#     insert(lst[i])
'''
검색을 빠르게 하는 대표적인 알고리즘으로 BST와 HASH가 있습니다.
BST는 logN의 속도로 검색을 가능하게 하지만, 입력되는 데이터가 좋지 않을 시
최악의 경우 O(n)의 속도가 날 수도 있습니다.
이때 발란스드 트리로 만들어주는 알고리즘을 적용하여 로그 엔의 속도로 탐색이
가능하게끔 하는 과정이 필요합니다. (red/black Tree)
'''

arr =[3,7,1,4,7,31,8]
heap=[0] * 30
hindex = 1

def insert(value):
    global hindex
    heap[hindex] = value
    now = hindex
    hindex += 1
    while 1:
        p = now//2   # 부모 인덱스 구하기
        if p==0 : break  # 만약에 부모인덱스가 0이라면 (now는 루트노드) 비교할 것 없음, 꺼버림
        if heap[p] >= heap[now] : break  # 부모와 now값 비교해서 부모가 크거나 같으면 꺼버림
        heap[p],heap[now] = heap[now],heap[p] # 부모값 <now 값 이라면 swqp
        now = p  # 부모가 그다음의 now가 됨 (부모가 부모의 부모와 비교를 실행)
def top():
    return heap[1]
def pop():
    global hindex
    heap[1] = heap[hindex-1] #맨 뒤에 아이를 루트로 올리고
    heap[hindex] = 0  # 맨 뒤에 값을 0으로 바꾸고
    hindex -= 1
    now = 1
    while 1:
        son = now*2
        rson = now*2 +1
        # 오른쪽 자식이 있고! 오른쪽자식이 왼쪽 자식보다 크면 (오른쪽자식과 now랑 비교하겠다)
        if son <= hindex and heap[son] < heap[rson]: son = rson
        # 자식이 없거나 부모가 자식이 더 크다면 break
        if son > hindex or heap[now] < heap[son]: break
        heap[now],heap[son] = heap[son], heap[now]
        now = son



for i in range(len(arr)):
    insert(arr[i])
for i in range(len(arr)):
    print(top(),end=' ')
    pop()


