class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
# 再创建一个猫对象
lazy_tom = Cat()
# 输出引用地址
print(tom)  # <__main__.Cat object at 0x0000013CC7582EC8>
print(lazy_tom)  # <__main__.Cat object at 0x0000013CC7582F48>

lazy_tom2 = lazy_tom
print(lazy_tom2)  # <__main__.Cat object at 0x0000021AE5D82F88>
