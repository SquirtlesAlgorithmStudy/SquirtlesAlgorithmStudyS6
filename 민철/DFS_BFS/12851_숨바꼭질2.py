from collections import deque
n, k = map(int, input().split())
road = [0] * 100001

def bfs(x):
    answer = 0
    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()

        if x == k:
            answer += 1
            continue
            
        for nx in [x - 1, x + 1, 2 * x]:
            if nx < 0 or nx > 100000 or (road[nx] and road[nx] != road[x] + 1):
                continue
            queue.append(nx)
            road[nx] = road[x] + 1

    return road[k], answer

time, answer = bfs(n)
print(time)
print(answer)