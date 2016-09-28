matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

trans = []
for i in range(4):
    trans.append([row[i] for row in matrix])

print(trans)
