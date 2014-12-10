#coding=utf-8

'''
    继承和多态

    继承最大的好处就是获得了父类的全部功能
    子类和父类存在相同方法时,子类的方法会覆父类的方法,在代码运行时,总是会调用子类的同名方法 ,这样我们就获得了
    继承的另一个好处: 多态

    有了继承才能有多态
'''

__author__ = "i3342th"

#基类
class Animal(object):
    def run(self):
        print 'Animal is running...'

#继承
class Dog(Animal):
    pass

class Cat(Animal):
    pass


#扩展方法
class Dog(Animal):
    def fun(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'


#多态
def run_twice(animal):
    animal.run()
