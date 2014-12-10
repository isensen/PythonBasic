#coding=utf-8
'''
列表生成 即  List Comprehensions
'''
__author__ = "i3342th"

L1 = range(5,11)
print L1

#如果要生成 [1*1, 2*2, 3*3, ... , 10*10]怎么办

#笨方法:
L2 =[]
for x in range(1,11):
    L2.append(x * x)
print L2

#聪明方法:
print [x * x for x in range(1,11)]
# for 循环还可以加上判断
print [x * x for x in range(1, 11) if x % 2 == 0]
# 还可以使用两层循环,生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']
#当然也可以写3层或以上循环,但很少用到


#利用这个可以写出很简洁的代码
#如: 列出当前目前下所有的文件和目录名

import os
#  .  代表当前目录   .. 上层目录
print [d  for d in os.listdir('.')]


# for 循环可以利用多个变量
# 所以列表生成,也可以使用多个变量

d = {'x':'A', 'y': 'B', 'z':'C'}
print [k + '=' + v for k,v in d.iteritems()]

