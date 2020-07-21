"""
需求：
1 设计一个 Game 类
2 属性：
    定义一个类属性 top_score 记录游戏的历史最高分
    定义一个实例属性 player_name 记录当前游戏的玩家排名
3 方法
    静态方法 show_help 显示游戏帮助信息
    类方法 show_top_score 显示历史最高分
    实例方法 start_game 开始当前玩家的游戏
4 主程序步骤
    查看帮助信息
    查看历史最高分
    创建游戏对象，开始游戏
"""


class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏啦..." % self.player_name)


# 查看游戏帮助信息
Game.show_help()
# 查看历史最高分
Game.show_top_score()
# 创建游戏对象
gamer = Game("小明")
gamer.start_game()

"""
案例小结：
实例方法 -- 方法内部需要访问实例属性
类方法 -- 方法内部只需要访问类属性
静态方法 -- 方法内部，不需要访问实例属性和类属性


如果方法内部既需要访问实例属性，又需要访问类属性，应该定义实例方法
"""
