# 私有属性和私有方法在定义前增加两个下划线
class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def secret(self):
        print("%s的年龄是%s" % (self.name, self.__age))


xiaofang = Women("小芳")
# 私有属性，在外界不能够被访问
print(xiaofang.__age)  # 错误：AttributeError: 'Women' object has no attribute '__age'

"""
其实在Python中是没有真正意义上的私有属性和私有方法的。
可通过下面所示格式访问到：
访问私有变量：
对象名._类名__私有变量
访问私有方法：
对象名._类名__私有方法
"""
print(xiaofang._Women__age)  # 18
