"""
概念
    ·包是一个 包含多个模块 的 特殊目录
    ·目录下有一个特殊的文件__init__.py
    ·包名的命名方式和变量名一致，小写字母+_
好处
    ·使用 import包名 可以一次性导入 包 中 所有的模块

__init__.py
    要在外界使用 包 中的模块，需要在__init__.py中指定对外界提供的模块李彪
"""
import message

message.send_message.send("hello")
txt = message.receive_message.receive()
print(txt)
