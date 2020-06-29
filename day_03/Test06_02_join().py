"""
join方法用于将序列中的元素以指定字符连接成一个新的字符串
语法如下：
    str.join(sequence)
str代表指定检索的字符串，sequence代表要连接的元素序列。
返回结果为指定字符连接序列中元素后生成的新字符串


"""

num = [1, 2, 3, 4]
mark = '+'
# mark.join(num)  # 错误：TypeError: sequence item 0: expected str instance, int found
# num.join(mark)#错误：AttributeError: 'list' object has no attribute 'join'
field = ['1', '2', '3', '4', '5']
print('连接字符串列表：', mark.join(field))  # 连接字符串列表： 1+2+3+4+5
# field.join(mark)  # AttributeError: 'list' object has no attribute 'join'
dirs = '', 'home', 'data', 'hdfs'
print('路径：', '/'.join(dirs))  # 路径： /home/data/hdfs
# 再写一个上面的示例
seq = ['hello', 'world', 'hello', 'china']
print(' '.join(seq))  # hello world hello china
"""
由输出结果看，进行join操作调用和被调用的对象必须都是字符串，任意一个不是字符串都会报错
"""
