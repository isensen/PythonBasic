#!/usr/bin/env python
# _*_ coding: utf-8 _*_

'''
测试文件
第一行,可以让文件直接在Unix/Linux/Mac上运行

脚本语言的第一行，目的就是指出，你想要你的这个文件中的代码用什么可执行程序去运行它，就这么简单
#!/usr/bin/python是告诉操作系统执行这个脚本的时候，调用/usr/bin下的python解释器；
#!/usr/bin/env python这种用法是为了防止操作系统用户没有将python装在默认的/usr/bin路径里。当系统看到这一行的时候，首先会到env设置里查找python的安装路径，再调用对应路径下的解释器程序完成操作。
#!/usr/bin/python相当于写死了python路径;
#!/usr/bin/env python会去环境设置寻找python目录,推荐这种写法

第二行表示文件编码,也可以写 coding=utf-8

本区域为文档注释
任何模块代码的第一个字符串都被视为模块的文档注释,可以用  模块名.__doc__  引用

__author__ 变量,存储作者名字,当公开源码后,别人可以瞻仰你,哈哈

当然也可以全删掉不写
'''

__author__ = 'isensen'
