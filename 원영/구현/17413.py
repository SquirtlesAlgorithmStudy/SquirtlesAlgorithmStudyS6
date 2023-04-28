import sys

strings = sys.stdin.readline().rstrip()
tag = False # 뒤집어진 경우
reverse=''
stack = ''

for s in strings:
    if tag==False:# 뒤집어진 경우
        if s=='<': # 태그가 시작된 경우
            tag=True
            stack += s
        elif s==' ': # 공백의 경우
            stack += s
            reverse += stack
            stack=''
        else: stack = s+stack
    elif tag == True: # 정상 출력
        stack+= s
        if s=='>': # 태그가 닫힌 경우
            tag=False
            reverse += stack
            stack=''
print(reverse+stack)