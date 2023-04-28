import sys
input = sys.stdin.readline

input_string = input().rstrip()

is_bracket_mode = False
splited_data = []
buffer = ""
for char in input_string:
    if char == '<':
        is_bracket_mode = True
        if len(buffer) > 0:
            splited_data.append(("non-bracket", buffer))
        buffer = '<'
    elif char == '>':
        is_bracket_mode = False
        buffer += '>'
        splited_data.append(("bracket", buffer))
        buffer = ""
    elif char == ' ':
        if is_bracket_mode:
            buffer += ' '
        else:
            splited_data.append(("non_bracket", buffer))
            buffer = ""
    else:
        buffer += char
if not is_bracket_mode:
    splited_data.append(("non-bracket", buffer))

result = ""
for idx, item in enumerate(splited_data):
    if item[0] == "bracket":
        result += item[1]
    else:
        if len(result) != 0 and result[-1] != '>':
            result += ' '
        string_list = list(item[1])
        string_list.reverse()
        result += ''.join(string_list)
# print(splited_data)
print(result)
