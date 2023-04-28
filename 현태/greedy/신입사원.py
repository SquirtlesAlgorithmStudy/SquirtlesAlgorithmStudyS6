import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    scores = [list(map(int,input().split())) for _ in range(n)]

    # 서류 심사 순위를 기준으로 오름차순 정렬
    scores.sort(key = lambda x : x[0])

    count = 1
    min_interview_score = scores[0][1]
    for j in range(1, n):
        # 현재 지원자의 면접 성적이 이전 지원자의 면접 성적보다 높으면
        if scores[j][1] < min_interview_score:
            count += 1
            min_interview_score = scores[j][1]

    print(count)
