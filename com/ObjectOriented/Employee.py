#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:ZhouJinxin
@file: Employee.py
@time: 2019/05/{DAY}
"""
if __name__ == "__main__":
    pass


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary, x=0, y=0):
        self.name = name
        self.salary = salary
        self.x = x
        self.y = y
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("name is %s, salary is %d, x is %d, y is %d" % (self.name, self.salary, self.x, self.y))

# # 创建 Employee 类的第一个对象
# emp1 = Employee("Zara", 2000, 1, 2)
# # 创建 Employee 类的第二个对象
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)
# # 相当于get和set方法
# setattr(emp1, "name", "zhoujinxin")
# print(getattr(emp1, "name"), ", ", getattr(emp1, "salary"))
