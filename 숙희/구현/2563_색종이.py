array = [[0] * 100 for i in range(100)] # 2차원 배열 생성하기

count = int(input())
for _ in range(count):
    x, y = map(int,input().split())
    for i in range(10):
      for j in range(10):
        array[x+i][y+j] = 1

total = 0

for i in range(100):
  temp = array[i]
  total += sum(temp)

print(total)