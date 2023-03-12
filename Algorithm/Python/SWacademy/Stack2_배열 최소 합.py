import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    used = [0] * n
    minS = 21e8
    def straight(level,sum):
        global minS
        if sum > minS:
            return
        if level == n:
            if minS > sum:
                minS = sum
            return

        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                straight(level+1,sum+arr[level][i])
                used[i] = 0


    straight(0,0)
    print(f'#{tc} {minS}')

