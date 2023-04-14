import sys
input = sys.stdin.readline

s = input().rstrip()
nowValue = -1
count = 0

for letter in s:
    if int(letter) != nowValue:
        count += 1
        nowValue = int(letter)

print(count // 2)
