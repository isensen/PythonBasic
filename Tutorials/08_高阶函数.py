#coding=utf-8
'''
高阶函数(Higher-order function)
 1) 能够接收函数做为参数的函数
 2) 把函数作为返回结果
'''
__author__ = "i3342th"

print '--------------Higher-order Function-------------'
def f(x):
    return x * x

print map(f , [1,2,3,4,5])

def add(x,y):
    return x + y
print reduce(add, [1,2,3,4,5])

#当然像上例的求各运用太简单,我们可以直接用sum()
print sum([1,2,3,4,5])
print sum({1,2,3,4,5})


def fn(x,y):
    return x * 10 + y

# 因为字符串也是一个序列
# print map(int,'12345')  [1,2,3,4,5]
# 实现了,不用系统内置方法,而自己实现了 str -> int
print reduce(fn, map(int,'12345'))#最后输出  12345  ,有点巧妙..:)

# 结合 lambda
def str2int(s):
    return reduce(lambda x, y: x* 10 +y , map(int, s))




# 无论是冒泡排序还是快速排序, 核心是比较两个元素的大小. 如果是数字我们可以直接比较,但如果是字符串或者
# 两个dic呢? 直接比较数字上的大小是没有意义的, 因此比较的过程必须通过函数抽象出来. 通常规定 , 对于两
# 个元素 x 和 y, 如果认为 x < y, 则返回-1, 如果认为 x == y , 刚返回 0, 如果认为 x > y, 则返回 1, 这样
# 排序算法就不用关心具体的比较过程,而是根据比较结果直接排序.

#python内置的sorted()函数,就可以对list排序
print sorted([123,2,4,6,234,2])

# 此外 sorted() 函数也是一个高阶函数,可以接受一个比较函数来自定义排序.
# 倒序
def reverse_cmp(x, y):
    if x > y :
        return -1
    if x < y:
        return 1
    return 0

print sorted([23,21,1,55,2], reverse_cmp)


#返回函数

#引子, 求和

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

#改造, 如果不需要立刻求和,而是在后面代码中,根据需要再计算怎么办, 可以不返回求和的结果,而是返回求和的函数

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 上面例子中, 我们在函数 lazy_sum 中又定义了函数 sum
# 并且,内部函数sum 可以引用外部函数 lazy_sum的参数和局部变量
# 当 lazy_sum 返回 函数 sum 时, 相关参数和变量都保存在返回函数中
# 这种称为 "闭包(closure)" 的程序结构拥有极大的威力





