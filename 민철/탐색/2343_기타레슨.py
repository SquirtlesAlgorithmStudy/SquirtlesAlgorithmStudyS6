import sys

N, M = map(int, sys.stdin.readline().split())
bluerays = list(map(int,sys.stdin.readline().split()))

start, end = max(bluerays), sum(bluerays)

while start <= end: 
    mid = (start + end) // 2
    
    blueray_sum = 0
    blueray_count = 1
    save_all = True
    
    for blueray in bluerays:
        if blueray_sum + blueray > mid:
            if blueray_count + 1 <= M:
                blueray_count += 1
                blueray_sum = 0
            else:
                save_all = False
                break
        blueray_sum += blueray        
    
    if not save_all:
        start = mid + 1
    else:
        end = mid - 1
        
print(start)