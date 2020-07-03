x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3
x, y, z = 1, 2, 3
x, y = y, x
print(x, y, z)  # 2 1 3
"""
在Python中，交换所做的事情叫做序列解包或可选迭代解包，即将多个值的序列解开，
然后放到变量序列中。
"""
nums = 1, 2, 3
print(nums)  # (1, 2, 3)
print(type(nums))  # <class 'tuple'>
x, y, z = nums
print(x)  # 1
print(x, y, z)  # 1 2 3
# 由输出结果看到，序列解包后，变量获得了对应的值

zbc = zbc = {'卢本伟': '1001', '五五开': '1002', 'white': '1003'}
key, value = zbc.popitem()
print(key)  # white
print(value)  # 1003
# 由输出知，此处作用于元组，使用popitem方法将键-值作为元组返回，返回的元组可以直接赋值到两个变量中

"""
序列解包允许函数返回一个以上的值并打包成元组，然后通过一个赋值语句进行访问。
有一点要注意，解包序列中的元素数量必须和放置在赋值符号"="左边的数量完全一致，
否则Python会在赋值时引发异常
"""
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3
x, y, z = 1, 2  # 错误：ValueError: not enough values to unpack (expected 3, got 2)
