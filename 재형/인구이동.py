
import sys
import copy
sys.setrecursionlimit(5000)

answer = 0
N, L, R = map(int, input().split())

family = [[0]*N for _ in range(N)]

ground = []
for row in range(N):
    ground.append(list(map(int, input().split())))

def find_family(row, col, num):
    family[row][col] = num
    
    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_row = row + dir[0]
        next_col = col + dir[1]
        if 0 <= next_row < N and 0 <= next_col < N:  
            if family[next_row][next_col] == 0:
                now_value  = ground[row][col]
                next_value = ground[next_row][next_col]
                differ = abs(now_value - next_value)
                if L <= differ <= R:
                    find_family(next_row, next_col, num)


def population_movement():
    global ground
    population_dict = {}
    count_dict = {}
    next_ground = copy.deepcopy(ground)
    is_move = False
    
    for i in range(N):
        for j in range(N):
            family_num = family[i][j]
            if family_num in population_dict:
                count_dict[family_num] += 1
                population_dict[family_num] += ground[i][j]
            else:
                count_dict[family_num] = 1
                population_dict[family_num] = ground[i][j]
    
    for i in range(N):
        for j in range(N):
            family_num = family[i][j]
            next_ground[i][j] = population_dict[family_num] // count_dict[family_num]
            if next_ground[i][j] != ground[i][j]:
                is_move = True
    
    ground = copy.deepcopy(next_ground)
    return is_move

while True:
    # 1. family 초기화
    for i in range(N):
        for j in range(N):
            family[i][j] = 0
    
    # 2. family 정의
    family_num = 1
    for row in range(N):
        for col in range(N):
            if family[row][col] == 0: 
                find_family(row, col, family_num)
                family_num += 1

    # 3. 인구이동 시작
    if not population_movement():
        break
    else:
        answer +=1


print(answer)




