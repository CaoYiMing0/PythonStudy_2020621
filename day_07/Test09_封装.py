class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "名字：%s，体重：%s" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 0.5


xiaoming = Person("xiaoming", 75)
xiaoming.eat()
xiaoming.run()
print(xiaoming)  # 名字：xiaoming，体重：75.0
xiaoming.eat()
print(xiaoming)  # 名字：xiaoming，体重：75.5
