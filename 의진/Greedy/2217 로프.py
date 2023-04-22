import sys
input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
result = 0
for idx, rope in enumerate(sorted(ropes, reverse=True)):
    result = max(result, (rope * (idx + 1)))
print(result)
