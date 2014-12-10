#coding=utf-8

'''
    类

'''

__author__ = "i3342th"

class Student:
    pass

class Student(object):  # object 表示类是从哪个类继续过来的,如果没有合适的继续类,就用object
    pass

s1 = Student()     # 生成一个实例


print s1          #<__main__.Student object at 0x00BBC4D0>  0x00BBC4D0是内存地址
print Student     #<class '__main__.Student'>


s1.test = 'test'  # 可以自由的给他绑定属性,类似动态属性之类的
print s1.test


#类可以起到模板的作用, 因此可以在创建类实例时,把一些我们认为必须绑定的属性强制填进去,
#通过定义一个特殊的方法  __init__ 方法,在创建实例的时候,就把name, score等属性绑上去
# __init__ 方法的参数永远是 self , 表示创建实例的本身
# 有了__init__方法 ,在创建实例时,就不能传入空参数了,其实就相当于其他语言的 构造方法
# 必须传入 和 __init__ 相匹配的参数,self不用传,Python 解释器会自动传
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score



s2 = Student('isensen','100')
print s2.name

# 和普通的函数相比,在类中定义的函数只有一点不同
# 就是第一个参数永远是实例变量  self ,
# 并且调用时,不用传递参数. 除此之外,类的方法 和普通函数没有什么区别
# 所以仍然可以用默认参数, 可变参数, 和关键字参数


#数据封装
#上面的实例中,每个实例都有 name 和 score 这些数据,我们可以通过函数方便的访问这些数据

def print_score( std):
    print '%s %s' % (std.name, std.score)

print_score(s2)

# 像上面这样从外部访问没必要,直接从内部定义方法就好了
# 这样就实现了 数据和方法  的  封装
# 记住两点和以前认识不同的:
#   1. 可以自由绑定数据类型,不用像以前一样写参数为  Student std
#      def print_score( std):
#             print '%s %s' % (std.name, std.score)
#  2. 其实2 和1差不多,一个实例生成 后,还可以随便 动态的给他绑定属性
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_scrore(self):
        print '%s %s' % (self.name, self.score)

s2 = Student('isensen', 100)
s2.print_scrore()

#############################################访问限制##############################################


#以上声明的Student里的name 和  score , 外部还是可以访问或修改,如果想只能内部访问,外部不能访问
#这个不只是规范了,是外部真正访问不到
# PS: 其实也可以,就是Python解释器那它改名了 __Student__name
# Python不阻止你干坏事,靠自觉

class Student(object):
    def __init__(self, name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s %s' % (self.__name, self.__score)

s1 = Student('isensen', 101)
#print s1.__name #AttributeError: 'Student' object has no attribute '__name'

#这样外部就不能随便修改了,增强了代码的健壮性,如果外部要读取怎么办
#这样类就只能读取了,如果外部要修改怎么办,再增加 set,这个都是基础了.不多说了
#这样就比较灵活了,之前是外部能随便访问 ,修改 s1.name s1.name='aaa'
# 现在可以控制 访问 权限,设置权限,还可以在set方法里,对所赋值进行控制

class Student(object):
    def __init__(self, name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    @classmethod
    def test_class_method(cls):
        print 'class method'
      # print self.score   这是类方法 ,实例虽然 可以调,但设计目的不是实例去调,并且里面引用不了实例

Student.test_class_method();
Student('isensen',100).test_class_method();
#-----------------------------------区别   类方法  和 实例方法 ----------------------------------
#-----------------------------------区别   类属性  和 实例属性 ----------------------------------

class Student(object):
    name = 'Student' #这就是类属性

#实例属性必须通过实例来绑定,比如  self.name = 'isensen'

s = Student()
print s.name # 打印s.name,因为上面定义中没有定义 self.name 属性,所以会继续查找类属性,找到 'Student'
# 输出  'Student'

print Student.name #输出 Student

s.name = 'isensen'
print s.name # isensen
print Student.name


del s.name
print s.name #Student