"""
应用场景：
    在开发中，除了代码执行出错Python解释器会抛出异常之外
    还可以根据应用程序特有的业务需求主动抛出异常
示例：
    输入密码函数提示用户输入密码，如果长度少于8，抛出异常


在Python中提供了一个Exception异常类
在开发时，如果满足特定业务需求时，希望抛出异常，可以：
    1.创建一个Exception的对象
    2.使用raise关键字抛出异常对象
需求：
    定义input_password函数，提示用户输入密码
    如果用户输入长度<8,抛出异常
    如果用户输入长度>=8，返回输入的密码
"""


def input_password():
    pwd = input("请输入密码：")
    if len(pwd) >= 8:
        return pwd
    print("主动抛出异常")
    ex = Exception("密码长度不够")
    # 2>主动抛出异常
    raise ex


try:
    print(input_password())
except Exception as result:
    print(result)
