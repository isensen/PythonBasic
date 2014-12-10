#coding=utf-8
import os, time

print 'Current dir is %s'% os.getcwd()

start = time.time()


os.system('ipconfig -all')

print 'time consuming', time.time() - start
print input('...')
