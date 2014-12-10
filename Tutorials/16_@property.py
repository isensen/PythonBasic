#coding=utf-8

'''

'''

__author__ = "i3342th"

class Student(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age

#绑定属性时,如果我们直接把属性暴露出去,虽然写起来简单,但是造成了没法检查参数的正确性,导致可以随意修改
s = Student('isensen',100)
s.age = 10000

# 上面设置的年龄10000 显然是不对的, 为了限制age的范围,可以通过一个 set_age()方法来设置年龄
# 再通过一个get_age()方法来获取年龄

class Student(object):
    def __init__(self,name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if not isinstance(value,int):
            raise ValueError('age must be integer!')
        elif value < 0 or value >100:
            raise ValueError('age must between 0 ~ 100!')
        else:
            self.__age = value

s = Student('isensen',100)
#s.set_age(1000) # 报错 ValueError: age must between 0 ~ 100!


# 但是上面的调用方法感觉是不是有点复杂, 没有直接调用那么方便
# 有没有既能检查参数, 又可以用类似属性这样简单的方法来访问类的变量呢?
# 还记得 Decorator 装饰器 可以给函数动态加上功能吗? 对于类的方法 ,装饰器一样起作用
# Python内置的 @property 装饰器就是负责把一个方法变成属性调用的

class Student(object):

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value,int):
            raise ValueError('age must be integer!')
        elif value < 0 or value >100:
            raise ValueError('age must between 0 ~ 100!')
        else:
            self.__age = value

# property 的实现较复杂 ,我们先学会如何使用, 把一个getter方法 变成属性,只需要加上 @property 就可以了
# @property本身又创建了另一个装饰器 @age.setter, 负责把一个setter方法变成属性赋值
# 只定义@property 不定义 @xxx.setter的话,就是一个只读属性

s = Student()
s.age = 10000 #报错
