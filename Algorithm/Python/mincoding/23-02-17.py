## 같은 단어 찾기


def longst(a,b):
    global L1, L2
    if a > b:
        L1 = a
        L2 = b
    else :
        L1 = b
        L2 = a

st1 = input()
st2 = input()

L1 = len(st1)
L2 = len(st2)
longst(L1,L2)  ## 길이 긴 문자열 L1에 저장

maxL = 0
maxst = 0
maxed = 0
for l1 in range(L1):

    for l2 in range(L2):
        ans = []
        if st1[l1] == st2[l2]:
            ans.append(st2[l2])
            for i in range(1,L2-l2):
                if l1+i < L1 and l2+i <L2:
                    if st1[l1+i] == st2[l2+i]:
                        ans.append(st2[l2+i])
                        temped = l2 + i
            if len(ans) > maxL:
                maxL = len(ans)
                maxst = l2
                maxed = temped + 1
print(st2[maxst:maxed])