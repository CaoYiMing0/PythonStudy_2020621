"""
在Python中，当一个对象被从内存中销毁前，会自动调用__del__方法。
应用场景：
    __del__如果希望在对象被销毁前，再做一些事情，可以考虑一下__del__方法
"""


class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s来了" % self.name)

    def __del__(self):
        print("%s去了" % self.name)


tom = Cat("Tom")
print(tom.name)
print("-" * 10)
"""
输出结果：
Tom来了
Tom
----------
Tom去了
"""
