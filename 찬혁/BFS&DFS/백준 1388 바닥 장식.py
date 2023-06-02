import sys

input = sys.stdin.readline

N, M = map(int,input().split())
board = [list(input().rstrip()) for _ in range(N)]
answer = 0

def dfs(n, m, re_deco):
    if n >= N or m >= M or board[n][m] != re_deco:
        return

    if board[n][m] == '-':
        dfs(n, m+1, board[n][m])
        board[n][m] = 0

    elif board[n][m] == '|':
        dfs(n+1, m, board[n][m])
        board[n][m] = 0

for n in range(N):
    for m in range(M):
        deco = board[n][m]
        if deco != 0 and deco == '-':
            answer+=1
            dfs(n, m+1, deco)
            board[n][m] = 0

        elif deco != 0 and deco == '|':
            answer+=1
            dfs(n+1, m, deco)
            board[n][m] = 0

print(answer)

