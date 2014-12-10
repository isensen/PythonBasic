#coding=utf-8
'''
 赋值/ 输出/ List/ Tuple/ Dict/ Set 基础操作

 一定要记住:
 Python类似于JS的函数作用域
 Python中能改变变量使用域的就是: 函数 ,类, lambda

'''
__author__ = "i3342th"

print '----------------赋值---------------'
#可以这样赋值
a1, a2, a3 = 1, 'a2', True
print a1,a2,a3
print ("hahahahahahah")
a = "aaaa %s te %sst"
print a % (1,2)
print 10 * 'a'

print '----------------输出---------------'
#打印
spaces = ' ' * 25
print('%s 12 Butts Wynd' % spaces)
print('%s Twinklebottom Heath' % spaces)
print('%s West Snoring' % spaces)
print('')
print() # This print a empty row in Python 3 version
print  ()
print('Dear Sir....')

print '----------------List---------------'
#list
basic = [0,1,2]
basic.append(3)
basic.remove(0)
print basic
del basic[1]
print basic
#basic.remove(100)
print basic

ad = [1,2,3,3,'4',['a','b']]
print ad[1],ad[1:4],ad[-1]

print(basic + ad)
print(basic * 5)

print '---------------Tuple---------------'
#tuple 元组,和 list的区别:不可修改
test = (1, 2, 4, 5)
print test, test[0]
t = (1) #这个不是tuple,这个是带一个括号的数字1
t1 = (1,)#这个才是tuple,加逗号就是为了消除歧义
test2 = (6,7)
print test + test2
#test[0] = 0    'tuple' object does not support item assignment

print '--------------Map/dict-------------'
#dict,也称map
#和list 相比
#1) 查找和插入速度极快,不会随着key的增加而增加(有类似索引的东西)
#2) 需要占用大量的内存,内存浪费很多
# 所以dict是用空间换与时间的一种方法,牢记一点,dict的key,必须是不可变对象(要根据它来计算value的位置啊)
map1 = {'a': 'A', 'b':'B', 'c':'C'}
print map1, map1['a']
del map1['b']
map1['a']='AA'
print map1
map2 = {'d':'D'}
#不能进行加操作
#map1 + map2  #unsupported operand type(s) for +: 'dict' and 'dict'
#可判断是否在MAP里
print ('d' in map2)
print map1.get('b', 'default')
print (map2.get('SB','this is the value if not exsit'))
print map1.pop('a'),'map1 --->', map1#会将a pop出,并将其在 map1中删除
#None值
nullvalue = None

print '----------------Set----------------'
#和dict类似 ,也是一组key的集合(key也不可变),唯一的区别不同的是,不能存储value
#key不能重复
#set可以看做数学意义上无序和无重复元素的集合,所以可以进行交集,并集等操作
s = set([1,2])# 用list 为参数
print s
s1 = set([1,1,1,2,2])
print s1 # set([1,2])
print (s == s1)#True
s.add(3)
print s
s.remove(1)
print(s)

print s & s1, s | s1
