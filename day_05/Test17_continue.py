# 在for循环中
for letter in 'hello':
    if letter == 'l':
        continue
    print('当前字母：', letter)
"""
当前字母： h
当前字母： e
当前字母： o
"""

# 在while中
num = 3
while num > 0:
    num -= 1
    if num == 2:
        continue
    print('当前变量值：', num)
"""
当前变量值： 1
当前变量值： 0
"""