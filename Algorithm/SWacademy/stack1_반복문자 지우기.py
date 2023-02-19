'''난이도 D2'''

# 투포인터로 접근
# T = int(input())

# for tc in range(1,T+1):
#     st = list(input())
    
#     fix = 0
#     mov = 1
#     cnt = 0
#     while mov < len(st):
#         if st[fix] == st[mov]:   # 일치하고 
#             if fix >= 0 and mov > 1:          # 맨 처음 걸린게 아니면,
#                 fix -= 1         
#                 mov += 1        # 포인터 벌려주기
#                 cnt += 2  
#                 if fix == -1:
#                     fix = mov
#                     mov += 1      #  개수 +2 
#             elif st[fix] == st[mov] and fix == 0 and mov == 1:               # 일치하지만, 맨 처음에 걸린경우 (예외처리)
#                 st.pop(0)       
#                 st.pop(0)   ## 두 문자를 아예 날려버림
#                 fix = 0         # 포인터 처음으로 옮기고 검색 다시시작
#                 mov = 1
#         elif mov-fix != 1: # 일치하지 않고 포인터가 한번이상 벌려진경우
#             fix = mov      ## 전에는 일치, 이번엔 일치 x 경우임
#             mov += 1        # 벌려진 포인터 마지막검색 오른쪽으로 옮겨주기
        
#         else:               # 일치하지 않은경우
#             fix += 1        # 전에도 불일치, 이번에도 불일치인 경우
#             mov += 1    # 포인터 한칸씩 이동

#     print(f'#{tc} {len(st)-cnt}')

# 투포인터 꺼져
T = int(input())

for tc in range(1,T+1):
    st = list(input())
    
    rst = [0]
    
    for i in range(len(st)):
        if rst[-1] != st[i]:
            rst.append(st[i])
        else:
            rst.pop()
    
    print(f'#{tc} {len(rst)}')