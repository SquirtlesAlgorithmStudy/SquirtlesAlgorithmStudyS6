# 도화지의 크기만큼 반복
# 만약 색종이가 존재한다면 1로 채워줌
# 아이디어가 도저히 안떠올라서 블로그 참고했습니다.
import sys

n = int(sys.stdin.readline())
board = [[0]*100 for _ in range(100)]

for _ in range(n):
    y,x = map(int,sys.stdin.readline().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            board[i][j] = 1
            
cnt = 0
for a in board:
    cnt += a.count(1)

print(cnt)