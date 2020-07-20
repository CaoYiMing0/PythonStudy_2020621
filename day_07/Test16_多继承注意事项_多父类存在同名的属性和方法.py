"""
如果不同的父类存在同名的方法，子类对象在调用方法时，会调用哪一个父类中的方法呢？
开发时，应该尽量避免这种容易产生混淆的情况！--如果父类之间存在同名的属性和方法，
应该尽量避免使用多继承。
"""


class A:
    def test(self):
        print("A test 方法")

    def demo(self):
        print("A demo 方法")


class B:
    def test(self):
        print("B test 方法")

    def demo(self):
        print("B demo 方法")


class C(A, B):
    pass


c = C()
c.test()  # A test 方法
c.demo()  # A demo 方法


# 调整继承顺序
class D(A, B):
    pass


d = D()
d.test()  # A test 方法
d.demo()  # A demo 方法
