#coding=utf-8

'''

'''

__author__ = "i3342th"

class Student(object):
    pass

#定义了一个类后, 创建一个类的实例后,我们可以给该实例绑定任何属性和方法,这就是动态语言的灵活性
s = Student()
s.name = 'isensen' #动态绑定属性
print s.name

#可以尝试给对象绑定一个方法
def set_age(self,age):#定义一个函数作为实例方法
    self.age = age

#注意这只是给一个实例绑定了方法, 其他实例不具有此方法
from types import MethodType
s.set_age = MethodType(set_age, s , Student) #给一个实例绑定一个方法
s.set_age(25) #调用实例方法
print s.age


#为了给所有实例都绑定方法 , 可以给class 绑定方法 (这样灵活度就很高了,相当于动态给class绑定方法 )
def set_score (self, score):
    self.score = score

Student.set_score = MethodType(set_score, None, Student)#指定实例参数为None

#---------------------------------使用__slots__-----------------------------

#如果我们想要限制class的属性怎么办? 比如,只允许对Student实例添加 name 和 age 属性
#为了达到限制的目的, Python允许在定义class的时候,定义一个特殊的__slots__变量,来限制该class能添加的属性
#注意: __slots__定义的属性仅对当前类起作用, 对继承的子类是不起作用的
#除非在子类中也定义 __slots__,这样,子类允许定义的属性就是自身的__slots__加上父类的 __slots__
class Student(object):
    __slots__ = ('name','age') #用Tuple 定义允许绑定的属性名称

s = Student()
s.name = 'isensen'
s.age = 29
s.score = 100 #AttributeError: 'Student' object has no attribute 'score'





