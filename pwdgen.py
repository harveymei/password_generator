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
"""

import string
import random


# 密码字符类型
# https://docs.python.org/3/library/string.html
numbers = [i for i in string.digits]  # 依次将数字放入列表
lowercase_letters = [j for j in string.ascii_lowercase]  # 依次将小写字母放入列表
uppercase_letters = [m for m in string.ascii_uppercase]  # 依次将大写字母放入列表
symbols = [n for n in string.punctuation]  # 依次将符号放入列表

# 不同等级密码字符组合列表
level1 = numbers
level2 = numbers + lowercase_letters
level3 = numbers + lowercase_letters + uppercase_letters
level4 = numbers + lowercase_letters + uppercase_letters + symbols

print("1）数字\n"
      "2）数字+小写字母\n"
      "3）数字+小写字母+大写字母\n"
      "4）数字+小写字母+大写字母+符号\n")

level_input = input("请选择密码复杂度等级:（默认为4）")
# 密码复杂度等级
if level_input == '1':
    level = level1
elif level_input == '2':
    level = level2
elif level_input == '3':
    level = level3
elif level_input == '4' or '':
    level = level4
else:
    print("Error Input")
    exit()


length_input = input("请输入密码长度：（默认为12）")
if level_input == '':
    length_input = 12

# 在指定字符组合中取随机字符，循环，直到满足密码长度要求，打印结果

# 返回对象长度
# print(len(level1))
# print(len(level2))
# print(len(level3))
# print(len(level4))

# 随机数作为列表索引值，取列表元素
print(level1[random.randrange(0, len(level1))])
print(level2[random.randrange(0, len(level2))])
print(level3[random.randrange(0, len(level3))])
print(level4[random.randrange(0, len(level4))])

level_n = ['level1', 'level2', 'level3', 'level4']


def password_generator(level=4, length=12):

    output = []
    while length > 0:
        output.append(level[random.randrange(0, len(level))])
        length = length - 1
        if length < 1:
            break
    print(output)


password_generator()

