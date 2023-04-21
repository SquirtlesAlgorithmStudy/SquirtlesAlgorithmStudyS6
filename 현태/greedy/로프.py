n = int(input())
ropes = []
for i in range(n):
    ropes.append(int(input()))
ropes.sort(reverse=True)

max_weight = 0
for i in range(n):
    weight = ropes[i] * (i + 1)
    if weight > max_weight:
        max_weight = weight

print(max_weight)
