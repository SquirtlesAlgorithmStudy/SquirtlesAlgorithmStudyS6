#완전 탐색: 모든 지원자를 비교하며 탈락자 or 합격자를 가려내야 한다. -> 시초 100%
#정렬을 통해 시간을 줄이고 판단하는 영역도 줄일 수 있다.

#풀이
#(서류성적, 면접성적)의 list를 서류성적으로 정렬하고 반복하며 다음 index가 면접 성적보다 낮으면 탈락 높으면 합격, 기준 숫자 변경

import sys

input = sys.stdin.readline

T = int(input().rstrip())

for i in  range(T):
    answer = 0
    N = int(input().rstrip())
    score = [list(map(int,input().split())) for i in range(N)]
    
    score.sort(key = lambda x: x[0])

    interview_min = -sys.maxsize
    for s in score:
        if s[0] != 1 and interview_min < s[1]:
            continue

        if interview_min > s[1]:
            interview_min = s[1]
            answer += 1
    
    print(answer)