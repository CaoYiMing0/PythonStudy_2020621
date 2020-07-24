# is：判断两个标识符是否引用自一个对象
# is not：用于判断两个标识符是否引用自不同对象
a = 10
b = 10
print(a is b)
print(a is not b)
b = 20
print(a is b)
print(a is not b)
