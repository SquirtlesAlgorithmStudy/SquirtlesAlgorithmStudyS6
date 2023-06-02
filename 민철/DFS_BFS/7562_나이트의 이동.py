from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    queue = deque()
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()

        if x == e_x and y == e_y:
            return graph[x][y]
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                
case_count = int(input().rstrip())    
        
for case in range(case_count) :
    l = int(input().rstrip())
    s_x, s_y = map(int, input().rstrip().split())
    e_x, e_y = map(int, input().rstrip().split())
    graph = [[0] * l for _ in range(l)]
    print(bfs(s_x, s_y))