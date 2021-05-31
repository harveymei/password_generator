#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/31 09:46
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: pwdgen.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
Python 密码生成器
Python Password Generator
指定长度和复杂度的密码批量生成工具
用户录入作为参数，传入函数，生成密码
PyCharm缩进，选中代码块按tab键或shift+tab键
"""

import string
import random
from datetime import datetime as dt

# 密码字符类型
# https://docs.python.org/3/library/string.html
level_1 = string.digits
level_2 = level_1 + string.ascii_lowercase
level_3 = level_2 + string.ascii_uppercase
level_4 = level_3 + string.punctuation


# 不同等级密码字符组合列表
print("Python 密码生成器\n"
      "1）数字\n"
      "2）数字+小写字母\n"
      "3）数字+小写字母+大写字母\n"
      "4）数字+小写字母+大写字母+符号\n")

level_input = input("请选择密码复杂度等级:（默认为4）")
# 密码复杂度等级
if level_input == '1':
    level = level_1
elif level_input == '2':
    level = level_2
elif level_input == '3':
    level = level_3
elif level_input == '4':
    level = level_4
else:
    print("Error Input")
    exit()

length_input = int(input("请输入密码长度：（默认为12）"))
if length_input == '':
    length_input = 12

number_input = int(input("请输入生成数量：（默认为1）"))
if number_input == '':
    number_input = 1

# 在指定字符组合中取随机字符，循环，直到满足密码长度要求，打印结果
password_list = []
while number_input > 0:
    pwd = ''
    length = length_input  # 额外增加第三变量，防止嵌套循环第二次条件为length_input > 0值为False的情况
    while length > 0:  # 循环指定次数拼接字符串
        pwd = pwd + level[random.randrange(0, len(level))]
        length = length - 1
    password_list.append(pwd)
    number_input = number_input - 1

# print(pwd_list)
filename = dt.now().strftime("%Y%m%d%H%M%S") + ".txt"
with open(filename, 'wt') as f:
    for password in password_list:
        f.write(password + "\n")
