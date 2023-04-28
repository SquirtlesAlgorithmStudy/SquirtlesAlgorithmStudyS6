import sys

N, M, B = map(int,input().split())
mat = []
for _ in range(N):
    mat.append([x for x in mat(int, sys.stdin.readline().rstrip().split())])

answer = sum(map(sum, mat))
height = 0

for i in range(min(mat), max(mat)):
    use = 0
    get = 0
    for x in range(N):
        for y in range(M):
            if mat[x][y] > i:
                get += mat[x][y] - i
            else:
                use += i - mat[x][y]

    count = get * 2 + use

    if use > get + B:
        continue

    if count <= answer:
        answer = count
        height = i

print(answer, height)