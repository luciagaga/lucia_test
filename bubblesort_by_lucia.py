array = [4, 72, 56, 209, 0, -3, 0.9]

length = len(array)
print('The length of the array = ', length)

for j in range(length - 1, -1, -1):
    # print('j = ', j)
    for i in range(j):
        # print(i)
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

print('The result of the bubble sort is:', array)


