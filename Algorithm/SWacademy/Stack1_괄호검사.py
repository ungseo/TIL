'''난이도 D2'''

'''접근
스택사용.
연속으로 반대괄호 나오면 pop해버리기
아니면 그대로 스택에 추가
탐색 끝나면 반 짤라서 이진탐색으로 확인'''


T = int(input())

for tc in range(1,T+1):
    code = input()
    stack = [0]
    lst1 = ['(', ')']
    lst2 = ['{', '}']

    for st in range(len(code)):
        if code[st] in lst1 or code[st] in lst2:
            if stack[-1] == '(' and code[st] == ')':
                stack.pop()
            elif stack[-1] == '{' and code[st] == '}':
                stack.pop()
            else:
                stack.append(code[st])

    stack = stack[1:]

    flag = 1
    first = 0
    second = -1
    if len(stack) > 1 or len(stack) == 0:
        while first < len(stack)//2:
            if len(stack) % 2 == 1:
                flag = 0
                break
            if stack[first] != stack[second]:
                flag = 0
                break
            else:
                first += 1
                second -= 1
    else:
        flag = 0
    print(f'#{tc} {flag}')




