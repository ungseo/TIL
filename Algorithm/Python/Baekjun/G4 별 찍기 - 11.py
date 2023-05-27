import sys

input = sys.stdin.readline

def printStar(x, level):
    if level == n - 2:
        return
    paper[level][x] = '*'
    paper[level+1][x-1] = '*'
    paper[level+1][x+1] = '*'
    for i in range(5):
        paper[level+2][x-2+i] = '*'

    printStar(x-3, level+3)
    printStar(x+3, level+3)




n = int(input())

paper = [[''] * (n * 2 + 1) for _ in range(n)]

dfs(n)