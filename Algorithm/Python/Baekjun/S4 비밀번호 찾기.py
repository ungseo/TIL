import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

dic = {}

for i in range(16):
    a, b = input().rstrip().split()
    if a not in dic:
        dic[a] = b

for j in range(4):
    site = input().rstrip()
    print(dic[site])