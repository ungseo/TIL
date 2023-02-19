'''난이도 D3'''
import sys
sys.stdin = open('input.txt','r')
#
# for i in range(10):
#     tc = int(input())
#     N, M = map(int,input().split())
#
#     def gopgop(time):
#         if time == 1:
#             return N
#         elif time > 1:
#             return gopgop(time-1) * N
#
#     print(f'#{tc} {gopgop(M)}')


for i in range(10):
    tc = int(input())
    N, M = map(int, input().split())

    rst = 0
    def jegop(level, gop):
        global rst
        if level == M:
            rst = gop
            return

        jegop(level+1, gop*N)

    jegop(1,N)
    print(f'#{tc} {rst}')
