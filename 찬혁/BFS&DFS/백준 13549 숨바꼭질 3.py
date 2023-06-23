import sys
from collections import deque

N, K = map(int, input().split())  
que = deque()
que.append(N) 
visited = [-1] * 100001
visited[N] = 0

while que:
    loca = que.popleft()
    if loca == K:
        print(visited[loca])
        break
    
    if 0 <= loca-1 < 100001 and visited[loca-1] == -1:
        visited[loca-1] = visited[loca] + 1
        que.append(loca-1)
    if 0 < loca*2 < 100001 and visited[loca*2] == -1:
        visited[loca*2] = visited[loca]
        que.appendleft(loca*2)  
    if 0 <= loca+1 < 100001 and visited[loca+1] == -1:
        visited[loca+1] = visited[loca] + 1
        que.append(loca+1)


