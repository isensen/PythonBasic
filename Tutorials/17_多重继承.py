#coding=utf-8

'''
    多重继承
    class Dog(Mammal, Runnable):
        pass
'''


__author__ = "i3342th"


class Animal(object):
    pass



# 大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass



# 各种动物
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


# 现在我们要给动物再加上 Runnable 和 Flyable 功能, 只需先定义好 Runnable 和 Flyable 类
class Runnable(object):
    def run(self):
        print 'Running...'

class Flyable(object):
    def fly(self):
        print 'Flying...'


#对于需要Runnable 的动物就多继承一个Runnable

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass



# -------------------------------------------------Mixin-------------------------------------------------
# 在设计类的继续关系时,通常,主线都是单一继承下来的
# 如 Ostrich 继承自 Bird. 但是,如果需要"混入"额外的功能,通过多重继承就可以实现
# 比如让 Ostrich 除了 继承 Bird外,再同时继续 Runnable,这样设计通常称为  Mixin

# 为了更好的看出继续关系, 我们把 Runnable 和 Flyable 改为 RunnableMixin 和 FlyableMixin
#  个人感觉像JAVA里的接口,做个区分而已,只不过这样设计的时候,语言本身会更简单


# Mixin 的目的就是给一个类增加多个功能, 这样在设计类的时候,我们优先考虑通过多重继承来组合多个Mixin的功能
# 而不是设计多层次的继承关系

# Python自带的很多库也使用了Mixin
# Python自带了 TCPServer 和UDPServer 这两类网络服务,而要同时服务多个用户就必须使用多进程或多线程模型
# 这两种模型由 ForkingMixin 和 ThreadMixin 提供,通过组合,我们可以创造出合适的服务来

# 比如编写 一个多进程模式的TCP服务

# from SocketServer import TCPServer
# class MyTCPServer(TCPServer, ForkingMixin):
#     pass