def service(y, x, k):


movy = [-1,0,1,0]
movx = []
T = int(input())

for tc in range(1, T+1):
    n, m = map(int,input().split())
    city = [list(map(int,input().split())) for _ in range(n)]

    if m > 1: # m이 1이 아닐때,
