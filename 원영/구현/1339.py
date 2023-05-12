import sys

input = sys.stdin.readline

n = int(input())
alphas = []
dictionary = {}
START = 9

for _ in range(n):
  alphas.append(input().rstrip())
alphas.sort(key=lambda x : len(x),reverse=True)
alpha = sum([list(x) for x in alphas],[])

from collections import Counter

cnt = Counter(alpha).most_common()
for c in cnt:
  dictionary[c[0]]= START
  START -= 1


# 구현
# 단어 출현 빈도수와 위치 중에 어떤걸 우선으로 생각해야할지 모르겠음.