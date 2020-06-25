number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number[1:3])  # 取索引值为1到2的元素
print(number[-3:-1])  # 取索引值为-3到-1的元素
print(number[7:100])  # [8, 9, 10]

print(number[-3:0])  # []
# 上面的输出有点奇怪，怎么能取得索引值为-1的元素呢，下面的输出可以成功
print(number[-3:])  # [8, 9, 10]
# 正数索引是否能用这种方式呢？答案是肯定的
print(number[0:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number[5:])  # [6, 7, 8, 9, 10]
print(number[:3])  # [1, 2, 3]
print(number[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 切片都是有步长的，没设置步长时，默认步长是1
print(number[0:10:1])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 设置步长为2
print(number[0:10:2])  # [1, 3, 5, 7, 9]
print(number[0:10:3])  # [1, 4, 7, 10]
print(number[2:6:3])  # [3, 6]
print(number[2:5:3])  # [3]
print(number[1:5:3])  # [2, 5]
# 除了上面的索引方式，还可设置前两个索引都为空
print(number[::3])  # [1, 4, 7, 10]
# 步长不可以为0
# print(number[::0])    错误：ValueError: slice step cannot be zero


"""
对于正数步长，Python会从序列的头部开始向右提取元素，直到最后一个元素；
对于负数步长，则是从序列的尾部开始向左提取元素，直到第一个元素。
正数步长必须让开始点小于结束点，而负数步长必须让开始点大于结束点。
"""
print(number[10:0:-2])  # [10, 8, 6, 4, 2]
print(number[0:10:-2])  # []
print(number[::-2])  # [10, 8, 6, 4, 2]
print(number[5::-2])  # [6, 4, 2]
print(number[:5:-2])  # [10, 8]
print(number[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(number[10:0:-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2]
print(number[10::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(number[2::-1])  # [3, 2, 1]
print(number[2:0:-1])  # [3, 2]
