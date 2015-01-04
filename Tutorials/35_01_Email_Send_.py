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


SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
Python对SMTP支持有smtplib和email两个模块:
1) email负责构造邮件
2) smtplib负责发送邮件。
"""
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

__author__ = 'isenen'

# ------------------------------------发送文本邮件---------------------------

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 输入Email地址和口令:
from_addr = raw_input('From: ')
password = raw_input('Password: ')
# 输入SMTP服务器地址:
smtp_server = raw_input('SMTP server: ')
# 输入收件人地址:
to_addr = raw_input('To: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()



"""
按上面代码执行后,仔细观察，发现如下问题：
1) 邮件没有主题；
2) 收件人的名字没有显示为友好的名字，比如Mr Green <green@example.com>；
3) 明明收到了邮件，却提示不在收件人中。

这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在
发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整
的邮件：
"""

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = raw_input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()





# ------------------------------------发送HTML邮件---------------------------
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
pass




# ------------------------------------发送附件-------------------------------
"""
如果Email中要加上附件怎么办？带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正
文，再继续往里面加上表示附件的MIMEBase对象即可
"""
# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/R/1.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='1.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='1.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)



# ------------------------------------发送图片-------------------------------
"""
如果要把一个图片嵌入到邮件正文中怎么做？直接在HTML邮件中链接图片地址行不行？
答案是，大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。
要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，
在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，
然后引用不同的cid:x即可。
"""
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))


# -----------------------------------同时支持HTML和Plain格式------------------
"""
如果我们发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，但
是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？

办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级
查看纯文本邮件。

利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative
"""
msg = MIMEMultipart('alternative')
msg['From'] = raw_input()
msg['To'] = raw_input()
msg['Subject'] = raw_input()

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
# 正常发送msg对象...




# ----------------------------加密SMTP-------------------------------------
"""
使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更
安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安
全SMTP发送邮件。

必须知道，Gmail的SMTP端口是587，因此，修改代码如下：
"""
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
#只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。
server.starttls()
# 剩下的代码和前面的一模一样:
server.set_debuglevel(1)



