#coding=utf-8
"""
了解了WSGI框架，我们发现：其实一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。但是
如何处理HTTP请求不是问题，问题是如何处理100个不同的URL。

每一个URL可以对应GET和POST请求，当然还有PUT、DELETE等请求，但是我们通常只考虑最常见的GET和POST请求。

一个最简单的想法是从environ变量里取出HTTP请求的信息，然后逐个判断：

"""
def handle_home(*args):
    pass
def handle_signin(*args):
    pass

def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method=='GET' and path=='/':
        return handle_home(environ, start_response)
    if method=='POST' and path=='/signin':
        return handle_signin(environ, start_response)

"""
只是这么写下去代码是肯定没法维护了。
代码这么写没法维护的原因是因为WSGI提供的接口虽然比HTTP接口高级了不少，但和Web App的处理逻辑比，还是比
较低级，我们需要在WSGI接口之上能进一步抽象，让我们专注于用一个函数处理一个URL，至于URL到函数的映射，就
交给Web框架来做。


常见的Python Web框架:
1) Flask

2) Django：全能型Web框架；

3) web.py：一个小巧的Web框架；

4) Bottle：和Flask类似的Web框架；

5) Tornado：Facebook的开源异步Web框架。

"""






