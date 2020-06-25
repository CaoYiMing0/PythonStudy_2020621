"""
tuple函数的功能和list函数基本上一样，都是以一个序列作为参数，并把它转换为元组。
如果参数是元组，参数就会被原样返回
"""
print(tuple(['hello', 'world']))  # ('hello', 'world')
print(tuple('hello'))  # ('h', 'e', 'l', 'l', 'o')
print(tuple(('hello', 'world')))  # ('hello', 'world')
