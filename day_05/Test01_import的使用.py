"""
import的标准语法如下：
    import module1[,module2[,...moduleN]]
表示允许一个import导入多个模块，但各个模块间需要用逗号隔开。

当我们使用import语句时，Python解释器怎样找到对应的文件呢？这涉及Python的搜索路径，
搜索路径由一系列目录名组成，Python解释器会依次从这些目录中寻找引入的模块。看起来很像环境变量，
事实上可以通过定义环境变量的方式确定搜索路径。搜索路径是在Python编译或安装时确定的，被存储在
sys模块的path变量中。
"""

import sys

print('Python的搜索路径为：%s' % sys.path)  #
"""
Python的搜索路径为：['D:\\Code\\PythonStudy_2020621\\day_05', 
'D:\\Code\\PythonStudy_2020621', 
'D:\\install\\program\\PyCharm 2019.3.3\\plugins\\python\\helpers\\pycharm_display', 
'D:\\install\\program\\Anaconda\\envs\\PythonStudy_2020621\\python37.zip', 
'D:\\install\\program\\Anaconda\\envs\\PythonStudy_2020621\\DLLs', 
'D:\\install\\program\\Anaconda\\envs\\PythonStudy_2020621\\lib', 
'D:\\install\\program\\Anaconda\\envs\\PythonStudy_2020621', 
'D:\\install\\program\\Anaconda\\envs\\PythonStudy_2020621\\lib\\site-packages', 
'D:\\install\\program\\PyCharm 2019.3.3\\plugins\\python\\helpers\\pycharm_matplotlib_backend']
"""

# from math import pi语句就是从math模块中导入pi到当前命名空间，该语句不会将math整个模块导入
from math import pi

print(pi)  # 3.141592653589793
"""
如果把上面的示例写成下面这样
import math 
print(pi)  # 会出错 NameError: name 'pi' is not defined
由上面的输出结果可知，如果在导入math模块时访问pi对象，需要使用math.pi，直接使用
pi访问不了，会报错。
"""

# 使用多个模块
from math import sin, cos
# 如果访问的模块很多，可以写成如下形式，pi可以直接使用
from math import *
# 还可以为模块取别名
import math as m
from math import pi as p
