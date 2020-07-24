"""
Python的解释器在导入模块时，会：
    1.搜索当前目录指定模块名的文件，如果有就直接导入
    2.如果没有，再搜索系统目录
在开发时，给文件起名，不要和系统的模块文件重名
Python中每一个模块都有一个内置属性__file__可以查看模块的完整路径
示例：
    import random
    #生成一个0~10的数字
    rand = random.randint(0,10)
    print(rand)
注意：如果当前目录下，存在一个random.py的文件，程序就无法正常执行了
这个时候，Python的解释器会加载当前目录下的random.py而不会加载系统的random
"""
import random

print(random.__file__)  # D:\install\program\Anaconda\envs\PythonStudy_2020621\lib\random.py
