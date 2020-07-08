"""
调用函数时，如果没有传递参数，就会使用默认参数
使用默认参数，就是在定义函数时，给参数一个默认值。如果没有给调用的函数的参数
赋值，调用的函数就会使用这个默认值。
"""


def defaultparam(name, age=23):
    print('hi，我叫：', name)
    print('我今年：', age)
    return


defaultparam('小萌')
"""
hi，我叫： 小萌
我今年： 23
"""

# 上例函数调用时没有对age赋值，在输出结果中使用了函数定义时的默认值
defaultparam('小萌', 21)
"""
hi，我叫： 小萌
我今年： 21
"""


# 默认参数的位置有要求吗？把默认参数放在前面行不行？
def defaultparam1(age=23, name):
    print('hi，我叫：', name)
    print('我今年：', age)
    return


"""
默认参数得放在后面，放前面会出现如下提示错误
SyntaxError: non-default argument follows default argument
"""


def defaultparam2(name, age=23, addr='shanghai'):
    print('hi，我叫：', name)
    print('我今年：', age)
    print('我现在在：', addr)
    return


print('------传入必须参数------')
defaultparam2('小萌')
print('------传入必须参数，更改第一个默认参数值------')
defaultparam2('小萌', 21)
print('------传入必须参数，默认参数值都更改------')
defaultparam2('小萌', 21, 'beijing')
print('------传入必须参数，指定默认参数名并更改参数值------')
defaultparam2('小萌', addr='beijing')
print('------传入必须参数，指定参数名并更改值------')
defaultparam2('小萌', addr='beijing', age=23)
print('------第一个默认参数不带参数名，第二个带------')
defaultparam2('小萌', 21, addr='beijing')
print('------两个默认参数都带参数名------')
defaultparam2('小萌', age=23, addr='beijing')
print('------第一个默认参数带参数名，第二个不带，报错------')
defaultparam2('小萌', age=23, 'beijing')
"""
------传入必须参数------
hi，我叫： 小萌
我今年： 23
我现在在： shanghai
------传入必须参数，更改第一个默认参数值------
hi，我叫： 小萌
我今年： 21
我现在在： shanghai
------传入必须参数，默认参数值都更改------
hi，我叫： 小萌
我今年： 21
我现在在： beijing
------传入必须参数，指定默认参数名并更改参数值------
hi，我叫： 小萌
我今年： 23
我现在在： beijing
------传入必须参数，指定参数名并更改值------
hi，我叫： 小萌
我今年： 23
我现在在： beijing
------第一个默认参数不带参数名，第二个带------
hi，我叫： 小萌
我今年： 21
我现在在： beijing
------两个默认参数都带参数名------
hi，我叫： 小萌
我今年： 23
我现在在： beijing
------第一个默认参数带参数名，第二个不带，报错------
最后一个错误：SyntaxError: positional argument follows keyword argument
"""

"""
以上输出结果发现：
（1）无论有多少默认值，默认参数都不能在必须参数之前
（2）无论有多少默认参数，若不传入默认参数值，则使用默认值
（3）若要更改某一个默认参数值，又不想传入其他默认参数，且该默认参数的位置不是第一个，则
    可以通过参数名更改想要更改的默认参数值
（4）若有一个默认参数通过传入参数名更改参数值，则其他想要更改的默认参数都需要传入参数名
    更改参数值，否则报错
（5）更改默认参数值时，传入默认参数的顺序不需要根据定义的函数中的默认参数的顺序传入，不过最好同时
    传入参数名，否则容易出现执行结果与预期不一致的情况
"""
