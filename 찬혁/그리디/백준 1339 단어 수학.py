import sys

input = sys.stdin.readline

n = int(input())
answer = 0
alpa_dic = {}

alpa_list = [input().rstrip()[::-1] for _ in range(n)]

for al in alpa_list:
    for idx, data in enumerate(al):
        if data in alpa_dic.keys():
            alpa_dic[data] += 10**idx
        else:
            alpa_dic[data] = 10**idx

num = 9
for i in sorted(list(alpa_dic.values()),reverse=True):
    answer += i*num
    num -= 1

print(answer)
