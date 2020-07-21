"""
在Python中属性的获取存在一个向上查找机制
1.首先在对象内部查找对象属性 2.没有找到就会向上寻找类属性

因此，要访问类属性有两种方式：
    类名.类属性
    对象.类属性
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
tool3 = Tool("铁锹 ")

# 输出工具对象总数
print(Tool.count)  # 3
print("工具对象总数 %d" % tool3.count)  # 工具对象总数 3
