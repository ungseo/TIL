import sys

input = sys.stdin.readline

n = int(input().rstrip())
ans = 0
dic = {}
for i in range(n):
    st, ed = map(int, input().rstrip().split())
    if st == ed:
        ans += 1
    else:
        if st in dic:
            if dic[st] > ed:
                dic[st] = ed
        else:
            dic[st] = ed

dic = list(sorted(dic.items(), key=lambda x: x[1]))
if len(dic) == 0:
    print(ans)

else:
    if len(dic) == 1:
        print(ans + 1)
    else:
        st = dic[0]
        cnt = 1
        p = 0
        while 1:
            if p == len(dic) - 1:
                break
            p += 1
            if st[1] > dic[p][0]:
                continue
            else:
                st = dic[p]
                cnt += 1


        print(ans + cnt)
