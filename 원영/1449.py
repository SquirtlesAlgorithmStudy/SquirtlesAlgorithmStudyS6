# 물이 새는 곳마다 1의 길이가 필요
# 물 새는 곳 수에서 테이프의 길이가 몇번 반복되어 필요하는지를 걔산
import sys
import math

N, L = map(int,sys.stdin.readline().split())
pipe = list(map(int,sys.stdin.readline().split()))
pipe.sort()

print(math.ceil(N/L))