# ## 13566. 숫자 카드

# T = int(input())

# for tc in range(1,T+1):
#     N = int(input())
#     card = list(map(int,map(str,input())))

#     DAT = [0 for i in range(10)]

#     for i in range(N):
#         DAT[card[i]] += 1
    
#     mastartpointV = 0
#     for i in range(10):
#         if mastartpointV < DAT[i]:
#             mastartpointV = DAT[i]
    
    
#     for i in range(9,-1,-1):
        
#         if DAT[i] == mastartpointV:
#             print(f'#{tc} {i} {DAT[i]}')
#             break


## 전기버스


# def busMove(startpoint):        ## 한칸씩 움직이는 함수 작성
#         me
#         me += 1

# def checkStation(startpoint):   ## 충전해야하는 조건 함수로 작성
#         for i in range(startpoint+K,startpoint,-1):  ## 시작위치 + 최대이동거리~ 시작위치 전까지(역순)탐색
#             if station[i] == 1:   ##뒤로 탐색하면서 최대로 갈 수있는 역 위치 찾기
#                 return i   ##역 위치 반환
#         else:
#             return 0   ## 못가면 0 반환

# T = int(input())

# for tc in range(1,T+1):                   
#     K, N, M = list(map(int,input().split()))  ## 입력받기
#     lst = list(map(int,input().split()))   
#     me = 0                                      ##시작지점 = me
#     station = [0 for i in range(N+1)]           ## 역의 위치 DAT이용해서 리스트화
#     charge_cnt = 0      

#     for i in lst:                       ## 역의 위치 DAT이용해서 리스트화
#         station[i] += 1

#     while me != N:      ## me가 최대(N)도달하면 종료
#         if me + K >= N:     ## (N에 다왔으면)
#             me = N
#             print(f'#{tc} {charge_cnt}') ## 충전횟수 출력후 종료.
#             break
#         else:    ## 아직 더 가야하면
#             if station[me+K] == 1:   ## 최대이동(K)거리에 역이 있으면 
#                 for i in range(K):    
#                     busMove(me)      ## 최대이동거리만큼 이동후 충전횟수 +1
#                 charge_cnt += 1
#             else:                     ## 최대 이동거리(K)에 역이 없으면
#                 st = checkStation(me)   ## 최대 거리부터 뒤로 탐색하면서 가능한 가장 먼 역 탐색
#                 if st == 0:              ## 만약 못가면 
#                     charge_cnt = 0
#                     print(f'#{tc} {charge_cnt}')   ## 0 출력하고 종료
#                     break
#                 else:
#                     for i in range(st-me):   ## 갈수 있으면 충전소까지 가고 충전횟수 +1
#                         busMove(me)
#                     charge_cnt += 1
            

     
# T = int(input())

# for tc in range(1,T+1):

#     N = int(input())

#     lst = list(map(int,input().split()))

#     ans = []
#     for i in range(N-1):
#         std = lst[i]
#         cnt = 0
#         for j in range(i,N):
#             if std > lst[j]:
#                 cnt += 1
#         ans.append(cnt)

#     maxV = ans[0]
#     for i in ans:
#         if maxV < i:
#             maxV = i

#     print(f'#{tc} {maxV}')

N = int(input())
lst = [] 
for i in range(N):
    n = int(input())
    lst.append(n)

lst.sort()
for i in lst:
    print(i)
