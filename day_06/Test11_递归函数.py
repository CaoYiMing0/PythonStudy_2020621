"""
函数的简单定义如下：
    def recurision():
        return  recurision()
"""


# 计算n!
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print("调用递归函数执行结果为：", fact(5))  # 调用递归函数执行结果为： 120

# 使用递归要注意防止栈溢出
print(fact(10000))  # 错误：RecursionError: maximum recursion depth exceeded in comparison
