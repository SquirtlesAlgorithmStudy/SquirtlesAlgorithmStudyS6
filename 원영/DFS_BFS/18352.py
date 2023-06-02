from collections import deque
import sys

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
city = [[] for _ in range(n+1)] 
distance = [0] * (n+1)
visited = [0] * (n+1)

# 도시 정보
for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)


def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in city[now]:
            if not visited[i]: # 방문하지 않았을 경우
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1 # 도시 간 거리 +1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0: # k인 도시가 없다면
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)

bfs(x)