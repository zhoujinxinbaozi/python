#!usr/bin/env python
# -*- coding:utf-8 _*-

import time

"""
@author:zhoujinxin
@file: 日期和时间.py
@time: 2019/04/{DAY}
"""
if __name__ == "__main__":
    pass

print(time.strftime("%Y%m%d%H%M%S", time.localtime()))
print(time.strftime("%Y%m%d", time.localtime()))

