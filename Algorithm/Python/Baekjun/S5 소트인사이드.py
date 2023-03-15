

num = list(map(int, list(input().rstrip())))

num.sort(reverse=True)

for i in num:
    print(i, end='')


import sys

input = sys.stdin.readline


N=list(input().rstrip())
# 정렬시 int로 보고 정렬, 내림차순이므로 reverse 사용
N.sort(key=int,reverse=True)
# 문자열을 합치기 위한 join
print(*N)