while True :
  sentence = input()
  if sentence == '.' :
    break

  stack = []
  result = True

  for temp in sentence :
    if temp == '(' or temp == '[' :
      stack.append(temp)

    elif temp == ')' :
      if len(stack) == 0 or stack[-1] == '[' :
        result = False
        break
      elif stack[-1] == '(' :
        stack.pop()

    elif temp == ']' :
      if len(stack) == 0 or stack[-1] == '(' :
        result = False
        break
      elif stack[-1] == '[' :
        stack.pop()

  if len(stack) == 0 and result == True :
    print('yes')
  else :
    print('no') 