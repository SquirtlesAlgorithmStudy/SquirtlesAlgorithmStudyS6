import sys

input = sys.stdin.readline

n, l = list(map(int, input().split()))
leaks = list(map(int, input().split()))
leaks.sort() 

count = 1 
tape_p = leaks[0]
for i in range(1, len(leaks)):
    if leaks[i] - tape_p >= l:
        count += 1 
        tape_p = leaks[i]

print(count)
   
