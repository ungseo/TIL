'''
3
5
3 1 2 3 4
6
1 4 2 33 2 1
7
3 4 5 3 1 11 6
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    maxV = arr[0]    # 첫 원소를 최대로
    for i in range(1,N): ## 나머지 원소와 비교
        if maxV < arr[i]:
            maxV = arr[i]
    print(f'#{tc} {maxV}')