"""
类属性就是给类对象中定义的属性
通常用来记录与这个类相关的特征
类属性不会用于记录具体对象的特征
"""
"""
示例需求：
定义一个工具类
每件工具都有自己的name 
需求 -- 知道使用这个类，创建了多少个工具对象啥
"""


class Tool(object):
    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name
        # 针对类属性做一个计数+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")

# 输出工具对象总数
print(Tool.count)  # 2

tool3 = Tool("铁锹 ")

# 输出工具对象总数
print(Tool.count)  # 3
