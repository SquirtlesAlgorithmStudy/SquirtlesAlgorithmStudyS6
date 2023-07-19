import sys

N = int(sys.stdin.readline())
cards = [0] + list(map(int, sys.stdin.readline().split()))
d = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + cards[j])

print(max(d))