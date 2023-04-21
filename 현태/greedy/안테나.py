import sys

input = sys.stdin.readline

n = int(input())
places = list(map(int, input().split()))

places.sort() 


if n % 2 == 0:
    mid = places[n//2 - 1] 
else:
    mid = places[n//2]


print(mid)