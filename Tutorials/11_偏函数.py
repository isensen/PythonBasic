#coding=utf-8
'''
    偏函数(Partial Function)(部分函数)
    Python 的  functools 模式提供了很多功能, 其中一个就是偏函数
    注意: 这里的偏函数 和 数学里的偏函数不同

    简单理解: 和默认参数提供的功能类似(联想JS里partial function)

    简单总结:
    functools.partial的作用就是,把一个函数的某些参数(不管有没有默认值)固定住(设默认值)
    返回一个新的函数,使函数时更简单
    要从右向左固定参数,不然会变得很复杂
'''
__author__ = "i3342th"

#int 函数提供了额外的 base 参数,默认值为10,如果传入base参数,可以做N进制的转换
print int('12345')

print int('12345',base = 8 )

print int('12345', 16)

# 假设我们有大量的二进制需要转换, 每次都传入 int(x, base=2) 很麻烦,我们可能会想到定义一个int2()函数

def int2(x, base=2):
    return int(x,base)

print int2('1000')

# functools.partial 就是帮助我们创建一个偏函数, 不需要我们自定义int2(),可以直接使下面的代码创建一个新的int2:
import functools

int2 = functools.partial(int, base=2)#也可以赋给int ,更改默认
print int2('1000')
print int2('1000',base = 10)#当然也可以像原来一样传入新值,不用默认值

