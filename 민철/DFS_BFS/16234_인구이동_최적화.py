from collections import deque
n, l, r = map(int, input().split())

graph = []
answer = 0
for i in range(n):
    graph.append(list(map(int, input().split())))

#상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, moved):
    queue = deque()
    queue.append((x, y))
    federation = [(x, y)]
    population_sum = graph[x][y]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue

            if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                visited[nx][ny] = 1
                federation.append((nx, ny))
                population_sum += graph[nx][ny]
                queue.append((nx, ny))
                moved = True
            else:
                continue
        
    for x, y in federation:
        graph[x][y] = population_sum // len(federation)

    return federation,  moved

first = True
while True:
    moved = False
    visited = [[0] * n for _ in range(n)]
    
    if first:
        to_check = []
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    visited[i][j] = 1
                    federation, moved = bfs(i, j, moved)
                    to_check.extend(federation)
        first = False
        
    else:
        last_moved = to_check.copy()
        to_check = []
        for i, j in last_moved:
            if not visited[i][j]:
                visited[i][j] = 1
                federation, moved = bfs(i, j, moved)
                to_check.extend(federation)
                    
    if not moved:
        break
    else:
        answer += 1

print(answer)
