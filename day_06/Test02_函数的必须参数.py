def paramone(str):
    print('the param is:', str)
    print('我是一个传入参数，我的值是：', str)


paramone('hello,world')  # 我是一个传入参数，我的值是： hello,world

# 不传入参数呢？
paramone()  # 出错：TypeError: paramone() missing 1 required positional argument: 'str'

# 输入超过一个参数呢
paramone('hello', 'world')  # 出错：ypeError: paramone() takes 1 positional argument but 2 were given
