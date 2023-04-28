import sys
import copy

input = sys.stdin.readline
n,m,b = map(int,input().rstrip().split()) # 세로, 가로, 인벤토리 입력
house = [list(map(int,input().rstrip().split())) for _ in range(n)] # 블럭 입력
house = sum(house,[]) # 2차원 배열을 1차원으로 변환

num = (max(house)+min(house))//2 # 최소값과 최대값의 평균
times = 256*500*500*2 # 최대 시간
height = num+1 # 최대 높이

for top in range(num, num+2): # 가능한 높이 : 평균의 최소값과 최대값
    cnt = 0 # 진행 시간
    inven = copy.copy(b) # 인벤토리 현황
    for i in range(n*m): # 블록 전체 순환
        dif = top-house[i]
        if house[i]<top: # 높이보다 작은 경우
            if dif>inven: # 높이와의 차이만큼 인벤토리에 없다면 통과
                cnt = copy.copy(times) # 진행시간 복구
                continue
            else:
                cnt += dif # 진행시간
                inven -= dif # 인벤토리에서 제거
        elif house[i]>top: # 높이보다 큰 경우
            cnt += (-dif)*2 # 진행시간 추가
            inven += (-dif) # 인벤토리에 저장
    
    if cnt<times: # 진행시간이 더 짧다면
        times = cnt
        height = top
print(times, height)