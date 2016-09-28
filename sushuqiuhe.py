sum_no = 0
i = 2
while i < 12:
    print('i = ', i)
    sum_no = sum_no + i
    for j in range(1, i + 1):
        if i % j == 0:  # 若能够除尽 则不是素数
            i += 1
print('sum =', sum_no)
