import sys
input = sys.stdin.readline

n = int(input())
DAT = [0] * 1000001 # 0번 인덱스 제외하고 입력값(인덱스)에 1씩추가
for i in range(n):
    DAT[int(input())] += 1

p = 1
cnt = 0
while p <= 1000000: #pointer가 배열 끝을 넘으면 반복문 종료
    if DAT[p] == 0: # 값없을시 포인터 이동
        p += 1
    else:   # 있을 시 1감소시키고 출력
        DAT[p] -= 1
        cnt += 1
        print(p)
    if cnt == n:
        break