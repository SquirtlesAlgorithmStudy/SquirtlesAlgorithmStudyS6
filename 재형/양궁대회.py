import copy

possible_infos = []

def score_compare(lion_scores, apachi_scores):
    lion_ret = 0
    apachi_ret = 0
    for idx in range(11):
        if lion_scores[idx] == 0 and apachi_scores[idx] == 0:
            continue
        elif lion_scores[idx] <= apachi_scores[idx]:
            apachi_ret += (10 - idx)
        else:
            lion_ret += (10-idx)

    if lion_ret <= apachi_ret:
        return -1
    else:
        return lion_ret - apachi_ret

def backtracking_product(spare_num, tmp_idx, tmp_array, apachi_info):
    if tmp_idx == 11:
        if spare_num > 0:
            tmp_array[-1] = tmp_array[-1] + spare_num
        possible_infos.append(tmp_array)
        return
    
    my_array = copy.deepcopy(tmp_array)
    if len(tmp_array) < tmp_idx+1:
        my_array.append(0)
    
    next_array = copy.deepcopy(my_array)
    # 1. 그냥 건너뜀
    backtracking_product(spare_num, tmp_idx+1, next_array, apachi_info)
    
    if spare_num > apachi_info[tmp_idx] and spare_num > 0:
        next_2_array = copy.deepcopy(next_array)
        next_2_array[tmp_idx] = apachi_info[tmp_idx] + 1
        # 2. 아파치 idx에 1추가하고 다음꺼넘어감
        backtracking_product(
            spare_num-(apachi_info[tmp_idx] + 1), tmp_idx, next_2_array, apachi_info
        )

    
def solution(n, info):
    global possible_infos
    now_big_score = 0
    backtracking_product(n ,0 ,[], info)
    
    answer = []
    
    possible_infos = sorted(possible_infos, key=lambda x: x[::-1], reverse=True)

    for possible_info in possible_infos:
        score = score_compare(possible_info ,info)
        # 처음에 나온놈이 장땡
        if score != -1 and score > now_big_score:
            answer = possible_info
            now_big_score = score
            
    if len(answer) == 0:
        answer = [-1]

    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))