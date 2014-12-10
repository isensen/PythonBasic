#coding=utf-8
'''
    连接到数据库
    打开游标Cursor
    通过Cursor执行SQL语句
'''
import sqlite3

__author__ = 'isenen'
#导入SQLite驱动
#数据库文件是test.db
#如果文件不存在,会自动在当前目录创建


conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('drop table user ')

cursor.execute('create table user(id varchar(20) primary key , name varchar(20))')

cursor.execute('insert into user (id,name) values (\'1\',\'isensen\')')

print cursor.rowcount

cursor.execute('select * from user where id =?', '1')

values = cursor.fetchall()

print values


cursor.close()

conn.close()
#================================查询==========================================

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('select * from user where id =?', '1')

values = cursor.fetchall()

print values #这里搞不懂了,为什么这里输出 是 [] 空的???关闭再重新连接就查不着了

cursor.close()

conn.close()
