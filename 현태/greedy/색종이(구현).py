import sys


input = sys.stdin.readline
n = int(input())

p = [list(map(int,input().split())) for _ in range(n)]
p.sort() # 앞의 값 기준으로 정렬


x, y = p[0]  
area = 0

 
for i in range(1, n):
    
# 뭔가 겹치지 않는 부분은 더해야 겠다는 생각은 하여 위의 반복문을 쓰려고 했는데 
# 아무리 생각해도 코드는 어떻게 작성해야되는지 모르겠습니다.

