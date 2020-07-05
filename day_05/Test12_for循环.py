"""
语法格式如下：
for iterating_var in sequence:
    statements(s)
sequence是任意序列，iterating_var是序列中需要遍历的元素。statements是待执行的语句块
"""

fields = ['a', 'b', 'c']
for f in fields:
    print('当前字母是：', f)

print('-----for循环字符串-----')
for letter in 'good':
    print('当前字母：', letter)

print('-----for循环数字序列-----')
number = [1, 2, 3]
for num in number:
    print('当前数字：', num)

print('-----for循环字典-----')
tups = {'卢本伟': '1001', '五五开': '1002', 'white': '1003'}
for tup in tups:
    print('%s:%s' % (tup, tups[tup]))

"""
当前字母是： a
当前字母是： b
当前字母是： c
-----for循环字符串-----
当前字母： g
当前字母： o
当前字母： o
当前字母： d
-----for循环数字序列-----
当前数字： 1
当前数字： 2
当前数字： 3
-----for循环字典-----
卢本伟:1001
五五开:1002
white:1003
"""