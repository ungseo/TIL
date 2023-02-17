# N, M = map(int,input().split())
# lst = list(map(int,input().split()))
# for tc in range(M):
#     i, j = map(int,input().split())
#     temp = lst[i-1:j]
# sum = 0
# for i in temp:
#     sum += i
# print(sum)

#
# def pal(m, st):
#     # 절반씩 나눠서 한쪽을 거꾸로 만든것과 일치하는지 체크
#     if m % 2 == 0:
#         if st[:m // 2] == st[m // 2:][::-1]:
#             return st
#     else:
#         if st[:(m + 1) // 2 - 1] == st[(m + 1) // 2:][::-1]:
#             return st
#     return False
#
# def hor(m, lst):
#     for i in range(len(lst)):
#         for j in range(1):
#             st = lst[i][j:j+m]
#             ans = pal(m, st)
#             if ans:
#                 return st
#     return False
#
# # test
#
# lst = [[input()] for i in range(10)]
# print(hor(10, lst))

''' 입력
3
4
5
6
'''

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i = j = dr = 0  # 초기값 설정
    for cnt in range(1, N * N + 1):
        arr[i][j] = cnt  # 현재좌표에 숫자 기록
        ni, nj = i + di[dr], j + dj[dr]  # 이동할 위치 계산

        # 이동할 위치가 범위내 and 빈칸(==0)인경우 이동
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:  # 방향을 꺽어서 이동위치 다시 계산
            dr = (dr + 1) % 4  # 0-1-2-3-1-2..
            i, j = i + di[dr], j + dj[dr]

    print(f'#{test_case}')
    for lst in arr:
        print(*lst)