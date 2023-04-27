'''
n = int(input())
location = list(map(int,input().split()))
location.sort()

start = location[0]
end = location[n-1]
all_distance = []
temp_distance = 0

for i in range(start,end+1):
  for distance in location[1:]:
    temp_distance += abs(i-distance)
  all_distance.append(temp_distance)
  temp_distance = 0

min_distance = min(all_distance)

print(all_distance.index(min_distance)-1)
'''
# 중앙값 찾기
n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1) // 2])