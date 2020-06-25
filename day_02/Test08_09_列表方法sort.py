# sort()方法用于对原列表进行排序，如果指定参数，就会使用该参数的方法进行排序
# list.sort(func)
num = [5, 8, 1, 3, 6]
num.sort()
print(num)  # [1, 3, 5, 6, 8]
num = [5, 8, 1, 3, 6]
n = num[:]
n.sort()
print(n)  # [1, 3, 5, 6, 8]
print(num)  # [5, 8, 1, 3, 6]

# sorted函数可以用于任何序列，返回结果都是一个列表
num = [5, 8, 1, 3, 6]
n = sorted(num)
print(n)  # [1, 3, 5, 6, 8]
