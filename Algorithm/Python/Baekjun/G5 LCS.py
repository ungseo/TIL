import sys

input = sys.stdin.readline

def cut(x):
    value = arr[x][0]

    for i in range(1, n-1):
        if x == 0:
            if arr[1][i] + arr[x][i+1] > arr[1][i+1]:
                value += arr[1][i]
                x = 1
            else:
                a = arr[0][i+1]
                b = arr[1][i+1]
                if a > b:
                    value += a
                    x = 0
                else:
                    value += b
                    x = 1

        else:
            if arr[0][i] + arr[1][i+1] > arr[0][i+1]:
                value += arr[0][i]
                x = 0
            else:
                a = arr[0][i + 1]
                b = arr[1][i + 1]
                if a > b:
                    value += a
                    x = 0
                else:
                    value += b
                    x = 1
    return value

T = int(input())

for tc in range(T):
    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(2)]

    rst1 = cut(0)
    rst2 = cut(1)

    print(max(rst1, rst2))

