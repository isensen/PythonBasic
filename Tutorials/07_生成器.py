#coding=utf-8
'''
生成器 yield
'''
__author__ = "i3342th"


# 通过列表生成式,我们可以直接创建一个列表
# 但是受到内存限制, 列表容量肯定是有限的,而且创建一个包含100万个元素的列表,不仅占用很大的存储空间,如果我们
# 仅仅需要访问前面几个元素,那后面绝大多数元素占用的空间就白白浪费了.

# 所以如果列表可以按照某种算法推算出来,那我们是否可以在循环的过程中不断推算出后续的元素呢? 这样就不必创建
# 完整的list, 从而节省大量的空间

# 在 Python中,这种 一边循环, 一边计算的机制,称为生成器(Generator)

# 创建一个生成器,有很多种方法 , 第一种方法很简单,只要把一个列表生成器的[] 改成 ()


#L = [x * x for x in range(100000000)] Memory Error
L = [x * x for x in range(10)] #列表生成
g = (x * x for x in range(10)) #生成器

print L # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print g # <generator object <genexpr> at 0x00BC02D8>

# 可以看出,可以直接打印出 L, 因为他是个列表,而不能直接打印出 g ,因为他是个generator
# 如果要打印g ,要利用 generator的 next()

print g.next() #0
print g.next() #1


# generator 保存的是算法,每次调用 next() , 就计算出下一个元素的值,直到最后一个元素,没有更多元素时
# 抛出 StopIteration的错误
# 一直用next() 太变态 了,可以用循环, generator 是可迭代的


g = (x * x for x in range(10))
for n in g:
    print n


# generator 非常强大,如果推算的算法比较复杂,用类似 列表生成 的方式无法实现时,还可以用函数来实现
# 比如著名的斐拉波契数列, 除第一个和第二个数外, 任意一个数都是由前两个数相加得到:
# 1,1,2,3,5,8...
# 用列表生成式写不出来,但可用函数打印出来:
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

fab(8)

# 可以观察,上面fab函数实际上是定义了斐波拉契数列的推算规则 ,可以从第一个元素,推算出后续任意的元素,
# 这种逻辑非常类似 generator

# 只需把 print b ,换为  yield b
# 如果一个函数定义中包含 yield ,那么这个函数不再是一个普通函数,而是一个generator
# 最难理解的就是generator  和  函数的执行流程不一样,函数是顺序执行,遇到return 或最后一行语句就返回.
# 而变成generator函数, 在每次调用  next() 的时候执行, 遇到 yield() 语句返回,再次执行时,从上次返回的 yield语句
# 处继续执行
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

print fab(6) #<generator object fab at 0x00BC03F0>



# 简单例子

def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

o = odd()
print o.next()
print o.next()
print o.next()


# 我们基本上也不会用next()来调用generator, 而是用for
for n in fab(6):
    print n