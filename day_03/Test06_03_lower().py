"""
lower()方法用于将字符串中所有大写字符转换为小写
语法如下：
    str.lower()
该方法不需要参数，返回结果为转化后的字符串
"""

field = 'DO IT NOW'
print(field.lower())  # do it now
greeting = 'Hello,World'
print(greeting.lower())  # hello,world
print('-------------------------------------')

"""
如果想要编写‘不区分大小写’的代码，就可以使用lower()方法。
如果想要在一个字符串中查找某个字符串并忽略大小写，也可以使用lower方法。
"""
field = 'DO IT NOW'
print(field.find('It'))  # -1
print(field.lower().find('It'))  # -1
print(field.lower().find('It'.lower()))  # 3
