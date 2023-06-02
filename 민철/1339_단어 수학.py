import sys 

N = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for i in range(N)]
alphabets = set([alphabet for word in words for alphabet in word])
counts = [[0] * 8 for _ in range(len(alphabets))]
answer = 0

alphabet_dict = {}
for alphabet, count in zip(alphabets,  counts):
    alphabet_dict[alphabet] = count

for word in words:
    for i, alphabet in enumerate(word[::-1]):
        alphabet_dict[alphabet][-i - 1] += 1

alphabet_dict = dict(sorted(alphabet_dict.items(), key=lambda item: item[1], reverse = True))

for i, alphabet in enumerate(alphabet_dict.keys()):
    alphabet_dict[alphabet] = 9 - i

for word in words:
    for i, alphabet in enumerate(word[::-1]):
        answer += alphabet_dict[alphabet] * 10 ** i
print(alphabet_dict)
print(answer)
