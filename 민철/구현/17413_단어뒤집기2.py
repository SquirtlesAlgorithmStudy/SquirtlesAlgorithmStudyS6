import sys

S = sys.stdin.readline().rstrip()
answer = ''
in_tag = 0
stack = []

for s in S:
    if in_tag:
        answer += s
        if s == '>':
            in_tag = 0
    else:
        if s == '<' or s == ' ':
            while stack:
                answer += stack.pop()
            answer += s
            if s == '<':
                in_tag = 1
        else:
            stack.append(s)
        
while stack:
    answer += stack.pop()

print(answer)
    

