#coding=utf-8

'''
    为了方便管理, 重用, 避免冲突等原因,引入了模块 / 包的概念
    目录结构

    mycomapny
       __init__.py
       acb.py
       xyz.py


    每个包的目录下面都会有一个__init__.py 文件, 这个文件是必须的
    否则 Python就会把这个目录当成普通目录,而不是一个包
    __int__.py 可以是一个空文件,也可以有Python代码
    因为 __init__.py 本身就是一个模块,而它的模块名就是包名 mycompany

    可以有多级目录 ,级成多层次的包结构
'''

__author__ = "i3342th"

import sys

def test():
    args = sys.argv  #argv 用list 存储命令行调用参数,至少会有一个,并且永远是文件名 12_模块.py
    print args
    if len(args) == 1:
        print 'Hello world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments'

if __name__ =='__main__':
    test()


# 导入模块时可以起别名
# Python 库一般会提供 StringIO 和 cStingIO 两个库,这两个库的接口一样的,但是 cStringIO是 C写的,速度更快
# 所以会经常看到这样的写法
# 这样就可以优导入 cStringIO

try:
    import cStringIO as StringIO
except ImportError:#导入失败会捕获到ImportError
    import StringIO



#作用域
# __xxx__ 这种名称是特殊变量如  __author__     __name__    __doc__
# _xx __xxx 这样的变量是private变量,不应该被外部直接引用
# _xx 是规范,外部其实还是能访问,是不建议
# __xxx是外部真不能访问,(其实也可以,就是Python解释器那它改名了)

# python 搜索引入模块时,会寻找 当前目录 /所有已安装的内置模块和第三方模块搜索路径放在了sys.path里

print sys.path
#如果我们要添加自己的搜索目录 ,有两种方法 :
# 1.
# sys.path.append('自定义的路径')
# 2.
# 设置环境变量PYTHONPATH,该环境变量内容会被自动添加到模块搜索路径中. Python自身的搜索路径不会受到影响
