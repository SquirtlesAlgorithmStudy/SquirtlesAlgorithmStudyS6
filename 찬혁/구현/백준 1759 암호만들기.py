from itertools import combinations

L,C = map(int,input().split())

alpa_li = list(input().split())
answer_li = []
vowel = ('a','e','i','o','u')

for data in combinations(alpa_li, L):
    condition = len(set(data+vowel))
    if condition == L+5 or condition < 7:
        continue

    answer_li.append(''.join(sorted(data)))

answer_li.sort()

for answer in answer_li:
    print(answer)