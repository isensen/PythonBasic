#coding=utf-8
'''
 函数/ 空函数/ 返回多值/ 必选参数/ 默认参数/ 可变参数/ 关键字参数/ 递归函数
'''
__author__ = "i3342th"

print '--------------Function-------------'
#函数名其实就是指向一个函数对象的引用
#没有 return 语句的话,函数也会返回结果,只是结果是 None
# return None 可以简写为 return
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >=0:
        return x
    else:
        return -x

#空函数
def testNullFunction():
    pass

#可返回多个值,(其实本质上也是一个tuple)
def testMutiReturn(x,y):
    return x,y

x,y = testMutiReturn(1,2)

print x,y

#默认参数
#1. 必选参数在前,默认参数在后,否则报错
#2. 如何设置默认参数,应该变化大的参数放前,变化小的放后
#3, 调用时,可以不按默认参数的顺序,只要要把形参名字带上
#4, 默认参数必须指向不变对象,不然会随着调用数数而改变
def power(x, n=2):
    s = 1
    while n >0:
        n = n-1
        s = s * x;
    return s

print power(3), power(3,3), power(3,n=3)

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n *n
    return sum

#可用Tuple 前面加星号调用
t = (1,2,3,4)
print calc(1,2,3,4)#应该这样调用
print calc(*t)#但如果有元组,为了方便,也可以这样调用,就省去了calc(t[0],t[1],t[2])这样的调用了
print calc(*(1,2,3,4))


#关键字参数,关键字参数允许你传0个或任意个含参数名的参数.这些参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:',kw

person('i3342th',33)
person('i3342th',33,city='dongying')
person('i3342th',33,city='dongying',job='software engineer')

#函数定义可以用 必选参数/ 默认参数/ 可变参数/ 关键字参数
# 4 种参数可以同时使用,或者只用某些,但注意,参数定义的顺序一定要符合上面列出
def func(a,b,c=0,*args,**kw):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw

print func(1,2)
print func(1,2,c=3)
print func(1,2,3,'a','b')
print func(1,2,3,'a','b',x=99)

#最神奇的可以通过一个tuple 和dict调用
args = (1,2,3,4)
kw = {'x':99}
func(*args, **kw)


#递归函数
#递归函数都可用循环方式写出,但递归逻辑清晰,简单
#递归注意防止栈溢出(是通过栈stack这种数据结构实现的),调用次数过多,会导致栈溢出
#解决递归栈溢出的方法是通过  尾递归  优化
#实际上,尾递归和循环效果是一样的,所以把循环看成是一种特殊的尾递归函数是可以的
#尾递归:
#     在函数返回的时候,调用自身本身,并且return语句不能包含表达式,这样编译器或解释器
#     就可以把尾递归做优化,使递归本身无论调用多少次,都只占用一个栈帧,不会出现栈溢出
# 遗憾的是: 大多数编程语言没有针对尾递归做优化, Python解释器也没有做优化,所以即使改成尾递归方式,也会溢出
# 不过有一个针对尾递归优化的 decorator ,后面会提到怎么编写 decorator
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)


#  下面是利用尾递归优化
#  可以看到, return fact_iter(product * count, count +1, max) 仅返回递归函数本身
#  尾递归调用时,如果做了优化,栈不会增长,因此无论调多少次都不会溢出
def fact(n):
    return fact_iter(1,1,n)

def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count+1, max)

print fact(4)
