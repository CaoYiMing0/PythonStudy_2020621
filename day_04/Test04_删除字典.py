dict = {'卢本伟': '1001', '五五开': '1002', 'white': '1003'}
print('删除前:', dict)  # 删除前: {'卢本伟': '1001', '五五开': '1002', 'white': '1003'}
del dict['卢本伟']
print('删除后：', dict)  # 删除后： {'五五开': '1002', 'white': '1003'}

# 除了删除键，还可以删除整个字典
dict2 = {'卢本伟': '1001', '五五开': '1002', 'white': '1003'}
print('删除前:', dict2)  # 删除前: {'卢本伟': '1001', '五五开': '1002', 'white': '1003'}
del dict2
print(dict2)  # 错误：NameError: name 'dict2' is not defined
