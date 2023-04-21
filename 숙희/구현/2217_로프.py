count = int(input())
x = []
for _ in range(count):
    temp = int(input())
    x.append(temp)

x.sort()

can = []
for i in range(len(x)):
    temp2 = x[i] * (count - i)
    can.append(temp2)

print(max(can))    