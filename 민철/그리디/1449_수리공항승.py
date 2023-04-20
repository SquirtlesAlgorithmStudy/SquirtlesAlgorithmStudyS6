import sys

N, L = map(int, sys.stdin.readline().split())
coords = sorted(list(map(int, sys.stdin.readline().split())))

answer = 0
last = 0

for coord in coords:
    if coord + 0.5 > last:
        answer += 1
        last = coord - 0.5 + L

print(answer)
