import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

def bfs(x,y):
    # 방향키 설정 # 우좌상하
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    # 배추가 있는지 주변 확인
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0<=nx<m) and (0<=ny<n):
            if board[nx][ny]==1: # 배추가 주변에 있는 경우
                board[nx][ny]=0 # 중복 확인 방지를 위해 초기화
                bfs(nx,ny)


t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    m,n,k = map(int,input().split()) # 가로, 세로, 배추 위치 수
    board = [[0 for _ in range(n)] for  _ in range(m)] # 배추밭 초기화
    cnt = 0 # 지렁이 수 초기화

    for i in range(k):
        x,y = (map(int, input().split())) # 배추 위치 입력
        board[x][y] = 1

    for i in range(m):
        for j in range(n):
            if board[i][j]==1: # 배추가 있다면
                bfs(i,j)
                cnt += 1 # 배추 지렁이 +1
    print(cnt)