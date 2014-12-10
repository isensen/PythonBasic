#coding=utf-8

'''
    看到类似   __slots__ 这种形如 __xxx__的变量或者函数名,就要注意,这些在Python中有特殊用途的.
    __slots__我们已经知道怎么用了, __len__()方法 ,我们也知道为了让能class作用于len()函数
    除此之外,Python中的class中还有许多这样有特殊用途的函数,可以帮助我们定制类.
'''

__author__ = "i3342th"



#----------------__str__----------------------------------------------

#我们先定义一个Student类,打印一个实例:
class Student(object):
    def __init__(self, name):
        self.name = name

print Student('isensen') #<__main__.Student object at 0x00BBC4F0>  这里是内存地址

#要打印好看,只需要定义好 __str__()方法

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

print Student('isensen') #Student object (name: isensen)
s = Student('isensen')

# >>> s 如果这样在控制台输出变量,会发现还是不好看
# 因为直接显示变量调用的不是 __str__(),而是 __repr__(),
# 两者的区别是  __str__()返回用户看到的字符串,而 __repr__()返回程序开发者看到的字符串
# 也就是说 __repr__()是为调试服务的

#解决办法是再定义一个  __repr__(),但是通常 __str__() 和  __repr__()代码都是一样的,所以有个偷懒的写法:

class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__


#----------------------------__iter__----------------------------------------------------

#如果一个类想被用于 for...in 循环, 类似  list  或 tuple 那样,就必须实现一个 __iter__()方法,
#该方法返回一个迭代对象,然后Python的for循环就会不断调用该迭代对象的next()方法 拿到循环的下一个值
#直接遇到StopIteration 错误时退出循环

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器 a,b

    def __iter__(self):
        return self #实例本身就是迭代对象,所以返回自己

    def next(self):
        self.a, self.b = self.b, self.a +self.b #计算下一个值
        if self.a > 1000:
            raise StopIteration();
        return self.a #返回下一个值

a = Fib()
for n in a:
    print n

# -------------------------__getitem__--------------------------------------------------
# Fib实例虽然能作用于for循环, 看起来和list有点像,但是把它当做list来用还是不行, 比如要取第5个元素

#Fib()[5] #TypeError: 'Fib' object does not support indexing

#要表现的像 list 那样,按照下标取出元素, 需要实现 __getitem__()方法:

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器 a,b

    def __iter__(self):
        return self #实例本身就是迭代对象,所以返回自己

    def next(self):
        self.a, self.b = self.b, self.a +self.b #计算下一个值
        if self.a > 1000:
            raise StopIteration();
        return self.a #返回下一个值

    def __getitem__(self, item):
        a, b  = 1,1
        for x in range(item):
            a,b = b, a+b

        return a

print Fib()[5]
print Fib()[100]


#但是 list 有个神奇的切片方法:
print range(100)[5:10]

# 对于 Fib()却报错, 原因是  __getitem__() 传入的参数可能是一个int, 也可能是一个切片对象 slice,要做判断

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a , b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L=[]
            for x in range(stop + 1):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# 但是做的例子还没有对 step 作处理 [:2:10] , 就是步进值
# 所以要正确实现一个 __getitem__() 要有很多工作去做

#此外,如果要把对象看到 dict , __getitem__() 的参数也可能是一个可以做为key的object,例如 str
#与之对应的就是  __setitem__()  , 还有一个 __delitem__()方法
# 我们自己定义的类表现和 Python自带的list, tuple, dict 没有什么区别
# 这完全归功于动态语言的 "鸭子类型",不需要强制继承某个接口


#-------------------------------------__getattr__--------------------------------------

#正常情况下,当我们调用 类的方法或属性时,如果不存在,就会报错,比如定义 Student 类

class Student(object):
    def __init__(self):
        self.name = 'isensen'

#调用 name 属性,没有问题,但是调用 不存在的 score属性,就会有问题了

s = Student()
print s.name
# print s.score #AttributeError: 'Student' object has no attribute 'score'

# 要避免这个错误, 除了可以加上一个score属性外, Python还有另一个机制,那就是写一个 __getattr__()方法
# 动态返回一个属性,修改如下:

class Student(object):
    def __init__(self):
        self.name = 'isensen'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99


s = Student()
print s.score

# 如果要返回一个函数 ,也完全是可以的

class Student(object):
    def __init__(self):
        self.name = 'isensen'
    def __getattr__(self, item):
        if item == 'age':
            return lambda: 25
s = Student()
print s.age()

#只有在找不到属性的情况下才会调用  __getattr__()
#此外,注意任意调用 比如  s.abcd  都会返回None,这是我们定义 的__getattr__()默认返回就是 None,要让我们的 class
# 只响应几个特殊 的属性,我们按照约定抛出 AttibuteError错误就可以了



# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了,不需要任何特殊手段
# 这种完全动态调用的特性有什么实际作用呢? 作用就是可以针对完全动态的情况作调用
# 举个例子:
# 很多网站都搞 REST API, 比如 WEIBO ,豆瓣啥 的,调用API的  URL 类似 :
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK, 给每个URL对应的API都写一个方法,那得累死,而且 API 一旦改动, SDK 也要改
# 利用完全动态的 __getattr__() ,我们可以写出一个链式调用:

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path

print Chain().status.user.isensen.go
# /status/user/isensen/go

# 这样,无论API 怎么变, SDK 都可以根据URL,实现完全动态的调用, 而且,不随API的增加而改变!
# 还有些 REST API 会把参数放到URL中, 比如GITHUB的API
#   GET  /user/:user/repos
# 调用时,需要把  :user 替换为实际用户名,如果我们能写出这样的链接调用
# Chain().users('isensen').repos,就可以非常方便的调用 API了


#-------------------------------------------__call__-------------------------------------------
# 一个对象实例可以有自己的属性和方法, 当我们调用实例方法时 ,我们用 instance.method() 来调用,能不能直接
# 在实例本身上调用呢??? 类似   instance() ?? 在Python中,是可以的!!!!!!!!

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print ('My name is %s.' % self.name )

a = Student('isensen')
a()

Student('i33')()

#  __call__() 也可以接收参数.
#  要判断一个变量是对象还是函数呢?其实
#  更多的时候,我们需要判断一个对象能否被调用,能被调用的对象就是一个 Callable对象

print callable(a)

# 还有很多可定制的方法, 参数 Python文档
# https://docs.python.org/2/reference/datamodel.html#special-method-names