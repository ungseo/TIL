def bbsort(arr):
    for i in range(N-1):
        for j in range(N-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    guest = map(int,input().split())
    bbsort(guest)
    bbang = '0' * M + str(K)
    bbang *= 100
