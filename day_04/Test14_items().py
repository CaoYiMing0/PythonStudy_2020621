"""
items()方法以列表返回可遍历的（键，值）元组数组。
语法如下：
    dict.items()
dict代表指定字典，该方法不需要参数，返回结果为可遍历的（键/值）元组数组。
"""

zbc = {'卢本伟': '1001', '五五开': '1002', 'white': '1003'}
print(zbc.items())  # dict_items([('卢本伟', '1001'), ('五五开', '1002'), ('white', '1003')])
