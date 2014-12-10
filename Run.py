__author__ = 'Administrator'
__haha__ = 'haha'


print __name__
print __haha__
print __debug__,__author__

def test():
    print "test1"

test()

def test():
    print "test2"

test()

a = {'a':'A','b':'B','c':'C'}
a.pop('a')
print a


if (1==1):
    xxx = 'testaaa';
print xxx


isensen = 1

def test2():
    global isensen
    isensen = 3
    print isensen
test2()
print isensen




