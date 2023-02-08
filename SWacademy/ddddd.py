

# T = int(input())
# for tc in range(1,T+1):
#     N, K = map(int,input().split())
#     puzzle = [list(map(int,input().split())) for i in range(N)]

    
#     ans = 0 
#     for i in range(N):
#         cnt = 0
#         for j in range(N):
#             if puzzle[i][j] == 1:
#                 cnt += 1
#                 if cnt == K:
#                     if j+1 >= N or puzzle[i][j+1] == 0:
#                         ans += 1
                        
#                     else:
#                         continue
#             else:
#                 cnt = 0
                            
#     for i in range(N):
#         cnt = 0
#         for j in range(N):
#             if puzzle[j][i] == 1:
#                 cnt += 1
#                 if cnt == K:
#                     if j+1 >= N or puzzle[j+1][i] == 0:
#                         ans += 1
                        
#                     else:
#                         continue
#             else:
#                 cnt = 0           
#     print(f'#{tc} {ans}')
                    
# import sys
# sys.stdin = open('input.txt','r')

# def checkNgo(y,x): #2로 마스킹하면서 이동하는 함수
#     global sty,stx
#     if x+1 != 100 and ladder[y][x+1] == 1:  ## 먼저 오른쪽 탐색
#         ladder[y][x+1] += 1                 ## 길이 있으면 
#         stx += 1                            ## 좌표 오른쪽으로 한칸 가고 값에 1추가 (2로 마스킹하기)
#     elif x-1 != -1 and ladder[y][x-1] == 1: ## 길 있으면 왼쪽탐색
#         ladder[y][x-1] += 1                 
#         stx -= 1                            ## 있으면 좌표 왼쪽으로 한칸 가고 값에 1추가 (2로 마스킹하기)
#     elif ladder[y-1][x] == 1:               ## 양쪽 없으면 위쪽탐색
#         ladder[y-1][x] += 1                 
#         sty -= 1                            ## 있으면 위로 1칸 가고 값에 1추가 (2로 마스킹하기)
        
# for i in range(1,11):
#     tc = int(input())
#     ladder = [list(map(int,input().split())) for i in range(100)] #사다리 생성
#     for i in range(100):
#         if ladder[99][i] == 2:  ## 출발지점 좌표 찾기
#             sty, stx = 99,i  ## 좌표 저장
#             break
#     while sty != 0:          ## y값이 0이 아닐때까지 (밑에서 위로 가기때문에)
#         checkNgo(sty,stx)   ## 마스킹하면서 이동
    
#     print(f'#{tc} {stx}')  ## y가 0에 도착하면 x값 출력
        
        

T = int(input())

for tc in range(1,1+T):
    dic = {}
    
    str1 = list(set(input()))  # 세트로 받아서 중복 문자 제거
    str2 = list(input())
    for i in str1:          
        cnt = 0
        for j in str2:    
            if i == j:
                cnt += 1
        dic[i] = cnt        ## 카운트해서 딕셔너리 추가
    
    ans = list(dic.values())     
    
    for i in range(len(ans)-1):       # ans 버블정렬
        for j in range(len(ans)-1):
            if ans[j] > ans[j+1]:
                ans[j],ans[j+1] = ans[j+1],ans[j]
                
    print(f'#{tc} {ans[-1]}')
                        
    