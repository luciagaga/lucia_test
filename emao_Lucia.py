# -*- coding=utf8 -*-

import re  # 引用正则包

html = 'http://www.baidu.com'  # 设置待测地址
emao = '[a-z]'  # 设置正则
find_emao = re.search(emao, html)  # 使用re.search调用正则去待测地址中找到是否能找到结果
if not find_emao:
    print('未找到')
else:
    print('找到')
