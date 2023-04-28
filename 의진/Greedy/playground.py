import sys
from operator import sub
input = sys.stdin.readline
list1 = [[3, 3, 3], [1, 1, 1]]
list2 = [[1, 1, 1], [2, 2, 2]]
result = list(map(sub, list1, list2))
print(result)
