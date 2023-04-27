# 최소 위치는 집 위치 중에 중간값
import sys

N = int(sys.stdin.readline()) # 입력값 받기
house = list(map(int,sys.stdin.readline().split()))

house.sort()

# 홀짝 구분
if N%2==0: print(house[N//2-1])
else: print(house[N//2])