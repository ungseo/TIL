import sys
input = sys.stdin.readline
n = int(input())
DAT = [0] * 10001
for i in range(n):
    DAT[int(input())] += 1
p = 1
cnt = 0
while cnt != n:
    if DAT[p] >= 1:
        cnt += DAT[p]
        sys.stdout.write((str(p) + '\n') * DAT[p])
        p += 1
    else:
        p += 1


