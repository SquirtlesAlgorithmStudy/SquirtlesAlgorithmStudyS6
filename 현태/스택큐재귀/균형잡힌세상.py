def balance_string(s):
    stack = []

    for char in s:
        if char in "([":  # 왼쪽 괄호일 경우
            stack.append(char)
        elif char in ")]":  # 오른쪽 괄호일 경우
            if not stack or not matching_pair(stack.pop(), char):
                return "no"

    return "yes" if not stack else "no"

def matching_pair(left, right):
    pairs = {
        "(": ")",
        "[": "]"
    }
    return pairs[left] == right

# 입력 처리 및 결과 출력
while True:
    s = input()
    if s == ".":
        break
    result = balance_string(s)
    print(result)