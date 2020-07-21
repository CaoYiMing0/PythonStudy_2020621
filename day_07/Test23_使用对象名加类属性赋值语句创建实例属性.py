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

# 下面一条语句执行后，内存会为实例申请一个count属性
tool3.count = 99
print("工具对象总数 %d" % tool3.count)  # 工具对象总数 99
print("Tool类的count值 %d" % Tool.count)  # Tool类的count值 3
