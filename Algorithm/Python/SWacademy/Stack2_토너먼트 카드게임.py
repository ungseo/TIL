'''난이도 D2'''
def winner(a,b):
    if a == b:
        return a
    elif a-b == -1 or a-b == 2:
        return a
    else:
        return b



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int,input().split()))

