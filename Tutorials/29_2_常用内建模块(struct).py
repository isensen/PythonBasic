#coding=utf-8
"""
准确地讲，Python没有专门处理字节的数据类型。但由于str既是字符串，又可以表示字节，所以，字节数组＝str。
而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。


"""
__author__ = 'isenen'


#在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的str，你得配合位运算符这么写：
n = 10240099
b1 = chr((n & 0xff000000) >> 24)
b2 = chr((n & 0xff0000) >> 16)
b3 = chr((n & 0xff00) >> 8)
b4 = chr(n & 0xff)
s = b1 + b2 + b3 + b4
print s


#非常麻烦。如果换成浮点数就无能为力了。
#好在Python提供了一个struct模块来解决str和其他二进制数据类型的转换。
#struct的pack函数把任意数据类型变成字符串：
import struct
struct.pack('>I', 10240099)

struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')