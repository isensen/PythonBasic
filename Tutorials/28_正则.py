#coding=utf-8
'''
 s = 'ABC\\-001' #python的字符串
 对应的正则表达式字符串变成:
 'ABC\-001'
 因此强烈建议使用Python的 r 前缀,这样就不用考虑转义问题了
'''
__author__ = 'isenen'

import re

#如果匹配成功,返回一个match对象,否则返回None
a  = re.match(r'\d{3}\-\d{3,8}','010-12345')
print a #<_sre.SRE_Match object at 0x00ACE410>

test = '用户输入的字符串'
if re.match(r'正则表达式',test):
    print 'ok'
else:
    print 'failed'


#========================================正则表达式切分字符=======================================
#正常切分
test = 'a b   c'.split(' ')
print test #['a', 'b', '', '', 'c']

#正则切分
test2 = re.split(r'\s+', 'a b   c')
print test2 #['a', 'b', 'c']

test3 = re.split(r'[\s\,]+','a, b   c')
print test3 #['a', 'b', 'c']

#=====================================分组(捕获)===================================================
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

#group(0)永远是原始字符串
print 'group(0):', m.group(0)
print'group(1):',m.group(1)
print 'group(2):',m.group(2)

#======================================贪婪=========================================================
# 默认是贪婪匹配
print  re.match(r'^(\d+)(0*)$','102300').groups() #('102300', '')

#要用非贪婪
print  re.match(r'^(\d+?)(0*)$','102300').groups() #('1023', '00')

#======================================编译=========================================================
#编译后生成Regular Expression对象
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

print re_telephone.match('010-12345').groups()
print re_telephone.match('010-23423').groups()



