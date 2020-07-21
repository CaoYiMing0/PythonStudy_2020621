"""
类方法就是针对类对象定义的方法
    在类方法内部可以直接访问类属性或者调用其他的类方法
语法如下
@classmethod
def 类方法名(cls):
    pass
类方法需要修饰器@classmethod来标识，告诉解释器这是一个类方法
类方法的第一个参数应该是cls
    由哪一个类调用的方法，方法内的cls就是哪一个类的引用
    这个参数和实例方法的第一个参数是self类似
    提示使用其他名称也可以，不过习惯使用cls
通过 类名. 调用类方法，调用方法时，不需要传递cls参数
在方法内部
    可以通过 cls. 访问类的属性
    也可以通过 cls. 调用其他的类方法

"""
"""
示例需求：
    定义一个工具类
    每件工具都有自己的name
    需求 -- 在类封装一个show_tool_count的类方法，输出使用当前这个类，创建的对象个数
"""


class Tool(object):
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
# 调用类方法
Tool.show_tool_count()  # 工具对象的数量 1
