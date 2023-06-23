import sys
from collections import deque


def bfs(N):
    que = deque([(N, 0)])

    while que:
        print(que)
        subin, cnt = que.popleft()
        move_subin = [subin*2, subin-1, subin+1]

        for idx, m in enumerate(move_subin):
            s_cnt = cnt
            if m < 0 or m >= 100000 or m in visited:
                continue

            if idx != 0:
                s_cnt += 1

            if m == K:
                return s_cnt

            que.append((m, s_cnt))
            visited.add(m)


input = sys.stdin.readline

N, K = map(int, input().split())

visited = {N}

if N == K:
    print(0)
else:
    print(bfs(N))
