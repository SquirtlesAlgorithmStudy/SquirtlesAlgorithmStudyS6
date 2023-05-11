import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([i + 1 for i in range(N)])
answer = 0

while queue:
    if len(queue) == 1:
        answer = queue[0]
        break

    queue.popleft()
    a = queue.popleft()      
    queue.append(a)       
    
print(answer)