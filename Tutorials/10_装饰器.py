#coding=utf-8
'''
    装饰器(Decorate)
    由于函数也是一个对象, 并且可以赋值给变量,所以通过变量也可以调用函数

    函数对象 有一个  __name__ 属性,可以拿到函数的名字

    假如我们要扩展一个函数的功能, 在函数调用前后自动打印日志,但不希望修改 原函数定义

    这种代码在运行期间动态增加功能的方式,称为 "装饰器"
'''
__author__ = "i3342th"

print __name__

def test():
    pass

print test.__name__


#原函数






# log 函数是一个decorator, 所以接受一个函数作为参数, 并返回一个函数

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

# 借助 Python @ , 将decorator置于函数的定义处
# 相当于执行了  now = log(now)
@log
def now():
    print '2014-06-30'

# 输出:
# call now()
# 2014-06-30
now()



#更高级的装饰器,举个简单的例子,还是LOG,如果想自定义输出文字
#比如我想函数调用前 输出" 我调用了 now()
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

# 相当于执行了 now = log2('我调用了')(now)
@log2('我调用了')
def now():
    print '2014-06-30'

now()

# 上面说了,函数是有__name__属性的,经过上面的装饰器之后,名称不是原来的名字了
print now.__name__ # wrapper


# 所以需要将原来的__name__ 复制到wrapper,保留以前的__name__, 否则有些依赖函数名的代码会执行出错
# 不需要执行 wrapper.__name__ = func.__name__ 这样的代码
# Python 内置的 functools.wraps 就是干这个的,所以,一个完整的Decorator是这样写的


import functools

def  log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log3('俺调用了')
def now():
    print '2014-06-30'


print now.__name__
