import sys

input = sys.stdin.readline

open_bracket = ['(','[']
close_bracket = [')',']']

def brakcket_stack(s):
    stack = []
    for data in s: 
        if data not in open_bracket+close_bracket:
            continue
        
        if data in open_bracket:
            stack.append(data)

        else:
            if len(stack) == 0:
                return False

            elif stack[-1] == open_bracket[0] and data == close_bracket[0]:
                stack.pop()

            elif stack[-1] == open_bracket[1] and data == close_bracket[1]:
                stack.pop()
            
            else:
                return False
            
    if len(stack) > 0:
        return False
    else:
        return True

while True:
    s = input().rstrip()
    if s == '.':
        break

    if brakcket_stack(s) == True:
        print("yes")
    else:
        print("no")