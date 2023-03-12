'''난이도 D3'''

for tc in range(1):
    L, lst = map(str,input().split())
    L = int(L)

    stack = [0]

    for i in range(L):
        if stack[-1] == lst[i]:
            stack.pop()
        else:
            stack.append(lst[i])
    stack = stack[1:]
    rst = ''.join(stack)

    print(f'#{tc} {rst}')