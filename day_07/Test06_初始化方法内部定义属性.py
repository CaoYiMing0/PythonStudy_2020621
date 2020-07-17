class Cat:
    def __init__(self):
        self.name = "Tom"


tom = Cat()
print(tom.name)  # Tom


# 使用参数设置属性初始值
class Cat2:
    def __init__(self, new_name):
        self.name = new_name
