import sys

input = sys.stdin.readline

m, n = map(int, input().split())
nlst = list(range(m, n + 1))

for j in range(2, int(n ** (1 / 2))):
    for i in range(len(nlst)):
        if j == nlst[i]: continue

        if nlst[i] % j == 0:
            nlst[i] = 0

for i in nlst:
    if i == 0: continue
    print(i)
