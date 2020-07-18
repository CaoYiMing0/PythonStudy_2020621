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
        print("hahaha")

    def pa(self):
        print("pa")

