from collections import deque

number = int(input())

q = []
for i in range(number):
  q.append(i+1)

dq = deque(q)

while len(dq) > 1 :
  dq.popleft()
  dq.rotate(-1)

print(dq[0])  