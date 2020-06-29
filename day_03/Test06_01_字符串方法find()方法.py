"""
find()方法用于检测字符串中是否包含子字符串str。如果指定beg(开始)和end（结束）范围，
就检查是否包含在指定范围内。如果包含子字符串，就返回开始的索引值；否则返回-1。
方法如下：
    str.find(str,beg=0,end=len(string))
"""

field = 'do it now'
print(field.find('do'))  # 0
print(field.find('now'))  # 6
print(field.find('python'))  # -1
# 由输出结果可知，如果找到字符串，就返回对应的索引值；如果没找到字符串，就返回-1
print('----------------------------------------')

# 提供起点
print(field.find('it', 2))  # 3
# 提供起点
print(field.find('it', 5))  # -1
# 提供起点和终点
print(field.find('it', 0, 3))  # -1
print(field.find('it', 0, 5))  # 3
print(field.find('it', 5, 10))  # -1
