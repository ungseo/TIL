def abs(a,b):     ## 높이 차 절댓값 구하기 함수
    if a > b:
        rst = a - b
    else:
        rst = b - a

    return rst
def sinkhole(y,x):       ## 8 방향 검색 해서 최대높이 출력하는 함수
    cnt = 0
    movey = [-1,-1,0,1,1,1,0,-1]
    movex = [0,1,1,1,0,-1,-1,-1]   ## 방향배열 설정
    maxH = 0
    for i in range(8):              # 8방향 탐색
        ny = y + movey[i]
        nx = x + movex[i]
        if Map[y][x] < Map[ny][nx]:        # 만약 주변지대가 높으면
            cnt += 1                        # cnt 1증가
            H = abs(Map[y][x], Map[ny][nx])  # 높이의 차 H에 저장
            if maxH < H:       ## 제일 높은 값 저장
                maxH = H
    if cnt == 8:      ## 주변 8군데가 모두 높으면
        return maxH   ## 높은 지대 값 출력
    else:           # 아니면 0 리턴
        return 0

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    Map = [list(map(int,input().split())) for _ in range(n)]
    rst = 0
    mH = 0                      ## 싱크홀중 주변지대 가장 높은 값 구하기
    for i in range(1,n-1):
        for j in range(1,n-1):
            if mH < sinkhole(i,j):
                rst += 1            # 싱크홀 갯수 카운트
                mH = sinkhole(i,j)  # 최대 높이값 저장

    print(f'#{tc} {rst} {mH}')  #출력