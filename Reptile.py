__author__ = 'Administrator'
import urllib

content =  urllib.urlopen('http://www.hoopchina.com').read()
s1 = 0
while s1>=0:
    begin = content.find(r'<a',s1)
    m1 = content.find(r'href=',begin)
    m2  = content.find(r'>',m1)
    if(content[m1:m2].find(r'.html')!=-1):
        m2 = content.find(r'.html',m1)
        url = content[m1+6:m2+5]
        print url
    s1 = m2