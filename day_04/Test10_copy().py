"""
copy()方法返回一个具有相同键/值对的新字典。这个方法是浅复制（shallow copy），
因为值本身是相同的，而不是副本。
语法如下：
    dict.copy()
"""

zhubo = {'卢本伟': '1001', '五五开': '1002', 'white': '1003', '五五开': '1009'}
z2 = zhubo.copy()
print(z2)  # {'卢本伟': '1001', '五五开': '1009', 'white': '1003'}

# 通过下面的示例可了解什么是浅复制
student = {'小智': '1002', 'info': ['小张', '1006', 'man']}
st = student.copy()
print(st['小智'])  # 1002
# 更改小智的值
st['小智'] = '1005'
print(st)  # {'小智': '1005', 'info': ['小张', '1006', 'man']}
print(student)  # {'小智': '1002', 'info': ['小张', '1006', 'man']}
st['info'].remove('man')
print(st)  # {'小智': '1005', 'info': ['小张', '1006']}
print(student)  # {'小智': '1002', 'info': ['小张', '1006']}
"""
由输出结果看，替换副本的值时原始字典不受影响。如果修改了某个值（原地修改，不是替换），
原始字典就会改变，因为同样的值也在字典中。以这种方式进行复制就是浅复制。
而使用深复制（deep copy）可以避免该问题。
"""
