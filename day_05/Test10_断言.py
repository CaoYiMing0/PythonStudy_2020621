"""
在Python中，有一个和if语句工作方式非常相近的关键字，其工作方式类似如下伪代码：
if not condition:
    crash program
在Python中为什么需要这样的代码呢？
在没完善一个程序之前，我们不知道程序会在哪里出错，与其在运行时崩溃，不如在出现错误条件时
就崩溃。一般来说，可以要求一些条件必须为真。在Python中，assert关键字能实现这种工作方式。
"""

x = 3
assert x > 0, "x is not zero or negative"
assert x % 2 == 0, "x is not an even number"  # 提示x不是偶数
"""
第二行代码的错误提示如下：
Traceback (most recent call last):
  File "D:/Code/PythonStudy_2020621/day_05/Test10_断言.py", line 12, in <module>
    assert x % 2 == 0, "x is not an even number"  # 提示x不是偶数
AssertionError: x is not an even number
"""

"""
由上面的输出结果看到，当assert后面的条件为真时，程序正常运行；当assert后面的条件为假时，
输出错误信息。错误的提示信息有我们自己定义，这个错误提示信息可以称为异常参数。
"""
