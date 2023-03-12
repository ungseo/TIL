T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    small, middle, big = []
    for s in range(n - 2):
        small += carrot[:s]
        for m in range(s + 1, n - 1):
           