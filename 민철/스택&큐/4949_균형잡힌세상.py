import sys

while True:
    S = sys.stdin.readline().rstrip()

    if S == '.':
        break

    answer = 'yes'
    stack = []
    for s in S:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')' or s == ']':
            if not stack:
                answer = 'no'
                break
            bracket = stack.pop()
            if s == ')':
                if bracket != '(':
                    answer = 'no'
                    break
            else:
                if bracket != '[':
                    answer = 'no'
                    break
    if stack:
        answer = 'no'                
    print(answer)