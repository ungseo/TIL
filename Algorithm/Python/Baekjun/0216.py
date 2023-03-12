# N = int(input())
# A = list(map(int,input().split()))
# A.sort()
# k = -1
# cnt = 0

# # while k < N - 1:
# #     st = 0 
# #     ed = N - 1
# #     k += 1
# for k in range(N):
#     st = 0
#     ed = N - 1    
#     while st < ed:
#         if A[st] + A[ed] == A[k]:
#             if st != k and ed != k:
#                 cnt += 1
#                 break
#             elif st == k:
#                 st += 1
#             elif ed == k:
#                 ed -= 1
            
#         elif A[st] + A[ed] > A[k]:
#             ed -= 1
#         else:
#             st += 1
    
# print(cnt)


## 슬라이딩 윈도우
# lens, lenp = map(int,input().split())
# st = input()
# minDNA = list(map(int,input().split()))
# DNAlst = ['A','C','G','T']
# password = str()
# stat = [0,0,0,0]
# cnt = 0
# for i in range(lenp): ## 초기 p만큼 문자 설정
#     password += st[i]

# for i in range(4):  ##   초기 상태 설정
#     stat[i] += st.count(DNAlst[i])
# flag = 1    
# for i in range(4):
#     if stat[i] < minDNA[i]:
#         flag = 0
#         break
# if flag:
#     cnt += 1


# flag = 1
# for i in range(lens-lenp):  ## 한칸씩 옮기면서 상태 업데이트
#     password -= password[i]
#     if password[i] == 'A':
#         stat[0] -= 1
#     elif password[i] == 'C':
#         stat[1] -= 1
#     elif password[i] == 'G':
#         stat[2] -= 1
#     else:
#         stat[3] -= 1
    
#     password += password[i+lenp]
#     if password[i+lenp] == 'A':
#         stat[0] += 1
#     elif password[i+lenp] == 'C':
#         stat[1] += 1
#     elif password[i+lenp] == 'G':
#         stat[2] += 1
#     else:
#         stat[3] += 1
    
#     for i in range(4):
#         if stat[i] < minDNA[i]:
#             flag = 0
#             break
    
#     if flag:
#         cnt += 1
        
# print(cnt)

def check(a,b):
    cnt = 0
    for i in range(4):
        if a[i] >= b[i]:   ## b = min ACGT
            cnt += 1
    if cnt == 4:
        return 1
    return 0
    
    
ll, lp = map(int,input().split())
DNAst = input()
min_ACGT = list(map(int,input().split()))
ACGT_cnt = [0] * 4
result = 0

for i in range(lp):
    if DNAst[i] == 'A':
        ACGT_cnt[0] += 1
    elif DNAst[i] == 'C':
        ACGT_cnt[1] += 1
    elif DNAst[i] == 'G':
        ACGT_cnt[2] += 1
    else:
        ACGT_cnt[3] += 1
result += check(ACGT_cnt,min_ACGT)

for i in range(ll-lp):
    # 왼쪽 값 빼기
    if DNAst[i] == 'A':
        ACGT_cnt[0] -= 1
    elif DNAst[i] == 'C':
        ACGT_cnt[1] -= 1
    elif DNAst[i] == 'G':
        ACGT_cnt[2] -= 1
    else:
        ACGT_cnt[3] -= 1
    # 오른쪽값 더하기
    if DNAst[i+lp] == 'A':
        ACGT_cnt[0] += 1
    elif DNAst[i+lp] == 'C':
        ACGT_cnt[1] += 1
    elif DNAst[i+lp] == 'G':
        ACGT_cnt[2] += 1
    else:
        ACGT_cnt[3] += 1

    result += check(ACGT_cnt,min_ACGT)

print(result)
    