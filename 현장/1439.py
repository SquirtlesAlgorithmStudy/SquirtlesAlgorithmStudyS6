import sys

# N = list(map(str,sys.stdin.readline().split()))
N = sys.stdin.readline()

if __name__ == "__main__":
    
    s = N[0:-1]
    size = len(s)

    zeros, ones = 0, 0
    for i in range(size-1):
        if s[i] != s[i+1] and s[i] == "0":
            zeros += 1
        elif s[i] != s[i+1] and s[i] == "1":
            ones += 1
    
    print(min(zeros, ones))



