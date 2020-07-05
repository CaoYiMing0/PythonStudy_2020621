"""
reversed和sorted这两个函数可作用于任何序列和可迭代对象，
但不是原地修改对象，而是返回翻转或排序后的版本。
"""

print(sorted([5, 3, 7, 1]))  # [1, 3, 5, 7]
a = [5, 3, 7, 2]
b = a
a[3] = 10
print(a == b)  # True
print(a is b)  # True
c = sorted(a)
print(c == a)  # False
print(a is c)  # False
print(a)  # [5, 3, 7, 10]
a.sort()
print(a)  # [3, 5, 7, 10]
print(a == b)  # True
print(sorted('hello,world!'))  # ['!', ',', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print(list(reversed('hello,world!')))  # ['!', 'd', 'l', 'r', 'o', 'w', ',', 'o', 'l', 'l', 'e', 'h']
print(''.join(reversed('hello,world!')))  # !dlrow,olleh
