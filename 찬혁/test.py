# import sys

# input = sys.stdin.readline

# N, M = map(int, input().split())

# A = [list(map(int,input().split())) for _ in range(N)]
# B = [list(map(int,input().split())) for _ in range(N)]

# for a, b in zipA, B:
#     print(a, b)
# print(A, B)
from collections import deque
n = 2

cand = deque([(i,j) for i in range(n) for j in range(i%2,n,2)])

print(cand)