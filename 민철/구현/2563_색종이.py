import sys

n =  int(sys.stdin.readline())
mat = [[0] * 100 for _ in range(100)]
answer = 0

for _ in range(n):
    x1, y1 = map(int, sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            mat[x1 + i][y1 + j] = 1

print(sum(map(sum, mat)))
