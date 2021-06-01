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
PyCharm缩进，选中代码块按tab键或shift+tab键
批量注释或取消注释，选中代码按command+/键
"""

import string
import random
from datetime import datetime as dt


# https://docs.python.org/3/library/string.html
# https://docs.python.org/3/library/random.html
# 密码字符类型

# 不同等级密码字符组合列表
print("---------------\n"
      "Python 密码生成器\n"
      "---------------\n"
      "1）数字\n"
      "2）数字+小写字母\n"
      "3）数字+小写字母+大写字母\n"
      "4）数字+小写字母+大写字母+符号\n")

password_level = input("请选择密码复杂度等级:（建议为4）")
# 密码复杂度等级
if password_level == '1':
    level = string.digits
elif password_level == '2':
    level = string.digits + string.ascii_lowercase
elif password_level == '3':
    level = string.digits + string.ascii_lowercase + string.ascii_uppercase
elif password_level == '4':
    level = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
else:
    print("Error Input")
    exit()

length_input = int(input("请输入密码长度：（建议为12）"))
if length_input == '':
    length_input = 12

number_input = int(input("请输入生成数量："))
if number_input == '':
    number_input = 1

# 在指定字符组合中取随机字符，循环，直到满足密码长度要求，打印结果
password_list = []
while number_input > 0:
    length = length_input  # 额外增加第三变量，防止嵌套循环length_input > 0第二次值为False的情况
    pwd = ''
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

