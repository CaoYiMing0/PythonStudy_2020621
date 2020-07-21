"""
需求：
1.在Dog类中封装方法game
    普通狗只是简单的玩耍
2.定义XiaoTianDog继承自Dog，并且重写game方法
    哮天犬需要在天上玩耍
3.定义Person类，并且封装一个和狗玩的方法
    在方法内部，直接让狗对象调用game方法
"""


class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍" % self.name)


class XioaTianQuan(Dog):
    def game(self):
        print("%s 飞到天上去玩耍" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))
        # 狗自己玩耍
        dog.game()


# 创建一个狗对象
wangcai = Dog("旺财")
# 创建一个小明对象
xiaoming = Person("小明")
# 小明调用方法
xiaoming.game_with_dog(wangcai)
"""
小明 和 旺财 快乐的玩耍
旺财 蹦蹦跳跳的玩耍
"""

# 创建一个哮天犬对象
xiao = XioaTianQuan("哮天犬")
# 创建一个小刚对象
xiaogang = Person("小刚")
# 小明调用方法
xiaogang.game_with_dog(xiao)
"""
小刚 和 哮天犬 快乐的玩耍
哮天犬 飞到天上去玩耍
"""
