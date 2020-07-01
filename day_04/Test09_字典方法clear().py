"""
clear()方法用于删除字典内的所有项
语法如下：
    dict.clear()
"""

zhubo = {'卢本伟': '1001', '五五开': '1002', 'white': '1003', '五五开': '1009'}
print('%d个' % len(zhubo))  # 3个
zhubo.clear()
print('%d个' % len(zhubo))  # 0个
print(zhubo)  # {}
