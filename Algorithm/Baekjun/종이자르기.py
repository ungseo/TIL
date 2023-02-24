x, y = map(int,input().split())

cut = int(input())
garo = []
sero = []
wide = [0]
height = [0]
for c in range(cut):
    direction, point = map(int,input().split())
    if direction == 0:
        garo.append((direction, point))
    else:
        sero.append((direction, point))

sero.sort(key= lambda x: x[1])
garo.sort(key= lambda x: x[1])

for w in range(len(sero)):
    wide.append(sero[w][1]-wide[w])
wide.append(x-wide[w+1])

for h in range(len(garo)):
    height.append(garo[h][1]-height[h])
height.append(y-height[h+1])

print(max(height)*max(wide))