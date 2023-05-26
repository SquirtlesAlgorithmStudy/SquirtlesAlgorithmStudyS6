from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().strip().split())
road = [[] for _ in range(n+1)]
for _ in range(m):
    dep, des = map(int, input().strip().split())
    road[dep].append(des)
visited = [-1] * (n+1)


def bfs(graph, start):
    global k
    global visited
    queue = deque([start])
    visited[start] = k

    while queue:
        v = queue.popleft()
        if visited[v] == k:
            k -= 1
        if k == -1:
            break
        for i in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = k


bfs(road, x)
cnt = 0
for i in range(n+1):
    if visited[i] == 0:
        print(i)
        cnt += 1
if cnt == 0:
    print(-1)
