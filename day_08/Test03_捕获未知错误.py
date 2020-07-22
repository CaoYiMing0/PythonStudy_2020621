"""
在开发时，要预判到所有可能出现的错误，还是有一定难度的
如果希望程序无论出现任何错误，都不会因为Python解释器抛出异常而被终止，可以再增加一个except
语法如下：
except Exception as result:
    print("未知错误 %s" % result)
"""

try:
    num = int(input("请输入一个整数："))
    result = 8 / num
except Exception as result:
    print("%s" % result)
