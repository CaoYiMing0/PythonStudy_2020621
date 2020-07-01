"""
setdefault()方法和get()方法类似，用于获得与给定键相关联的值。
如果键不存在于字典中，就会添加键并将值设为默认值。
语法如下：
    dict.setfault(key,default=None)
dict代表指定的键值，key代表查找的键值，default代表键不存在时设置的默认键值
"""

zbc = {'卢本伟': '1001', '五五开': '1002', 'white': '1003'}
print(zbc.setdefault('giao'))  # None
print(zbc.setdefault('white'))  # 1003
print(zbc)  # {'卢本伟': '1001', '五五开': '1002', 'white': '1003', 'giao': None}
