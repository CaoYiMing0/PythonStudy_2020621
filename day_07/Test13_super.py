class Animal:
    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animal):
    def bark(self):
        print("wangwang")


class Teddy(Dog):
    def bark(self):
        # 针对子类特有的需求，编写代码
        print("hahaha")
        # 使用super().调用原本在父类中封装的方法
        super().bark()
        # 增加子类的其他代码
        print("dwadawdhuawdhiadhiawd")

    def pa(self):
        print("pa")


# creat a dog object, which can make two kinds of bark
wangcai = Teddy()
wangcai.bark()
"""
hahaha
wangwang
dwadawdhuawdhiadhiawd
"""


# super和类里面的其他代码有先后顺序吗？
class Akita(Dog):
    def bark(self):
        super().bark()
        print("八嘎")


akita = Akita()
akita.bark()
"""
wangwang
八嘎
"""


# 子类创建的对象，怎么在创建后访问父类的方法呢？
# 应该对子类另写一个方法，用来专门访问父类方法，但是这不利于维护
class Collie(Dog):
    def bark(self):
        print("呵呵呵")

    def fatherbark(self):
        super().bark()


collie = Collie()
collie.bark()  # 呵呵呵
collie.fatherbark()  # wangwang
