#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:ZhouJinxin
@file: JustCounter.py
@time: 2019/05/{DAY}
"""
# 私有变量的访问方式
if __name__ == "__main__":
    pass

class JustCounter:
	__secretCount = 0  # 私有变量
	publicCount = 0    # 公开变量

	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量
counter._JustCounter__secretCount # 访问私有变量的正确方式