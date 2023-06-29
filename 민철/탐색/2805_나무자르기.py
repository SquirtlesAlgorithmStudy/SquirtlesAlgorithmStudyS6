import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

start, end = 1, max(trees) 

while start <= end: 
    mid = (start + end) // 2
    
    tree_sum = sum([tree - mid if tree - mid > 0 else 0 for tree in trees])
    
    if tree_sum >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
