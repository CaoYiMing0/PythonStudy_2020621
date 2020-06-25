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
#除了上面的索引方式
