"""
upper()方法用于将字符串中的小写字母转化为大写字母
upper()方法语法如下：
    str.upper()
该方法不需要参数，返回结果为转化后的字符串
"""

field = 'do it now'
print(field.upper())  # DO IT NOW
greeting = 'Hello,World'
print(greeting.upper())  # HELLO,WORLD
print('--------------------------------------')

"""
如果想要编写‘不区分大小写’的代码，就可以使用upper()方法。
如果想要在一个字符串中查找某个字符串并忽略大小写，也可以使用upper方法。
"""
field = 'do it now'
print(field.find('It'))  # -1
print(field.upper().find('It'))  # -1
print(field.upper().find('It'.upper()))  # 3
