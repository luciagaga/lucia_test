from pip.backwardcompat import raw_input

print("请想好一个0到100中间的数字~~~")

hi = 100
lo = 0
guessed = False
guess = 0

while not guessed:
    guess = int((hi + lo) / 2)
    print("你想的数字是 " + str(guess) + "吗?")

    user_inp = raw_input("如果高了请输入字母h~~~如果低了请输入字母l~~~如果是你想的数字请输入字母c~~~")

    if user_inp == 'c':
        guessed = True
    elif user_inp == 'h':
        hi = guess
    elif user_inp == 'l':
        lo = guess
    else:
        print("你输入的内容我不懂...")
print('游戏结束~~~你想好的数字是: ' + str(guess))
