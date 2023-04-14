import sys

input = sys.stdin.readline()[:-1]

target = input[0]
answer = 0
flip = 0

for i in range(1, len(input)):
  if input[i] != target and flip == 0:
    answer += 1
    flip = 1
  elif input[i] == target:
    flip = 0

print(answer)
