import sys
input = sys.stdin.readline
a, b = input().rstrip().split()
print(a, b)
print(1)

# 1. input은 "입력값을 입력해주세요 : " 이런 기능을 제공한다.
# 2. input은 마지막에 \n를 내보내지 않지만,
# readline은 \n을 마지막에 붙여서 내보낸다.
# 3. readline이 더 빠르다.
