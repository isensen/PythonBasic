#coding=utf-8

'''
   元类

'''

__author__ = "i3342th"



# 动态语言和静态语言最大的不同, 就是函数和类的定义,  不是编译时定义的,而是运行时创建的

# ----------------------------------type()-------------------------------------------------------
# 比如我们要定义一个 Hello 的class, 就写一个 hello.py 模块

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

# 当Python解释器载入 hello 模块时,就会依次执行该模块的所有语句,执行结果就是动态创建出一个Hello的class对象

# from hello import Hello

h = Hello()
h.hello()

print type(Hello)#<type 'type'>
print type(h)     #<class '__main__.Hello'> 如果是按模块导入的就会是 <class 'hello.Hello'>


# type() 函数可以查看一个类型或变量的类型, Hello是一个class,那么他的类型就是type
# h 是一个对象实例,那么它的类型就是 class  Hello

# 我们说  class 的定义是运行时动态创建的,而创建 class的方法就是使用 type()函数

# type() 函数既可以返回一个对象的类型, 又可以创建出新的类型,比如我们可以通过 type()函数创建出 Hello类
# 而无需要通过class Hello(object) 的定义

def fn(self, name = 'world'):
    print ('Hello, %s.' % name)

Hello2 = type('Hello', (object,), dict(hello = fn)) # 创建Hello class

h = Hello2()
h.hello()

# ------------其实就是动态创建类----------------

#要创建一个 class 对象, type() 函数依次传入3个参数:
# 1. class 的名称
# 2. 继承的父类集合, 注意Python支持多重继承,如果只有一个父类,别忘了tuple单元素的写法
# 3. class的方法名称与函数绑定, 这里我们把函数 fn 绑定到方法名 hello上

# type()函数允许我们动态的创建出类来,也就是说,动态语言本身支持运行期动态创建类
# 这和静态语言有非常大的不同, 要在静态语言运行期创建类, 必须构造 源代码字符串, 再调用编译器
# 或借助一些工具生成字节码实现, 本质上都是动态编译,会非常复杂


# -----------------------------------metaclass-----------------------------------------------
# 除了使用 type() 动态创建类以外, 要控制类的行为, 还可以使用 metaclass
# metaclass, 直译为  元类 , 简单解释就是
# 当我们定义了类以后,就可以根据这个类创建出实例,所以: 先定义类,然后创建实例
# 但是如果我们想创建出类呐?(不通过定义,直接创建), 那就必须根据 metaclass创建出类
# 所以先定义metaclass, 然后创建类, 定义metaclass -> 创建类 -> 创建实例

# metaclass 允许你创建类或修改类, 换句话说, 你可以把类看成是  metaclass 创建出来的实例
# metaclass 是 Python 面向对象里最难理,也是最难使用的魔术代码.
# 正常情况下, 你不会碰到需要使用 metaclass的情况.

# 其实可以理解为某些类的模板...指定这个模板的类,就有基于同一模板的方法神马的....

# 看个例子, 这个 metaclass 可以给我们自定义的 MyList 增加一个 add 方法
# 定义ListMetaclass , 按照默认习惯, metaclass 的类名总是以  Metaclass结尾


#metaclass是创建类,所以必须从type类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list): #继承自list
    __metaclass__ = ListMetaclass #指示使用ListMetaclass 来定制类


# 当我们写下  __metaclass__ = ListMetaclass 时, 魔术就生效了,安指示Python解释器在创建MyList时
# 要通过ListMetaclass.__new__()来创建, 在此,我们可以修改类的定义,比如加上新方法,然后返回修改后的定义

# __new__()接收的参数:
# 1. 当前准备创建的类的对象
# 2. 类的名字
# 3. 类继承的父类集合
# 4. 类的方法集合


#-------------------------------------- 教程中有一个简单ORM的例子,可以去学一下,加深印象------------------