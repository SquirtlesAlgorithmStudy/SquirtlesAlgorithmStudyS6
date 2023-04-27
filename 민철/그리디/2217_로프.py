import sys

n =  int(sys.stdin.readline())

ropes = [int(sys.stdin.readline()) for _ in range(n)]
ropes.sort(reverse = True)
answer = 0

for i, rope in enumerate(ropes):
    if (i + 1) * rope > answer:
        answer = (i + 1) * rope

print(answer)
