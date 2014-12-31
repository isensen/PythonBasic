#coding=utf-8
"""
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
"""
__author__ = 'isenen'

#首先，我们看看itertools提供的几个“无限”迭代器：

#因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出
import itertools

natuals = itertools.count(1)
for n in natuals:
    print n



#cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
for c in cs:
    print c


#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A', 10)
for n in ns:
    print n


#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print n



#itertools提供的几个迭代器操作函数更加有用：

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
#迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
for c in chain('ABC', 'XYZ'):
    print c



#groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group) # 为什么这里要用list()函数呢？


# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
# 这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略
# 大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print key, list(group)



#imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x




#注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕：
r = map(lambda x: x*x, [1, 2, 3])
print r  #已经计算出来了 [1, 4, 9]



#当你调用imap()时，并没有进行任何计算：
r = itertools.imap(lambda x: x*x, [1, 2, 3])
r # <itertools.imap object at 0x103d3ff90> r只是一个迭代对象


#必须用for循环对r进行迭代，才会在每次循环过程中计算出下一个元素
#这说明imap()实现了“惰性计算”，也就是在需要获得结果的时候才计算。类似imap()这样
#能够实现惰性计算的函数就可以处理无限序列：



#ifilter()就是filter()的惰性实现。


#itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是迭代对象，
#只有用for循环迭代的时候才真正计算。