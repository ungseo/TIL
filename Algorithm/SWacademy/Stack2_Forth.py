T = int(input())
 
for tc in range(1, 1+T):
    pre = list(map(str, input().split()))
    stack = []
    line = ['+','-','*','/','.']   # 연산자 모음
     
    for i in range(len(pre)):     # 선형탐색
        if pre[i] not in line:        # 연산자 아니고 숫자면
            stack.append(int(pre[i]))  # 스택에 숫자로 저장
         
        elif pre[i] == '+':
            if len(stack) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            else:
                print(f'#{tc} error')
                break
        elif pre[i] == '-':
            if len(stack) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            else:
                print(f'#{tc} error')
                break
        elif pre[i] == '*':
            if len(stack) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            else:
                print(f'#{tc} error')
                break
        elif pre[i] == '/':
            if len(stack) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(b//a)
            else:
                print(f'#{tc} error')
                break
        else:
            if len(stack) != 1:           #### 이조건때문에 계속틀렸네...
                print(f'#{tc} error')
            else:
                print(f'#{tc} {stack.pop()}')

        ## 틀린건 컴퓨터가 아니라 나였고 ^^..;