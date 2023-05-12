from collections import deque

def last_remaincard(N):
    # 큐 초기화
    cards = deque(range(1, N + 1))

    while len(cards) > 1:
        # 가장 위에 있는 카드 제거
        cards.popleft()

        # 그 다음으로 가장 위에 있는 카드를 큐의 맨 뒤로 옮김
        cards.append(cards.popleft())

    # 마지막에 남는 카드 반환
    return cards[0]

# N 입력
N = int(input())

# 마지막에 남는 카드 계산
result = last_remaincard(N)

# 결과 출력
print(result)
