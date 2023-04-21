import sys
input = sys.stdin.readline

N, L = map(int, input().split())
leaking_points = list(map(int, input().split()))

result = 0
threshold = 0
for leaking_point in sorted(leaking_points):
    if leaking_point >= threshold:
        result += 1
        threshold = leaking_point + L

print(result)
