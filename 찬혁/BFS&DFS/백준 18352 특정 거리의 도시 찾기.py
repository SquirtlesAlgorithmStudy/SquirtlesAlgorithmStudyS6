import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int,input().split())
road_dic={}
visited = set()
answer = []

def bfs(node, cnt):
    que = deque([(node,cnt)])
    while que:
        node, cnt = que.popleft()
        visited.add(node)

        if node not in road_dic.keys():
            return

        for n in road_dic[node]:
            if n in visited:
                continue

            if cnt+1 == K: 
                answer.append(n)
                visited.add(n)

            elif n in road_dic.keys():
                que.append((n, cnt+1))
                visited.add(n)
            
            else:
                visited.add(n)

for _ in range(M):
    A, B = map(int,input().split())
    if road_dic.get(A) == None:
         road_dic[A] = [B]
    else:
        road_dic[A].append(B)

bfs(X, 0)

if len(answer) == 0:
    print(-1)
else:
    print(*sorted(answer), sep='\n')