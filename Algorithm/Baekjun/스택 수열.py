n = int(input())
lst = []
ans = [int(input()) for _ in range(n)]
stack = []
alst = []

idx = 0
for i in range(1,n+1):
    lst.append(i)
    alst.append('+')
    while lst and lst[-1] == ans[idx]:
        stack.append(lst.pop())
        idx += 1
        alst.append('-')

if len(alst) == n*2:
    for i in alst:
        print(i)
else:
    print('NO')


