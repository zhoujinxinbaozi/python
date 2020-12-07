#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhoujinxin
@file: 函数.py
@time: 2019/04/{DAY}
"""
import time

if __name__ == "__main__":
    pass


def printMe(s):
    print(s)
    i = 0
    while i < 100000:
        i = i + 1


t1 = int(round(time.time() * 1000))
printMe("周金鑫")
print(int(round(time.time() * 1000)) - t1)
