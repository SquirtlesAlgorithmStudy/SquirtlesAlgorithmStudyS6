import sys
input = sys.stdin.readline

N = int(input())
lopes = [int(input()) for _ in range(N)]
result = 0
for idx, lope in enumerate(sorted(lopes, reverse=True)):
    result = max(result, (lope * (idx + 1)))
print(result)
