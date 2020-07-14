class MyClass(object):
    i = 123

    def f(self):
        return "Hello world!"


use_class = MyClass()
print("调用类的属性：", use_class.i)  # 调用类的属性： 123
print("调用类的方法：", use_class.f())  # 调用类的方法： Hello world!"
"""
use_class = MyClass()这步叫做类的实例化。

    在上面的示例中，在类中定义f()方法时带了一个self参数，该参数在方法中并没有被调用，是否可以不要呢？
调用f()方法时没有传递参数，是否表示参数可以传递也可以不传递？
    对于在类中定义方法的要求：在类中定义方法时，第一个参数必须是self。除第一个参数外，类的方法和普通函数
没什么区别，如可以用默认参数、可变参数、关键字参数和命名关键字参数。
"""


class MyClass2(object):
    i = 123

    def f2(self):
        return "Hello world!"


class2 = MyClass2()
print(class2.i)
print(class2.f2())


class MyClass3(object):
    i = 123

    def f3(self, name):
        return "Hello world!"


class3 = MyClass3()
print(class3.i)
print(class3.f3(1))  # 不出错
print(class3.f3(1, 2))  # TypeError: f3() takes 2 positional arguments but 3 were given
print(class3.f3())  # TypeError: f3() missing 1 required positional argument: 'name'
