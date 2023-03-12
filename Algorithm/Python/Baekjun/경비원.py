def batch(dir,dis,num):               ## 사각형 각 변에 가게 위치 입력하기
    if dir == 1:
        north[dis-1] = num
    elif dir == 2:
        south[dis] = num
    elif dir == 3:
        west[dis] = num
    else:
        east[dis-1] = num

garo, sero = map(int,input().split())  ## 가로,세로

north = [0] * garo   # 윗줄
south = [0] * garo  # 아랫줄
west = [0] * sero   # 왼쪽줄
east = [0] * sero   # 오른쪽줄

n = int(input())         
for i in range(1,n+2):
    direction, distance = map(int,input().split())  
    batch(direction, distance, i)   # 가게 배치, i는 1~4 (방향)

line = north + east + south[::-1] + west[::-1]  # 사각형 모든 변 한줄로 이어붙이기

for i in range(len(line)):  # n+1 탐색 (경비업체 위치)
    if line[i] == n+1:
        st_idx = i 
        break
rst = 0
for i in range(1,n+1):    # 한칸씩 이동하면서 찾고있는 가게번호(1~n)까지 찾기
    pointer = st_idx     
    cnt = 0
    while 1:
        if pointer == len(line)-1:  # 포인터 한칸씩 이동 // 끝에 도달하면 포인터 맨앞으로 초기화
            pointer = 0
            cnt += 1                # 한칸마다 거리 1씩 더해주기
        if line[pointer] == i:     # 찾으면 멈추고 거리 계산
            break
        else:
            pointer += 1
            cnt += 1

    if cnt > garo + sero:          # 만약 거리가 사각형 둘레의 절반보다 크면 
        rst += (garo+sero)*2 - cnt # 사각형둘레에서 뺀값 이 최솟값이기 때문에 출력
    else:
        rst += cnt   # 절반보다 작으면 그게 최솟값이기 떄문에 출력 

print(rst)