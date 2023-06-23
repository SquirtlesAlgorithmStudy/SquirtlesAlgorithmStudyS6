# import sys

# input = sys.stdin.readline

# N, M = map(int, input().split())

# A = [list(map(int,input().split())) for _ in range(N)]
# B = [list(map(int,input().split())) for _ in range(N)]

# for a, b in zipA, B:
#     print(a, b)
# print(A, B)
a = set([1, 2])
b = set([3, 4])



print(a, b)
print(a+b)
a.add(b)
print(a)