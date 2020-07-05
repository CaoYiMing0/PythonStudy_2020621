# Python中的pass是空语句，作用是保持程序结构的完整性
name = '无情哈拉少'
if name == '无情哈拉少':
    print('zbc')
elif name == '真呢到':
    # 预留，不做任何处理
else:
    print('nothing')
"""
上段代码出错：
D:\install\program\Anaconda\envs\PythonStudy_2020621\python.exe D:/Code/PythonStudy_2020621/day_05/Test19_pass语句.py
  File "D:/Code/PythonStudy_2020621/day_05/Test19_pass语句.py", line 7
    else:
       ^
IndentationError: expected an indented block
"""

# 上段代码出错，是因为程序中有空代码，在Python中空代码是非法的，解决办法就是添加个pass
name2 = '无情哈拉少'
if name2 == '无情哈拉少':
    print('zbc')
elif name2 == '真呢到':
    # 预留，不做任何处理
    pass
else:
    print('nothing')
# zbc
