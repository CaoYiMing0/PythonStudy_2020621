"""
子类可以拥有多个父类，并且具有所有父类的属性和方法
语法：
class 子类名(父类名1, 父类名2)
    pass
"""


class A:
    def test(self):
        print("A test 方法")


class B:
    def demo(self):
        print("B demo 方法")


class C(A, B):
    pass


# 创建子类对象
c = C()
c.test()  # A test 方法
c.demo()  # B demo 方法
