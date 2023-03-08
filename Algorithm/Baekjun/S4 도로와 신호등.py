n, l = map(int,input().split())
road = [0] * (l+1)
for i in range(n):
    d, r, g = map(int,input().split())
    road[d] = 1

move = 0
while move != l:
    move += 1
    if road[move] == 1:
        if move%