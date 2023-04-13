N, M = map(int,input().split())

if N >= 3 and M >= 7:print(M-2)
elif N >= 3 and M < 5:print(M)
elif N == 2 and M < 7:print((M+1)//2)
elif N == 1:print(1)
else:print(4)