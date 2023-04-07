import sys
from collections import deque
input =sys.stdin.readline

n = int(input())
stack = deque()
for i in range(n):
    cmd = list(input().split())
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if stack:
            a = stack.popleft()
            print(a)
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif cmd[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
