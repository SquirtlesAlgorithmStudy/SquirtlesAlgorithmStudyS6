import sys

N, M = map(int,sys.stdin.readline().split())
# N, M = 100, 50

dxdy = [(2, 1), (1, 2), (-1, 2), (-2, 1)]

if __name__ == "__main__":

    def all_use(path):
        return path[0] > 0 and path[1] > 0 and path[2] > 0 and path[3] > 0
    
    def is_inside(x, y):
        return x > -1 and x < N and y > -1 and y < M
    
    def dfs(start):
        stack = [(start, [0, 0, 0, 0])]
        visit = [[False for _ in range(M)] for _ in range(N)]

        max_path = 0
        while stack:
            top, path = stack.pop()
            visit[top[0]][top[1]] = True
            max_path = max(max_path, sum(path))

            for i, dd in enumerate(dxdy):
                new_top = top[0] + dd[0], top[1] + dd[1]
                new_path = [path[0], path[1], path[2], path[3]]
                new_path[i] += 1

                if is_inside(new_top[0], new_top[1]):
                    if not visit[new_top[0]][new_top[1]]:
                        stack.append((new_top, new_path))

        return max_path + 1

    # N, M = 2, 3
    def search():

        answer = 0
        if N == 1:
            answer = 1
        elif N == 2:
            answer = min(4, (M + 1) // 2)
        else:
            if M < 4:
                answer = M
            elif M < 7:
                answer = 4
            else:
                answer = M-2
        print(answer)

    search()
