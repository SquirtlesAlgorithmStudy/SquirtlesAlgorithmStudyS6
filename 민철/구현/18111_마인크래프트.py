#PyPy로 제출해야 통과
import sys

N, M, B = map(int,input().split())
mat = []
for _ in range(N):
    mat.append([x for x in map(int, sys.stdin.readline().rstrip().split())])

answer = sys.maxsize
height = 0

for i in range(min(map(min, mat)), max(map(max, mat)) + 1):
    use = 0
    get = 0
    for x in range(N):
        for y in range(M):
            if mat[x][y] > i: #i: 기준이 되는 층
                get += mat[x][y] - i
            else:
                use += i - mat[x][y]
    if use > get + B:
        continue

    count = use + 2 * get
    if count <= answer:
        answer = count
        height = i

print(answer, height)