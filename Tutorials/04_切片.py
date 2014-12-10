#coding=utf-8
'''
切片(list, tuple, 字符串 Unicode)
'''
__author__ = "i3342th"

L = ['a','b','c','d','e']

#取前三个元素
#笨方法:
tmp1 = [L[0],L[1],L[2]]
print tmp1

#稍聪明一点可扩展方法
tmp2 = []
n = 3
for i in range(n):
    tmp2.append(L[i])
print tmp2

#高级特性 切片

print L[0:3], L[:3], L[-2:]#有下限,无上限

L = range(100)
print L
#前10个数
print L[:10]
#后10个数
print L[-10:]
#前10个数,每2个取一个
print L[:10:2]
#所有数,每5个一取
print L[::5]

print L[:]

#tuple 也是一种list,唯一区别是tuple不可变,因此tuple也可以进行切片操作,只是操作结果仍是tuple
print (0,1,2,3,4,5,6,7,8,9)[:3]
#字符串或 Unicode 也可以看成是一种list,也可以进行切片操作
print 'ABCDEFG'[:3]