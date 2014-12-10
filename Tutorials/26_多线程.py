#coding=utf-8

'''
    多任务可以由多进程完成, 也可以由一个进程内的多线程完成

    一个进程至少有一个线程

    线程是操作系统直接支持的执行单元,因此高级语言都内置多线程的支持

    Python的线程是真正的   Posix Thread ,而不是模拟出来的线程.

    Python 标准库提供了两个模块: thread  和 threading

    thread 是代级模块, threading 是高级模块,对thread进行了封装,绝大多数下,我们只需要使用threading这个高级模块

    启动一个线程就是把一个函数传入,并创建Thread实例, 然后调用 start() 开始执行:

    任何程序默认都会启动一个线程,我们把该线程称为  主线程,主线程又可以启动新的线程


    多线程和多进程最大的不同在于:
    多进程中,同一个变量, 各自有一份拷贝,存在于每个进程中,互不影响,而多线程中,所有变量都是所有线程共享的.
    所以任何一个变量都可以被任何一个线程修改,因此,线程之间共享数据最大的危险在于多个线程同时修改一个变量.
    所以有了LOCK



'''

__author__ = "i3342th"


#可以让CPU 使用率提高的代码
#########################################################
import threading , multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target = loop)
    t.start()
#########################################################
'''
    启动与CPU核心数量相同的N个线程, 在4核CPU上可以监控到CPU占用率仅有160%, 也就是使用不到两核
    即使启动100个线程,使用率也就170%左右,仍然不到两核

    但是用C/ C++/ JAVA 来改写相同的死循环, 直接可以把全部核心跑到400%, 8核就跑到800%

    为什么Python不行呢?

    因为Python的线程虽然是真正的线程,但解释器执行代码时, 有一个GIL锁: Global Interpreter Lock,
    任何Python线程执行前,必须先获得GIL锁, 然后,每执行100条字节码, 解释器就自动释放GIL锁,让别的
    线程有机会执行.这个GIL全局锁实际上把所有的线程执行都给上了锁, 所以, 多线程在Python中只能交
    替执行,即使100个线程跑在100核CPU上,也只能用到1个核

    GIL 是Python解释器设计的历史遗留问题,通常我们用的解释器是官方实现的Cpython, 要真正利用多核
    ,那只能通过C扩展来实现,不过这样就失去了Python简单易用的特点

    不过,也不用过于担心, Python虽然 不能利用多线程实现多核任务, 但可以通过多进程实现多核任务.
    多个Python进程有各自独立的GIL锁,互不影响


    小结:
    多线程编程,模型复杂,容易发生冲突, 必须用锁加以隔离, 同时,又要小心死锁的发生
    Python解释器由于设计时有GIL全局锁, 导致了多线程无法利用多核.
    多线程的并发在Python中就是一个美丽的梦.
'''

