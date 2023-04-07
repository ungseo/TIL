import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    flag = 0
    stack = []
    check = list(input())
    if len(check) % 2 == 0:
        print('NO')
        flag = 1
    if check[0] == ')':
        print('NO')
        flag = 1

    if flag == 0:
        for i in range(len(check)):
            stack.append(check[i])
            if stack[-2]

