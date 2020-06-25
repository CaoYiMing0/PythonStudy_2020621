# 为了检查一个值是否在序列中，Python为我们提供了in运算符。
greeting = 'hello,world'
print('w' in greeting)  # True
print('a' in greeting)  # False

users = ['卢本伟', 'White', '五五开']
print('White' in users)  # True
print('伞兵一号' in users)  # False

numbers = [1, 2, 3, 4, 5]
print(1 in numbers)  # True
print(6 in numbers)  # False

eng = '**Study python is so happy!**'
print('**' in eng)  # True
print('$' in eng)  # False

print('----------------------------')
print('a' in numbers) #False
print('3' in greeting) # False
"""
上面两个在3.7版本中没有报错
但是在3.5中，第二个报错了
在3.5中：
    数字类型不能在字符串类型中通过in进行成员资格检测，
    而字符串类型可以在数字列表中通过in进行成员资格检测
"""

