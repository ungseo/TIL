import sys

tenPaper = [list(map(int, input().split())) for _ in range(10)]
x, xx, xxx, xxxx, xxxxx = 5


def check5(y, x):
    for i in range(y, y + 5):
        for j in range(x, x + 5):
            if tenPaper[i][j] == 0:
                return 0
    return 1


def check4(y, x):
    for i in range(y, y + 4):
        for j in range(x, x + 4):
            if tenPaper[i][j] == 0:
                return 0
    return 1


def check3(y, x):
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            if tenPaper[i][j] == 0:
                return 0
    return 1


def check2(y, x):
    for i in range(y, y + 2):
        for j in range(x, x + 2):
            if tenPaper[i][j] == 0:
                return 0
    return 1


def check1(y, x):
    for i in range(y, y + 1):
        for j in range(x, x + 1):
            if tenPaper[i][j] == 0:
                return 0
    return 1


for i in range(10):
    for j in range(10):
        if tenPaper[i][j] == 1:
            if i <= 5 and j <= 5:
                for s in range(5):

            elif i <= 6 and j <= 6:
                check4(i, j)
                check3(i, j)
                check2(i, j)
                check1(i, j)

            elif i <= 7 and j <= 7:
                check3(i, j)
                check2(i, j)
                check1(i, j)
            elif i <= 8 and j <= 8:
                check2(i, j)
                check1(i, j)
            elif i <= 9 and j <= 9:
                check1(i, j)
