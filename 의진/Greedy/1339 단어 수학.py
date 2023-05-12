import sys
input = sys.stdin.readline

N = int(input())
operands = [input().rstrip() for _ in range(N)]


def get_priority(operands):
    result = {}
    for operand in operands:
        for idx, char in enumerate(operand[::-1]):
            if char in result:
                result[char] += (10 ** idx)
            else:
                result[char] = (10 ** idx)
    result = list(
        map(list, sorted(result.items(), key=lambda x: x[1], reverse=True)))
    for idx, i in enumerate(range(9, 9 - len(result), -1)):
        result[idx][1] = i
    return dict(result)


def calculate_value(operands, result):
    number_operands = []
    for operand in operands:
        number_operand = 0
        for idx, char in enumerate(operand[::-1]):
            number_operand += (result[char] * (10 ** idx))
        number_operands.append(number_operand)
    return sum(number_operands)


result = get_priority(operands)
print(calculate_value(operands, result))
