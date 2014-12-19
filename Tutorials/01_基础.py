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
null = None                 #None 是空值
print null
a1, a2, a3 = 1, 'a2', True
a4 = 0x123                  #十六进制
a5 = 1.2e-5                 #科学计数法
a6 = r'\n\.\1'              #r 字符表示里面的字符不进行转义
a = '''
  这样可是可以的
  就不用\\n换行了
'''                         #'''里面还是会转义的,要想不转义,前面加 r
print a1,a2,a3,a4,a5,a6,a

print '----------------逻辑----------------'
True and True or True
not True

if not False:
    print True





print '----------------输入---------------'
#test_raw_input = raw_input('This is raw_input:')
#test_input = input('This is input:')
#input() 本质上还是使用 raw_input() 来实现的，只是调用完 raw_input() 之后再调用 eval() 函数，
#所以，你甚至可以将表达式作为 input() 的参数，并且它会计算表达式的值并返回它。
#raw_input()读取的内容永远以字符串的形式返回,也就是说用户输入了  100 其实到程序里是 '100'
# birth = int(raw_input('birth: ')) 这样转一下才是int




print '----------------输出---------------'
#打印 %d整数  %f浮点数  %s字符串   %x十六进制整数
spaces = ' ' * 25
print('%s 12 Butts Wynd' % spaces)
print('%s Twinklebottom Heath' % spaces)
print('%s West Snoring' % spaces)
print('')
print() # This print a empty row in Python 3 version
print  ()
print('Dear Sir....')
a = "aaaa %s te %sst"
print a % (1,2)





print '----------------List---------------'
#list
basic = [0,1,2]
basic.append(3)
basic.remove(0)
len(basic)
print basic, len(basic)
del basic[1]
print basic
#basic.remove(100)
print basic

ad = [1,2,3,3,'4',['a','b']]
print ad[1],ad[1:4],ad[-1]

print(basic + ad)
print(basic * 5)





print '---------------Tuple---------------'
# tuple 元组,和 list的区别:不可修改
# 它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
test = (1, 2, 4, 5)
test2 = ()           #空的元组
print test, test[0]
t = (1)              #这个不是tuple,这个是带一个括号的数字1
t1 = (1,)            #这个才是tuple,加逗号就是为了消除歧义
test2 = (6,7)
print test + test2
#test[0] = 0    'tuple' object does not support item assignment
#来看一个可变的Tuple,不是不可变的吗?其实改变的是里面的list , 不是Tuple自身,里面的list指向并没有改变
#要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'




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
