import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
board = []
for _ in range(N):
    board.extend(list(map(int, input().split())))

max_value = max(board)
min_value = min(board)

result = -1
best_time = sys.maxsize
for height in range(min_value, max_value+1):
    time = 0
    sum_value = 0
    for i in range(N*M):
        difference = board[i] - height
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
