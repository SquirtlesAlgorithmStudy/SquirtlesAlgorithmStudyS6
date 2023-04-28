import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# board[N][M]

max_value = max([max(board[i]) for i in range(N)])
min_value = min([min(board[i]) for i in range(N)])

result = -1
best_time = sys.maxsize
for height in range(min_value, max_value+1):
    time = 0
    sum_value = 0
    for i in range(N):
        for j in range(M):
            difference = board[i][j] - height
            sum_value = sum_value + difference
            if difference > 0:
                time += (2 * difference)
            else:
                time += (-difference)
    if B + sum_value >= 0 and best_time >= time:
        result = height
        best_time = time
    else:
        continue
print(best_time, result)
