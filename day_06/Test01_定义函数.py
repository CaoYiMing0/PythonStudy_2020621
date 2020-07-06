"""
Python定义函数使用def关键字，一般格式如下：
def 函数名（参数列表）:
    函数体
"""


def hello():
    print('hello,world')


hello()
"""
需要注意以下几点：
    （1）没有return语句时，函数执行完毕也会返回结果，不过结果为None
    （2）return None可以简写为return
    （3）在Python中定义函数时，需要保持函数体中同一层级的代码缩进一致
"""


# 定义一个什么都不做的语句，可以用pass
def donothing():
    pass


donothing()
