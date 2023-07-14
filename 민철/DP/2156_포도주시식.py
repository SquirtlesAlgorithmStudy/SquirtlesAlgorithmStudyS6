import sys

N = int(sys.stdin.readline())
wines = [int(sys.stdin.readline()) for _ in range(N)]
d = [0] * N
d[0] = wines[0]
if N >= 2:
    d[1] = d[0] + wines[1]
if N >= 3:
    d[2] = max(d[1], wines[1] + wines[2], d[0] + wines[2])

for i in range(3, N):
    #(i - 2, i - 1, i)중 어느 포도주를 건너뛸지
    d[i] = max(d[i - 3] + wines[i - 1] + wines[i], d[i - 2] + wines[i], d[i - 1])

print(max(d))