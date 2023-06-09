from collections import deque
n, k = map(int, input().split())
road = [-1] * 100001
road[n] = 0

def bfs(x):
    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()

        if x == k:
            return road[x]

        for nx in [x - 1, x + 1, 2 * x]:
            if nx < 0 or nx > 100000 or road[nx] != -1:
                continue
            
            if nx == 2 * x:
                queue.appendleft(nx)
                road[nx] = road[x]
            else:
                queue.append(nx)
                road[nx] = road[x] + 1
            
answer = bfs(n)
print(answer)