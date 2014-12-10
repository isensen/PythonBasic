#coding=utf-8

'''
   序列化
   在程序运行中, 所有的变量都是在内存中, 比如,定义一个dict:
   d = dict(name='Bob', age=20, score=88)
   可以随时修改变量,比如把name改成'Bill',但是一旦程序结束,变量所占用的内存就会被操作系统全部回收, 如果
   没有把修改后的'Bill'存储到磁盘上,下次重新运行程序,变量又会被初始化为'Bob'

   我们把变量存储到磁盘的过程称之为序列化, 在Pthon中叫picking, 在其他语言中称为 serialization
   marshalling, flattening等等,都是一个意思

   反过来,从磁盘所变量内容重新读到内存里称之为反序列化,即unpicking

   python提供两个模块来实现序列化:cPickle  和 pickle
   这两个模块功能是一样的,区别在于cpickle是C语言写的,速度快,pickle是纯Python写的,速度慢
   跟cStringIO和stringIO是一个道理, 用的时候,先尝试导入cPickle,如果失败,再导入pickle

'''

__author__ = "i3342th"
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='isensen', age=20, score=100 )
a = pickle.dumps(d)#序列化为一个str
print a

with open('../R/dump.txt','wb') as f:
    pickle.dump(d,f) #序列化到文件

# 当我们需要把对象从磁盘读到内存时,可以先把内容读到一个str,然后用pickle.loads()方法反序列化出对象,
# 也可以直接用 pickle.load()方法,从一个file-like object中直接反序列化出对象

with open('../R/dump.txt','rb') as f:
    d1 = pickle.load(f)
print d1

# 变量又回来了,当然和原来的变量是完全不相干的对象, 它们只是内容相同而已.
# pickle 的问题和其他编程语言特有的序列化问题一样, 就是它只能用于Python
# 并且可能不同版本的Python彼此都不兼容


#-----------------------------------Json-----------------------------------------

#如果我们要在不同的编程语言之间传递对象, 就必须把对象序列化为标准格式, 比如XML, 便更好的序列化为JSON
#因为JSON表示出来就是一个字符串, 可以被所有语言读取, 也可以方便地存储到磁盘或者通过网络传输
#JSON不仅是标准格式,并且比XML更快, 而且可以直接在WEB页面中读取, 非常方便.

#Python内置的json模块提供了非常完善的Python对象到Json格式的转换
#dumps返回一个str,内容就是标准的Json,类似的dump()方法可以直接把JSON写入一个file-like object
import json
d = dict(name = 'isensen', age='20', score =100)
print json.dumps(d)

#要把JSON反序列化为Python对象, 用loads() 或 对应的load()方法, 将者把JSON的字符串反序列化, 后者从
# file-like object中读取字符串并反序列化

json_str = '{"age":20, "score":88, "name":"i33"}'
d2 = json.loads(json_str)
print isinstance(d2,dict), d2

#反序列化得到的所有字符串对象默认都是unicode而不是str.由于JSON标准规定JSON编码是UTF-8,所以
#我们总是能正确地在Python的str或unicode与JSON字符串之间转换


#--------------------------------JSON进阶---------------------------------------------------------
#我们很多时候,更喜欢用class表示对象, 比如定义Student,然后序列化,而不是从dict

import json
class Student(object):
    def __init__(self,name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('isensen', 20, 100)
#print json.dumps(s)
#TypeError: <__main__.Student object at 0x00BCC7D0> is not JSON serializable

#dumps()方法还提供了一大堆参数
#可选参数default就是把任意一个对象变成一个可序列化为JSON的对象, 我们只需要为Student专门写一个转换函数

def student2dict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

#这样Student实例首先被student2dict()函数转换为dict,然后再被转换为JSON
print (json.dumps(s, default=student2dict))

# 不过下一次如果再是个Teacher类呐?就又不行了,照样无法序列化为JSON,
# 我们可以偷个懒,把任意class的实例变为dict:
# 因为通常class的实例都有一个__dict__属性,它就是一个dict,用来存储实例变量
# 也有少数例外,比如定义了__slots__的class

print (json.dumps(s,default=lambda obj:obj.__dict__))

#class 对象的反序列化
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = '{"age":20, "score":100, "name":"i33"}'
s1 = json.loads(json_str, object_hook=dict2student)
print isinstance(s1,Student)