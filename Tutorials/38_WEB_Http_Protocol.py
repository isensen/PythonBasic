#coding=utf-8
"""
HTTP protocol

每个HTTP请求和响应都遵循相同的格式，一个HTTP包含Header和Body两部分，其中Body是可选的。



------------------------------请求格式 -------------------------------------
HTTP协议是一种文本协议，所以，它的格式也非常简单。每个Header一行一个，换行符是\r\n。

1) HTTP GET请求的格式：

                          +-----------------------+
                          | GET /path HTTP/1.1    |
                          | Header1: Value1       |
                          | Header2: Value2       |
                          | Header3: Value3       |
                          +-----------------------+

2) HTTP POST请求的格式：(当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body)

                          +-----------------------+
                          | POST /path HTTP/1.1   |
                          | Header1: Value1       |
                          | Header2: Value2       |
                          | Header3: Value3       |
                          |                       |
                          | body data goes here...|
                          +-----------------------+

------------------------------响应格式 -------------------------------------
Body的数据类型由Content-Type头来确定，如果是网页，Body就是文本，如果是图片，Body就是
图片的二进制数据。
当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip，所以，看到
Content-Encoding: gzip时，需要将Body数据先解压缩，才能得到真正的数据。压缩的目的在于
减少Body的大小，加快网络传输。

                          +----------------------+
                          | 200 OK               |
                          | Header1: Value1      |
                          | Header2: Value2      |
                          | Header3: Value3      |
                          |                      |
                          | body data goes here..|
                          +----------------------+


Detail:

GET / HTTP/1.1
GET表示一个读取请求，将从服务器获得网页数据，/表示URL的路径，URL总是以/开头，/就表示首页，
最后的HTTP/1.1指示采用的HTTP协议版本是1.1。目前HTTP协议的版本就是1.1，但是大部分服务器也
支持1.0版本，主要区别在于1.1版本允许多个HTTP请求复用一个TCP连接，以加快传输速度。


响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时
发生了错误；


Content-Type: text/html
Content-Type指示响应的内容，这里是text/html表示HTML网页。请注意，浏览器就是依靠Content-
Type来判断响应的内容是网页还是图片，是视频还是音乐。浏览器并不靠URL来判断响应的内容，所以，
即使URL是http://example.com/abc.jpg，它也不一定就是图片。


Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发。当我们编写一个页面时，
我们只需要在HTTP请求中把HTML发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求图
片和视频，它会发送另一个HTTP请求，因此，一个HTTP请求只处理一个资源。

HTTP协议同时具备极强的扩展性，虽然浏览器请求的是http://www.sina.com.cn/的首页，但是新浪在
HTML中可以链入其他服务器的资源，比如:

<img src="http://i1.sinaimg.cn/home/2013/1008/U8455P30DT20131008135420.png">

从而将请求压力分散到各个服务器上，并且，一个站点可以链接到其他站点，无数个站点互相链接起来，
就形成了World Wide Web，简称WWW。

"""
__author__ = 'isenen'
