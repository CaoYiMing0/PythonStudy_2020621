x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y)  # True
print(x == z)  # True
print(x is y)  # True
print(x is z)  # False
"""
为什么最后输出的是False？
    这是因为is运算符用于判定同一性而不是相等性。变量x和y被绑定在同一个列表上，而
变量z被绑定在另一个具有相同数值和顺序的列表上。它们的值可能相等，却不是同一个对象。
    从内存的角度考虑，即它们所指向的内存空间不一样，x和y指向同一块内存空间，z指向另一块内存。
"""

x = [1, 2, 3]
y = [1, 5]
print(x is not y)  # True
del x[2]
print(x)  # [1, 2]
y[1] = 2
print(y)  # [1, 2]
print(x == y)  # True
print(x is y)  # False
# 总结：使用==运算符判定两个对象是否相等，使用is判定两个对象是否等同（是否为同一对象）
