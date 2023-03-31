import sys
sys.stdin = open('input.txt','r')

T = int(input())
num_l = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for tc in range(1, T + 1):
    n, n16 = input().split()
    n = int(n)
    n10 = 0
    for i in range(n):
        if n16[i] in num_l:
            n10 += (16 ** (n-1-i)) * num_l[n16[i]]
        else:
            n10 += (16 ** (n-1-i)) * int(n16[i])
    ans = []
    if n10 == 0:
        print(f'#{tc} 0')
    else:
        while n10 != 1:

            ans.append(str(n10 % 2))
            n10 //= 2
        ans.append('1')
        if len(ans) % 4 != 0:
            ans.append('0')
        a = ''.join(ans)
        a = a[::-1]
        print(f'#{tc} {a}')