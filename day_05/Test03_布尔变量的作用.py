"""
下面的值在作为布尔表达式时，会被解释器看作假（false）:
    False   None    0   ""  ()  []  {}
换句话说，标准值False和None、所有类型的数字0（包括浮点型、长整型和其他类型）、
空序列（如空字符串、空元组和空列表）以及空字典都为假。其他值都为真，包括原生的布尔值True。
"""
# 在Python中，True和1等价，False和0等价
print(True)  # True
print(False)  # False
print(True == 1)  # True
print(False == 0)  # True
print(True + False + 2)  # 3

# bool函数可以用来转换其他值
print(bool('good good study'))  # True
print(bool(''))  # False
print(bool(3))  # True
print(bool(0))  # False
print(bool([1]))  # True
print(bool([]))  # False
print(bool())  # False
