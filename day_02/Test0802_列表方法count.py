# count()方法用于统计某个元素在列表中出现的次数
field = list('hello,world')
print(field.count('o'))  # 2
listobj = [123, 'hello', 'world', 123]
print(listobj.count(123))  # 2
print(listobj.count(1))  # 0
print(['a', 'c', 'a', 'f', 'a'].count('a'))  # 3
mix = [[1, 3], 5, 6, [1, 3], 2]
print(mix.count([1, 3]))  # 2
print(mix.count(2))  # 1
