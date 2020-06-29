"""
split方法通过指定分隔符对字符串进行切片，如果参数num有指定值，就只分隔num个字符串
方法如下:
    str.split(st='',num=string.count(str))
str代表指定检索的字符串；st代表分隔符，默认为空格；num代表分割次数。
返回结果为分割后的字符串列表。
"""

field = 'do it now'
print(field.split())  # ['do', 'it', 'now']
print(field.split('i'))  # ['do ', 't now']
print(field.split('o'))  # ['d', ' it n', 'w']
print(field.split('o', 1))  # ['d', ' it now']
# 如果不提供分隔符，程序就会把所有空格作为分割符
