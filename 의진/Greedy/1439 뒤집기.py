import sys
input = sys.stdin.readline

s = input().rstrip()
now_value = -1
count = 0

for letter in s:
    if int(letter) != now_value:
        count += 1
        now_value = int(letter)

print(count // 2)
