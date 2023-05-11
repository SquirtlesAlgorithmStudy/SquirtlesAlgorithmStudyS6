#완전 탐색: 256 * 500 * 500으로 생각보다 높지 않음
#0부터 256층까지 블록의 개수를 생각해 보며 시간을 계산해 본다.

#풀이
#Counter로 블록높이 마다의 개수를 세어줌
#256번 반복하며 파야할 블록과 덮어야할 블록의 개수를 카운트 해봄
#판 블록 + 기존의 블록 >= 덮아야할 블록 and 총시간 <= 기존 시간 이라면 그것이 최소 시간


import sys
from collections import Counter
input = sys.stdin.readline

N, M, B = map(int,input().split())
answer_time,answer_height = sys.maxsize,0

height_dic = Counter()

for _ in range(N):
    height_dic += Counter(map(int,input().split()))

for height in range(257):
    dig_block, cover_block = 0, 0

    for h, cnt in height_dic.items():
        if height <= h:
            dig_block += (h-height)*cnt
        else:
            cover_block += (height-h)*cnt

    if dig_block + B >= cover_block and dig_block*2 + cover_block <= answer_time:
        answer_time = dig_block*2 + cover_block
        answer_height = height

print(answer_time, answer_height)
