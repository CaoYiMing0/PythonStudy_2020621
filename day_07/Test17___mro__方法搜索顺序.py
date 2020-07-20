"""
Python中针对类提供了一个内置属性__mro__可以查看方法搜索顺序
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


print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


# 调整继承顺序
class D(A, B):
    pass


print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
