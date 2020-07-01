"""
formkeys()方法用于创建一个新字典，以序列seq中的元素做字典的键，value为字典所
有键对应的初始值。
语法如下：
    dict.formkeys(seq[,value])
dict代表指定字典；seq代表字典键值列表；value代表可选参数，设置键序列(seq)的值。
该方法返回结果为列表。
"""

seq = ('name', 'age', 'sex')
info = dict.fromkeys(seq)
print(info)  # {'name': None, 'age': None, 'sex': None}
info = dict.fromkeys(seq, 10)
print(info)  # {'name': 10, 'age': 10, 'sex': 10}
