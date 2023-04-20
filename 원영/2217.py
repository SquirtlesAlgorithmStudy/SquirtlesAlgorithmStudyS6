# 로프를 병렬 연결 하려면, 무게가 가벼울수록 연결 갯수가 커진다.
import sys

N = int(sys.stdin.readline()) # 입력값 받기
rope = [int(sys.stdin.readline().strip()) for i in range(N)]
rope.sort(reverse=True)

answer = []
for i in range(N):
    answer.append(rope[i]*(i+1))

print(max(answer))