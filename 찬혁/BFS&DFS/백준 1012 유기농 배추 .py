import sys
from collections import deque

input = sys.stdin.readline
T = int(input().rstrip())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(row, col):
    board[row][col] = 0
    que = deque([(row,col)])

    while que:
        row, col = que.popleft()
                    
        for d in range(4):
            dr = row + dx[d]
            dc = col + dy[d]

            if dr < 0 or dr >= M or dc < 0 or dc >= N or board[dr][dc] == 0:
                continue
                        
            board[dr][dc] = 0
            que.append((dr,dc))

for _ in range(T):
    M, N, K = map(int,input().split())
    answer = 0
    board = [[0] * N for _ in range(M)]

    for _ in range(K):
        row,col = map(int,input().split())
        board[row][col] = 1

    for row in range(M):
        for col in range(N):
            if board[row][col] == 1:
                bfs(row, col)
                answer += 1
                
    print(answer)