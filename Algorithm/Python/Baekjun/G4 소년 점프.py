import sys, heapq
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]

for i in range(3):
    y, x = map(int,input().split())
    maze[y][x] = -1

