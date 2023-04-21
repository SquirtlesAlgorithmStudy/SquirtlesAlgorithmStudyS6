import sys

rope = []

N = int(input())
for i in range(N):
    rope.append(int(sys.stdin.readline()))
    
for i, data in enumerate(sorted(rope, reverse=True)):
    rope[i] = data*(i+1)

print(max(rope))