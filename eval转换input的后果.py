"""
__import__('os').system('ls')
等价代码：
import os
os.system("终端命令")
"""

input_str = input("请输入算术题：")
# 输入:__import__('os').system('ls')
print(eval(input_str))
"""
1
'ls' �����ڲ����ⲿ���Ҳ���ǿ����еĳ���
���������ļ���

Python3.7输出上面的内容，不是错误，也不是列表，
Python3.5输出的是列表，3.7可能改正了这个缺点吧
"""