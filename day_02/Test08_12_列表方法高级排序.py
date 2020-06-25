"""
如果希望元素能按特定方式进行排序（不是sort方法默认的按升序排列元素），
就可以自定义比较方法。
sort有两个可选参数，即key和reverse。要使用它们，就要通过名字指定，
我们称之为关键字参数。
"""
field = ['hello', 'world', 'python', 'is', 'funny']
field.sort(key=len)  # 按字符串由短到长排序
print(field)  # ['is', 'hello', 'world', 'funny', 'python']
field.sort(key=len, reverse=True)  # 按字符串由长到短排序，传递两个参数
print(field)  # ['python', 'hello', 'world', 'funny', 'is']

num = [5, 8, 1, 3, 6]
num.sort(reverse=True)  # 排序后逆序
print(num)  # [8, 6, 5, 3, 1]
