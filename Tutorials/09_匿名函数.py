#coding=utf-8
'''
    lambda
    关键字 lambda  表示匿名函数,冒号前的x,表示函数参数

    匿名函数有个限制就是只能有一个表达式,不用写 return, 返回值就是该表达式的结果

    有个好处,因为没名字,不用担心 函数名冲突

    匿名函数也是一个函数,可以赋值给一个变量

    同样,也可以把匿名函数作为返回值返回

    python 对匿名函数支持有限,只有一些简单的情况下可以使用匿名函数
'''
__author__ = "i3342th"

print map(lambda x: x*x , [1,2,3,4,5,6,7,8,9])

f = lambda x: x * x

print f(5)






