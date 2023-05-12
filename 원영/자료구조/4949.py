import sys

input = sys.stdin.readline
stories = list(input().rstrip().split("."))

while True :
    stories = input()
    stack = []

    if stories == ".": break

    for i in stories :
        if i == '[' or i == '(': stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop() # 있을 경우
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else :
                stack.append(')')
                break
                
    if len(stack) == 0: print('yes')
    else: print('no')

# story = stories[0]
# stack = []
# i = 0
# while i!=len(story)-1:
#     if story[i].isalpha(): i+=1
#     # elif story[i] =="(":
#     #     stack.append(story[i])
#     #     i+=1
#     # elif story[i]=="[":
#     #     stack.append(story[i])
#     #     i+=1
#     # elif story[i]==")":
#     #     if stack[-1]=="()"
#     else:
#         print(story[i])
#         i+=1

# print(stack)