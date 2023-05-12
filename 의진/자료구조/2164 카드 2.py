from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
dq = deque([i for i in range(n, 0, -1)])

while len(dq) != 1:
    dq.pop()
    dq.appendleft(dq[len(dq)-1])
    dq.pop()

print(dq[0])
