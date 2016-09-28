# -*-coding:utf-8 -*-


array = u'永远相信美好的事即将发生'
print(len(array))
a = ''
for i in range(len(array) - 2, -1, -1):
    a += array[i]

print("{0}{1}".format(''.join(array), a))



