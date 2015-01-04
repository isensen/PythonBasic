#coding=utf-8
"""
MUA：Mail User Agent——邮件用户代理
MTA：Mail Transfer Agent——邮件传输代理
MDA：Mail Delivery Agent——邮件投递代理

--------------------------------------------------------------
发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人
--------------------------------------------------------------

有了上述基本概念，要编写程序来发送和接收邮件，本质上就是：

1. 编写MUA把邮件发到MTA；
2. 编写MUA从MDA上收邮件。


发邮件: MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面的MTA到
另一个MTA也是用SMTP协议。

收邮件: MUA和MDA使用的协议有两种：
1) POP：Post Office Protocol，目前版本是3，俗称 POP3；
2) IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还
   可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。

"""
__author__ = 'isenen'


