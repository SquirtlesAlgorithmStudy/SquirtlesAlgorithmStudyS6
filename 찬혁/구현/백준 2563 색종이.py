import sys

N = int(input())

board = [[0]*100 for _ in range(100)]
cnt = 0

for i in range(N):
    row, col = map(int,sys.stdin.readline().split())
    for i in range(row, row+10):
        for j in range(col, col+10):
            if board[i][j] == 0:
                board[i][j] = 1
                cnt += 1

print(cnt)
    