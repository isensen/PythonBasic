#coding=utf-8
'''
Python之所以自称“batteries included”，就是因为内置了许多非常有用的模块，无需额外安装和配置，即可直接使用。
'''
__author__ = 'isenen'


#--------------------------[collections]-----------------------------
# collections是Python内建的一个集合模块，提供了许多有用的集合类
# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
p = (1, 2)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
# 定义一个class又小题大做了，这时，namedtuple就派上了用场：

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x, p.y, isinstance(p, Point), isinstance(p, tuple)



#---------------------------[deque]----------------------------------
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，
# 数据量大的时候，插入和删除效率很低。

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q



#---------------------------[defaultdict]------------------------------
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
dd['key1'] # key1存在
dd['key2']



#---------------------------[OrderedDict]------------------------------
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d # dict的Key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od # OrderedDict的Key是有序的


#----------------------------[Counter]----------------------------------
# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print c