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
"""

import string
import random


# 密码字符类型
numbers = [i for i in string.digits]  # 依次将0-9放入列表
lowercase_letters = [j for j in string.ascii_lowercase]  # 依次将a-z放入列表
uppercase_letters = [m for m in string.ascii_uppercase]  # 依次将A-A放入列表
symbols = [n for n in string.punctuation]  # 依次将符号放入列表


# 密码复杂度等级
level1 = numbers
level2 = numbers + lowercase_letters
level3 = numbers + lowercase_letters + uppercase_letters
level4 = numbers + lowercase_letters + uppercase_letters + symbols

print("Numbers include: \n", numbers)
print("Lowercase Letters include: \n", lowercase_letters)
print("Uppercase Letters include: \n", uppercase_letters)
print("Symbols include: \n", symbols)

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


def password_generator(level_n, length=12):

    output = []
    while length > 0:
        output.append(level[random.randrange(0, len(level))])
        length = length - 1
        if length < 1:
            break
    print(output)


password_generator()
