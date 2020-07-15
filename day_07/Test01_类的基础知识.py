"""
设计一个类，需要满足以下三个要素：
    1.类名满足大驼峰命名法 CapWords
        每一个单词的首字母大写
        单词与单词之间没有下划线
    2.属性
    3.方法

在Python中对象几乎是无所不在，变量、数据、函数都是对象
"""

# 使用dir内置函数传入标识符/数据，可以查看对象内的所有属性及方法
a = 1


def demo():
    """dir测试函数"""
    print("hello dir")


print(dir(
    a))  # ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
print(dir(
    demo))  # ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# _方法名_格式的方法是Python提供的内置方法/属性
# _doc_就可以查看一个函数的说明文档，也就是注释
print(demo.__doc__)  # dir测试函数

"""
在Python中定义一个只包含方法的类，语法格式如下：
class 类名：
    def 方法1(self,参数列表):
        pass
    def 方法2(self,参数列表):
        pass
方法的定义格式和之前学习过的函数几乎一模一样，区别在于第一个参数必须是self
"""


# 需求：小猫爱吃鱼，小猫要喝水
class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
tom.eat()  # 小猫爱吃鱼
tom.drink()  # 小猫要喝水
