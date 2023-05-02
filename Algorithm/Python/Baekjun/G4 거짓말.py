import sys

input = sys.stdin.readline


def findboss(x):
    if relations[x] == 0:
        return x
    rst = findboss(relations[x])
    return rst


def union(a, b):
    aboss = findboss(a)
    bboss = findboss(b)
    if aboss == bboss:
        return
    relations[bboss] = aboss


n, m = map(int, input().split())
tPerson = list(map(int, input().split()))
party = [[0]] + [list(map(int, input().split())) for _ in range(m)]

relations = [0] * 51

for i in range(1, m + 1):
    std = party[i][1]
    for j in range(1, len(party[i])):
        if findboss(std) != findboss(party[i][j]):
            union(std, party[i][j])


# for i in range(1, len(tPerson)):
#     relations[tPerson[i]] = 55
print(findboss(4))
print(relations)
#
# for i in range(1, m + 1):
#     for j in range(1, len(party[i])):
#         if relations[party[i][j]] != 0:
#             m -= 1
#             break
#
# print(m)
