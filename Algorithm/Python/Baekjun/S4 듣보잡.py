import sys

input = sys.stdin.readline

n, m = map(int, input().split())


people = []

ans = []
cnt = 0
for i in range(n):
    people.append(input())

for j in range(m):
    name = input()

    if name in people:
        cnt += 1
        ans.append(name)

print(cnt)
ans.sort()

for i in ans:
    print(i)