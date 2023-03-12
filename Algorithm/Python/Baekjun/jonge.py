arr = [[0]*100 for _ in range(100)] # 100 X 100의 도화지
N = int(input())

for _ in range(N): # N개의 좌표
    y, x = map(int, input().split()) # 좌표 입력받으면
    for i in range(y, y+10):         # 해당 좌표부터 10 X 10 부분에 
        for j in range(x, x+10):     
            arr[i][j] = 1            # 1 넣기

cnt = 0
for i in range(100):                 
    for j in range(100):
        if arr[i][j] == 1:           # 전체 도화지에서 1인 부분의
            cnt += 1                 # 개수 세면 그게 넓이

print(cnt)