'''
55 7 78 12 42
for i : 0 N -1 -> 1  ## 각 구간의 끝
    for j : 0 -> i-1  ## 비교 할 왼쪽 원소
        if arr[j] > arr[j+1]
            arr[j] <-> arr[j+1]  ## 자리바꾸기
'''
arr = list(map(int, input().split()))

N = len(arr)
for i in range(N-1, 0, -1): ## 각 구간의 끝
    for j in range(i):  ## 비교 할 왼쪽 원소
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]## 자리바꾸기

print(*arr)

