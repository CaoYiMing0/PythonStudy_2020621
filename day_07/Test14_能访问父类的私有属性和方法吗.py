"""
在子类中不能访问父类的私有属性和私有方法，
但是可以通过继承的父类的方法访问父类的私有属性和方法
"""


class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def p(self):
        print(self.__num2)


class B(A):
    def demo(self):
        # 在子类方法中，不能访问父类的私有属性
        # print(self.__num2)
        # 不能调用父类的私有方法
        # self.__test()
        pass


# 创建一个子类对象
b = B()
b.p()
