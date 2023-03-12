# N, M = map(int,input().split())
# lst = list(map(int,input().split()))
# for tc in range(M):
#     i, j = map(int,input().split())
#     temp = lst[i-1:j]
# sum = 0
# for i in temp:
#     sum += i
# print(sum)


def pal(m, st):
    # 절반씩 나눠서 한쪽을 거꾸로 만든것과 일치하는지 체크
    if m % 2 == 0:
        if st[:m // 2] == st[m // 2:][::-1]:
            return st
    else:
        if st[:(m + 1) // 2 - 1] == st[(m + 1) // 2:][::-1]:
            return st
    return False

def hor(m, lst):
    for i in range(len(lst)):
        for j in range(1):
            st = lst[i][j:j+m]
            ans = pal(m, st)
            if ans:
                return st
    return False

# test

lst = [[input()] for i in range(10)]
print(hor(10, lst))