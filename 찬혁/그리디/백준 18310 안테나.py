import sys

N = int(input())
print(sorted(list(map(int,sys.stdin.readline().split())))[(N-1)//2])