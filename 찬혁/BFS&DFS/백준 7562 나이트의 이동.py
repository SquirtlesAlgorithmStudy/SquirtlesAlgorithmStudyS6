#수정해야함

import sys
from collections import deque

def bfs():
    que = deque([knight])
    while que:
        print(que)
        r, c, cnt= que.popleft()
        if board[r][c] == 2:
            return cnt

        for d in range(8):
            dr = r + dx[d]
            dc = c + dy[d]

            print(dr, dc)
            if dr < 0 or dc < 0 or dr >= board_len or dc >= board_len or visited[dr][dc] == 1:
                continue
            
            board[dr][dc] = 0
            que.append([dr,dc,cnt+1])
            visited[dr][dc] = 1

input = sys.stdin.readline

Case = int(input().rstrip())

dx = [-2,-1,1,2,2,1,-1,2]
dy = [1,2,2,1,-1,-2,-1,-2]

for _ in range(Case):

    board_len= int(input())
    knight = list(map(int, input().split()))+[0]
    knight_m = list(map(int, input().split()))
    board = [[-1] * board_len for _ in range(board_len)]
    visited = [[0] * board_len for _ in range(board_len)]

    board[knight[0]][knight[1]] = -1
    visited[knight[0]][knight[1]] = 1
    board[knight_m[0]][knight_m[1]] = 2
    print(bfs())