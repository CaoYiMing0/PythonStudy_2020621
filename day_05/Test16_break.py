# 在for循环中
for letter in 'hello':
    if letter == 'l':
        break
    print('当前字母：', letter)
"""
当前字母： h
当前字母： e
"""

# 在while循环中
num = 10
while num > 0:
    print('输出数字为：', num)
    num -= 1
    if num == 8:
        break
"""
输出数字为： 10
输出数字为： 9
"""