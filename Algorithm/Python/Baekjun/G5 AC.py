import sys

input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    p = list(input().rstrip())
    n = int(input())
    lst = input().rstrip()
    if len(lst) == 2:
        st = []
    else:
        st = list(map(str, lst[1:len(lst) - 1].split(',')))
    if p.count('D') > n:
        print('error')
    else:
        flag = 1

        for i in range(len(p)):
            if p[i] == 'R':
                st = st[::-1]
            else:
                if st:
                    st.pop(0)

                else:
                    flag = 0
                    break
        if flag == 1:
            rst = '[' + ','.join(st) + ']'
            print(rst)
        else:
            print('error')