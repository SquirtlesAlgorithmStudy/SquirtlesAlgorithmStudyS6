def 기준(x):
    return (x[1], x[0])


a = [(1, 4), (2, 4), (3, 1), (5, 3), (6, 4)]
b = sorted(a, key=lambda x: (x[1], x[0]))
print(b)
