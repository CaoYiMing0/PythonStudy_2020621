"""
单例 -- 让类创建的对象，在系统中只有唯一的一个实例
    1.定义一个类属性，初始值是None，用于记录单例对象的引用
    2.重写__new__方法
    3.如果类属性 is None，调用父类方法分配空间，并在类属性中记录结果
    4.返回类属性中记录的对象引用

"""


class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3.返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 1.判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return

        # 2.如果没有执行过，在执行初始化动作
        print("初始化播放器")
        # 3.修改类属性的标记
        MusicPlayer.init_flag = True


# 创建多个对象
player1 = MusicPlayer()  # 初始化播放器
print(player1)  # <__main__.MusicPlayer object at 0x00000204731D2F88>

player2 = MusicPlayer()  # 此处没有输出
print(player2)  # <__main__.MusicPlayer object at 0x00000204731D2F88>
