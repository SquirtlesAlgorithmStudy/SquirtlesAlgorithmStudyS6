import sys

N, L = map(int, sys.stdin.readline().split())
hole = sorted(list(map(int, sys.stdin.readline().split())))

start,end = hole[0],hole[0]+L
cnt = 1
for i in range(len(hole)):
    if start <= hole[i] < end:
        continue
    else:
        start = hole[i]
        end = hole[i] + L
        cnt += 1
print(cnt)