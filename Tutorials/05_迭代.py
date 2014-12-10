#coding=utf-8
'''
迭代
'''
__author__ = "i3342th"

#如果给定一个list 或 tuple 我们可以通过 for 循环遍历,这种遍历我们称为迭代 (iteration)

#python 中  迭代  是通过 for ... in  来完成的
#for ... in  不只可用于 list , tuple,还可用于其他可迭代对象上,例如:dict

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
#dict 存储不是按顺序来的,所以打印出来顺序是不一定的
#默认dict 用for 迭代的是 key
#如果迭代value,可以用  for value in d.itervalues()
#同时迭代 key value,   for k,v in d.iteritems()

for value in d.itervalues():
    print value

for k, v in d.iteritems():
    print k,'-->',v

#字符串也可以迭代

for ch in 'i3342th':
    print ch

#那么如何判断一个对象可迭代呢?

from collections import Iterable
print isinstance('abc',Iterable)
print isinstance(123,Iterable)

#如果要实现类似Java里的下标循环怎么办?
#Python 内置的 enumerate 函数可以把一个list变成索引-元素对

for i, v in enumerate(['i','3','3']):
    print i, '-->', v


#for 循环中同时引多个变量
for x, y in [(1,1),(2,4),(3,9)]:
    print x,y