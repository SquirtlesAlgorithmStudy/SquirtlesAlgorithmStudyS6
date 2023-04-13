S = input()
zero, one = 0, 0

while len(S) > 1:
    if S[0] == '0':
        S = S.lstrip('0')
        zero += 1
    elif S[0] == '1':
        S = S.lstrip('1')
        one += 1

print(min(zero, one))