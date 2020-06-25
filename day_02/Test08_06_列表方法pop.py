# pop()方法用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.pop(obj=list[-1])
field = ['hello', 'world', 'python', 'is', 'funny']
field.pop()
print(field)  # ['hello', 'world', 'python', 'is']
field.pop(3)
print(field)  # ['hello', 'world', 'python']
field.pop(0)
print(field)  # ['world', 'python']
print(field.pop())  # python
# pop方法时唯一一个既能修改列表 又能返回元素值（去了None）的列表方法

