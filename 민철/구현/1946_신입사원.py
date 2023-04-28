import sys

cases = int(sys.stdin.readline())
answers = []

for case in range(cases):
    answer = 0
    cands = int(sys.stdin.readline())
    ranks = []
    for cand in range(cands):
        rank1, rank2 = map(int, sys.stdin.readline().split())
        ranks.append((rank1, rank2))
    ranks.sort(key = lambda x: x[0])

    min = ranks[0][1]
    answer += 1
    
    for i in range(1, cands):
        if ranks[i][1] < min:
            min = ranks[i][1]
            answer += 1
    answers.append(answer)

[print(answer) for answer in answers]
