'''난이도 D2'''
def ssdel():
    global st
    for idx in range(len(st)-1):
        if st[idx] == st[idx+1]:
            if idx+2 < len(st):
                st = st[:idx] + st[idx+2:]
            else:
                st = st[:idx]

T = int(input())

for tc in range(1,T+1):
    st = list(input())
    while st:
        ssdel()

print(st)
