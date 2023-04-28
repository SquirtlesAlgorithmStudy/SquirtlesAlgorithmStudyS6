s = input()  

stack = []  
word = ''  
tag = False  
for c in s:
    if c == '<':
        # 태그 시작
        stack.append(word[::-1])  # 이전 단어 뒤집어서 스택에 추가
        word = ''
        tag = True
        word += c  # 태그 문자열 추가
    elif c == '>':
        # 태그 끝
        tag = False
        word += c  # 태그 문자열 추가
        stack.append(word)  # 태그 스택에 추가
        word = ''
    elif c == ' ':
        # 단어 끝
        if tag:
            # 태그 안에 있는 공백 문자열인 경우 그대로 스택에 추가
            word += c
        else:
            # 일반적인 경우 단어 뒤집어서 스택에 추가
            stack.append(word[::-1])
            stack.append(c)  # 공백 스택에 추가
            word = ''
    else:
        # 단어 계속 진행
        word += c

# 마지막 단어 처리
if not tag:
    stack.append(word[::-1])
else:
    stack.append(word)

# 스택에서 문자열 하나씩 꺼내서 출력한다.
result = ''.join(stack)
print(result)
