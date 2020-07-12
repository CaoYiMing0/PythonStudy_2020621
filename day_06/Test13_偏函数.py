from functools import partial


def mod(n, m):
    return n % m


mod_by_100 = partial(mod, 100)
print("自定义函数，100对7取余结果为：", mod(100, 7))  # 自定义函数，100对7取余结果为： 2
print("调用偏函数，100对7取余结果为：", mod_by_100(7))  # 调用偏函数，100对7取余结果为： 2
# 使用偏函数所需代码量比自定义函数更少，更简洁
