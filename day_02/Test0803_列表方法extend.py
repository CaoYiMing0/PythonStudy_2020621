# extend()方法用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 两列表：list、seq    list.extend(seq)
a = ['hello', 'world']
b = ['python', 'is', 'funny']
a.extend(b)
print(a)  # ['hello', 'world', 'python', 'is', 'funny']
a = ['hello', 'world']
b = ['python', 'is', 'funny']
print(a + b)  # ['hello', 'world', 'python', 'is', 'funny']
print(a)  # ['hello', 'world']
"""
从输出结果看，两个示例中a和b的赋值时一样的，但第一个示例中输出a的值
和第二个示例中输出的a的值不一样。
extend()方法修改了被扩展的序列，如前面的a；原始的连接操作会返回一个全新的列表，
如上面的示例，返回的时一个包含a和b副本的新列表，而不修改原始的变量。
"""

# 上述示例也可以用切片赋值来实现相同的结果,不过看起来没有extend易懂
a = ['hello', 'world']
b = ['python', 'is', 'funny']
a[len(a):] = b
print(a)  # ['hello', 'world', 'python', 'is', 'funny']
