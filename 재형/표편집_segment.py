change_dict = {}
segment_tree = [0] * 3000000
leaf_start = 1

def initial_segment(n):
    for i in range(leaf_start, leaf_start+n+1):
        segment_tree[i]=1
    
    for i in range(leaf_start-1, 0, -1):
        segment_tree[i] = segment_tree[i*2] + segment_tree[i*2+1]
        
    return segment_tree

# tmp_node => node_start ~ node_end 까지 합 의미
# tmp_node => node_start ~ node_end 까지 합 의미
def get_segment_sum(tmp_node, node_start, node_end, target_start, target_end):
    # print(tmp_node, node_start, node_end, target_start, target_end)
    if target_start > target_end:
        target_start, target_end = target_end, target_start
    if node_end < target_start or target_end < node_start:
        return 0
    
    if target_start <= node_start and node_end <= target_end:
        return segment_tree[tmp_node]
    
    mid = node_start + (node_end - node_start)//2
    left_val = get_segment_sum(2*tmp_node, node_start,  mid, target_start, target_end)
    right_val = get_segment_sum(2*tmp_node+1, mid+1 ,node_end, target_start, target_end ) 
    return left_val + right_val


def segment_update(tree ,tmp_node, differ):
    while tmp_node != 0:
        tree[tmp_node] += differ
        tmp_node = tmp_node//2 
    
    return tree

# 현재 start~end 보고있고 
# target start 부터 target_end 까지 볼꺼임
# target 구간까지 합이 target_num 이 나오는 
# 합이 target_num이 되는 target_end최솟값을 구하는것이 목표임
def binary_search_down(start, end, target_start, target_num):
    mid = (start + end)//2
    tmp_sum = get_segment_sum(1, leaf_start, 2*leaf_start-1, target_start, mid)
    # print(tmp_sum, start, mid,end, target_num, target_start)
    if start == end:
        return end
        # 4          3
    if tmp_sum < target_num:
        return binary_search_down(mid+1, end,target_start, target_num)
    elif tmp_sum >= target_num:
        return binary_search_down(start, mid ,target_start, target_num)
    
# 이번에는 밑에서부터 위를 볼껀데
# target_start 가 밑에있으며
# 합이 target_num 이 되는 target_end 의 최댓값을 구할거임 
# start < end  
def binary_search_up(start, end, target_start, target_num):
    mid = (start + end)//2
    tmp_sum = get_segment_sum(1, leaf_start, 2*leaf_start-1, mid, target_start)
    
    # print(start, mid, end, tmp_sum, target_start, target_num)
    if start == end:
        return end
    # 위로 올려야 되는순간? -> 
    # 같아도 밑으로 내리기
    #    5         4
    if tmp_sum > target_num:
        return binary_search_up(mid+1, end,target_start, target_num)
    elif tmp_sum <= target_num:
        return binary_search_up(start, mid,target_start, target_num)
    
    

def solution(n, k, cmd):
    global leaf_start,segment_tree
    while 2**leaf_start < n:
        leaf_start += 1
    leaf_start = 2**leaf_start
    
    # 1. 세그먼트 트리 n 초기화
    segment_tree = initial_segment(n)
    delete_stack = []

    # 2. 하나씩 돌면서, 명령수행
    leaf_loc = k + leaf_start
    leaf_end = n + leaf_start - 1
    # print(leaf_loc)
    for tmp_order in cmd:
        order = tmp_order.split()[0]
        
        if order == "D":
            number = int(tmp_order.split()[1])
            leaf_loc = binary_search_down(leaf_loc, leaf_end, leaf_loc, number+1)
            # binary search 로 찾기
        elif order == "C":
            segment_tree = segment_update(segment_tree, leaf_loc, -1)
            delete_stack.append(leaf_loc)
            if leaf_loc == leaf_end:
                leaf_loc = binary_search_up(leaf_start, leaf_loc , leaf_loc, 1) 
            else:
                leaf_loc = binary_search_down(leaf_loc, leaf_end , leaf_loc, 1)
        elif order == "U":
            number = int(tmp_order.split()[1])
            leaf_loc = binary_search_up(leaf_start, leaf_loc, leaf_loc, number+1)
        elif order == "Z":
            add_idx = delete_stack.pop()
            segment_tree = segment_update(segment_tree, add_idx, 1)
        # print(segment_tree[1:16])
        # print(leaf_loc)
    answer = ''
    
    for idx in range(leaf_start, 2*leaf_start):
        if segment_tree[idx] ==0:
            answer+= 'X'
        elif segment_tree[idx] ==1:
            answer += 'O'
    
    return answer


print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))