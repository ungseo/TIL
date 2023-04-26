import sys

input = sys.stdin.readline

A, B = map(int, input().split())

num = [0, 0] + [1] * int(((B - A) ** 0.5) - 1)

for i in range(2, int(B ** 0.25) + 1):
    for j in range(2, int((B - A) ** 0.5) + 1):  # 구하는 수
        if num[j] == 0: continue
        if i == j: continue
        if j % i == 0:
            num[j] = 0

cnt = 0
prime_number = []
for i in range(2, int((B - A) ** 0.5) + 1):
    if num[i] == 1:
        prime_number.append(i)

print(prime_number)
n = 2
ans = []
for i in range(len(prime_number)):
    while 1:
        a = prime_number[i] ** n
        if a > B:
            n = 2
            break
        if a in ans: continue
        ans.append(a)
        n += 1
print(ans)
print(len(ans))
