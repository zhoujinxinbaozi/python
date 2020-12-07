#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhoujinxin
@file: 模块.py
@time: 2019/04/{DAY}
"""
if __name__ == "__main__":
    pass

Money = 2000


def AddMoney():
    # 对全局变量的修改
    global Money
    Money = Money + 1


print(Money)
AddMoney()
print(Money)