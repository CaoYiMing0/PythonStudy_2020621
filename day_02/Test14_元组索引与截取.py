# 因为元组也是一个序列，所以可以访问元组中指定位置的元素，也可以截取索引中的一段元素
field = ('hello', 'world', 'welcome')
print(field[2])  # welcome
print(field[-2])  # world
print(field[1:])  # ('world', 'welcome')
