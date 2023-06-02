import sys
from collections import deque

def bfs(row, col):

    union = set([(row,col)])  
    cnt = 1
    population = board[row][col]
    que = deque([(row, col)])
    while que:

        r, c = que.popleft()
        for d in range(4):
            dr = r + dx[d]
            dc = c + dy[d]

            if dr < 0 or dc < 0 or dr >= N or dc >= N or visited[dr][dc] == 1:
                continue
            
            if L <= abs(board[r][c] - board[dr][dc]) <= R:
                que.append((dr,dc))
                union.add((dr,dc))
                visited[dr][dc] = 1
                population += board[dr][dc]
                cnt += 1

    if len(union) > 1:
        for row, col in union:
            board[row][col] = population//cnt
        
        return 1
    
    else:
        return 0


input = sys.stdin.readline

N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

days =  0

while True:
    visited = [[0] * N for _ in range(N)]
    flag = 0
    for row in range(N):
        for col in range(N):
            if visited[row][col] == 1:
                continue

            visited[row][col] = 1
            flag += bfs(row, col)

    if flag == 0:
        break
    days+=1

print(days)