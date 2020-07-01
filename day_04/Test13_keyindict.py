"""
在字典中，in操作符用于判断键是否存在于字典中，如果键在字典dict中就返回true,否则返回false
语法如下：
    key in dict
dict代表字典，key代表在字典中查找的键。
"""

zbc = {'卢本伟': '1001', '五五开': '1002', 'white': '1003'}
print('white' in zbc)  # True
print('无情哈拉少' in zbc)  # False
