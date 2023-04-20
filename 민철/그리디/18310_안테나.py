import sys

N = int(sys.stdin.readline())
houses = sorted(list(map(int, sys.stdin.readline().split())))

print(min(houses[(N - 1) // 2], houses[N // 2]))