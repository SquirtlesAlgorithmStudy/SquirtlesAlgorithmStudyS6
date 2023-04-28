import sys
input = sys.stdin.readline

test = int(input()) # test case

for t in range(test):
    n = int(input()) # 지원자 숫자
    score = [list(map(int,input().split())) for _ in range(n)] # 지원자 점수들
    score = sorted(score) # 오름차순 정렬
    top = 0
    result = 1
    for i in range(1,len(score)):
        if score[i][1]<score[top][1]: # 점수 높은 사람하고 비교
            top = i
            result += 1

    print(result)