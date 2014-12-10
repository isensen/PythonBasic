#coding=utf-8
'''
   1. 类型转换
   2. 判断类型
   3. 长度
   4. 获取一个对象所有方法和属性,判断是对象是否有 X 方法
   5. 异常
'''
__author__ = 'Administrator'

#-------------类型转换-------------
print int('123') ,isinstance(int('123'),int)
print float('123'), isinstance(float('123'),str)
print str(123) ,isinstance(str(123),str)
print unicode(100),  isinstance(unicode(100),unicode)
print ord('A'), chr(65)
print u'中文'.encode('utf-8')

print bool(1), bool('')

#-----------------------------------------------判断是否是类型------------------------------------------
# type('foo') == str 也可以判断
# 但区别在于 type() 不会认为子类是一种父类型,  isinstance()会认为子类是一种父类类型
if not isinstance(1, (int, float)):
        raise TypeError('类型错误哦')

if type(123) == type(456):
    pass

#Python把每种type类型都定义了常量 ,放在types里

import types
type('abc') == types.StringType
type([]) == types.ListType
type(str) == types.TypeType #所有类型本身都是TypeType


#-------------------------------------------------条件表达式------------------------------------------------
a = True if 5 >0 else False

#-------------------------------------------------长度----------------------------------------------------
print len({1,2,3}) # len()方法内部实现,是去调用对象内部的方法 __len__() ,和{1,2,3}.__len__()等价
print {1,2,3}.__len__()
print len([1,2,3])
print len({'1':'a','2':'b','3':'c'})

#自己编写的类,如果 也想实现 len(MyClass)  就在实现类的时候定义内部方法 __len__(self)就可以了

#---------------------------------------------获取一个对象所有方法和属性----------------------------------

print dir('Abc')

#判断对象是否有指定属性
print hasattr(str,'__len__')
#设置 对象属性  setattr()

#获取对象属性   getattr()
#只有在不明白对象内部的情况下才去获取对象信息
#如果可以直接 sum = obj.x + obj.y
#就不要写     sum = getattr(obj, 'x') + getattr(obj, 'y')

#---------------------------------------异常-----------------------------------------------
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError', enumerate
except ZeroDivisionError, e:
    print 'ZeroDivisionError', enumerate
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'

# 日志
# Python内置的logging模块可以很容易地记录错误信息
# logging.exception(e)  这样出错后,程序打印完错误信息后,会继续执行,并且 正常退出
# 还可以把错误记录到日志文件

#自定义错误
class FooError(StandardError):
    pass

# 如果在except语句中,用print XXX信息一下,然后再将错误抛出, 有时可以方便后续追踪,
# 只要在except中  raise       不带参数,就是把当前错误原样抛出

#---------------------------------------

print __file__

import sys
print sys.path


#-----------------------------------------

import cx_Oracle

#建立和数据库系统的连接

conn = cx_Oracle.connect('test/test@10.68.6.223/orcl')

#获取操作游标

cursor = conn.cursor()

#执行SQL,创建一个表

cursor.execute("""create table tb_user(id number, name varchar2(50),password varchar(50),primary key(id)) """)

#关闭连接，释放资源

cursor.close()

#执行完成，打印提示信息

print 'Completed!'



