# 哪一个对象调用的方法，self就是哪一个对象的引用
class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")

    def printself(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print(self)


tom = Cat()
print(tom)  # <__main__.Cat object at 0x0000024164592048>
tom.printself()  # <__main__.Cat object at 0x0000024164592048>


# 在类中的方法使用类的变量，可以使用self.变量名
class Dog:
    def eat(self):
        print("%s爱吃骨头" % self.name)


kugou = Dog()
kugou.name = "酷狗"
kugou.eat()
