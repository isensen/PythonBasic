#coding=utf-8

'''
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，
但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
然后，分别在父进程和子进程内返回。


子进程永远返回0，而父进程返回子进程的ID。
这样做的理由是，一个父进程可以fork出很多子进程
所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。


Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：




'''

__author__ = "i3342th"

import os

print 'Process (%s) start ...' % os.getpid()
pid = os.fork() # unix/linux 下,  wndows里木有

if pid == 0:
    print ' I am child process (%s) and my parent is %s.' % (os.getpid(), os.getpid())
else:
    print ' I (%s) just create a child  process(%s)' % (os.getpid(), pid)



'''
有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求



multiprocessing
如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。
由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序

由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。
multiprocessing模块就是跨平台版本的多进程模块。

'''

# 子进程要执行的代码

from multiprocessing import Process
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join() #方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print 'Process end.'



'''
    Pool
    如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

    对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()
    调用close()之后就不能继续添加新的Process了。
'''
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'



'''
进程间通信
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
'''
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()