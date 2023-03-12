
# def findboss(member):
#     if arr[ord(member)] == 0:
#         return member
#     else:
#         rst = findboss(arr[ord(member)])
#         return rst
#
# def union(a,b):
#     fa, fb = findboss(a), findboss(b)
#     if fa == fb:
#         return 0
#     else:
#         arr[ord(fb)] = fa
#         return 1
#
# arr = [0] * 200
# cnt = 6
# m = int(input())
# for i in range(m):
#     a, b = input().split()
#     cnt -= union(a,b)
#
#
# print(cnt)



'''
4	# 정점의 개수
5	# 간선의 개수
B C 2
B D 9
A B 4
A D 1
C D 9
'''

def fboss(member):
    if arr[ord(member)] == 0:
        return member
    else:
        rst = fboss(arr[ord(member)])
        return rst
def union(a,b):
    fa, fb = fboss(a),fboss(b)
    if fa == fb:
        return 0
    else:
        arr[ord(fb)] = fa
        return 1




# arr = [0] * 200
# P = int(input())
# L = int(input())
# sort_lst = []
#
# for i in range(L):
#     a, b, cost = input().split()
#     cost = int(cost)
#     sort_lst.append([a,b,cost])
#
#
# a = sorted(sort_lst,key= lambda x:x[2])
# island = 0
# sum = 0
# for i in range(len(a)):
#     if union(a[i][0],a[i][1]):
#         island += 1
#         sum += a[i][2]
#     if island == P - 1:
#         print(sum)
#         break

arr=[0]*200
k=int(input())  # 정점의 개수
n=int(input())  # 간선의 정보 개수
lst=[list(input().split()) for _ in range(n)] # 간선의 정보 입력

# 설계
# 비용을 기준으로 sort

# unionfind 하는데 보스가 같으면 안하고
#                   보스가 다르면 합체 / cnt+=1 / total 비용 더하기
#cnt가 k-1개 되면 끝

lst.sort(key=lambda x:int(x[2]))

def findboss(m):
    if not arr[ord(m)]:
        return m
    ret=findboss(arr[ord(m)])
    arr[ord(m)]=ret
    return ret

def union(a,b,i):
    global total,cnt
    aboss,bboss=findboss(a),findboss(b)
    if aboss == bboss:
        return
    total += int(lst[i][2])             # 다리건설 할때 드는 비용 더하기
    cnt+=1                              # 다리 개수 1 증가
    arr[ord(bboss)]=aboss               # 다리 건설하기!

total=0   # 최소비용
cnt=0    # 다리 개수
for i in range(n):
    if cnt==k-1:            # 다리개수가 정점개수 -1 개와 같으면 출력하고 끝내기
        print(total)
        break
    union(lst[i][0],lst[i][1],i)
