import sys

penny = [500, 100, 50, 10, 5, 1]
money = int(sys.stdin.readline())
change = 1000 - money
idx,answer = 0,0

while change > 0 or idx < len(penny):
    if penny[idx] <= change:
        change -= penny[idx]
        answer += 1
    else:
        idx += 1
print(answer)

#change(거스름돈)에서 가지고 있는 잔돈(penny)를 큰 수부터 차례로 감소시키며 count