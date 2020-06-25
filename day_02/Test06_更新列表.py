a = [1, 2, 3, 2, 1]
a[1] = 10
print(a[1])  # 10
a[2] = 'hello'
print(a)  # [1, 10, 'hello', 2, 1]
print(type(a))  # <class 'list'>
print(type(a[1]))  # <class 'int'>
print(type(a[2]))  # <class 'str'>
"""
由上面的输出结果可知，可以对一个列表中的元素赋不同类型的值
"""

# 加入对列表赋值时使用的编号超过了列表中的最大编号，是否还可以赋值呢？答案是不可以
tring = [1, 2, 3]
# tring[3]='test'#错误：IndexError: list assignment index out of range
print("----------------------------------------------------")

# 增加元素
tring1 = [1, 2, 3]
tring1.append(4)
print(tring1)  # [1, 2, 3, 4]
tring1.append('test')
print(tring1)  # [1, 2, 3, 4, 'test']
s = ['a', 'b', 'c']
s.append(4)
print(s)  # ['a', 'b', 'c', 4]
print("------------------------------------------------------")

# 删除元素
tring2 = ['a', 'b', 'c', 'd', 'e']
print(len(tring2))  # 5
del tring2[1]
print(tring2)  # ['a', 'c', 'd', 'e']
print(len(tring2))  # 4
num = [1, 2, 3, 4]
del num[1]
print(len(num))  # 3
print("---------------------------------------------")

# 分片赋值
print(list('正道的光'))  # ['正', '道', '的', '光']
boil = list('正道的光')
print(boil)  # ['正', '道', '的', '光']
show = list('hi,boy')
print(show)  # ['h', 'i', ',', 'b', 'o', 'y']
show[3:] = list('man')
print(show)  # ['h', 'i', ',', 'm', 'a', 'n']
# list()函数可以直接将字符串转换为列表
greeting = list('hi')
print(greeting)  # ['h', 'i']
greeting[1:] = list('ello')
print(greeting)  # ['h', 'e', 'l', 'l', 'o']
# 分片赋值的另一个强大的功能就是 可以使用与原序列不等长的序列将分片替换
field = list('ae')
print(field)  # ['a', 'e']
field[1:1] = list('bcd')
print(field)  # ['a', 'b', 'c', 'd', 'e']
boil2 = list('正道的光')
boil2[3:3] = list('大太阳')
print(boil2)  # ['正', '道', '的', '大', '太', '阳', '光']
field=list('abcd')
print(field)#['a', 'b', 'c', 'd']
field[1:3]=[]
print(field)#['a', 'd']
boil3 = list('正道的大太阳光')
boil3[3:6]=[]
print(boil3)#['正', '道', '的', '光']
"""
通过上面示例可以看出，通过分片赋值删除元素也是可行的，
并且分片赋值删除的功能和del删除的操作结果时一样的。
"""
