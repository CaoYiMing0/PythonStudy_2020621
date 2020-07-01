"""
get()方法返回指定键的值，如果值不在字典中，就返回默认值。
语法如下：
    dict.get(key,default=None)
dict代表指定字典，key代表字典中要查找的键，default代表指定键的值不存在时
返回默认值。该方法返回结果为指定键的值，如果值不在字典中，就返回默认值None。
"""

zhubo = {'卢本伟': '1001', '五五开': '1002', 'white': '1003'}
print(zhubo.get('white'))  # 1003
zbc = {}
# print(zbc['white'])  # 错误：KeyError: 'white'
print('%s' % zbc.get('white'))  # None

zbc = {}
print(zbc.get('white', '未指定'))  # 未指定
# 由输出结果看，输出结果中用”未指定“代替了None
