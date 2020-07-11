total = 0  # 全局变量


def sum(arg1, arg2):
    total = arg1 + arg2  # 局部变量
    print("函数内是局部变量:", total)
    return total


def totalprint():
    print("total的值是", total)
    return total


print("函数求和结果:", sum(10, 20))
totalprint()
print("函数外是全局变量:", total)
print("--------------------------")
"""
函数内是局部变量: 30
函数求和结果: 30
total的值是 0
函数外是全局变量: 0
"""

num = 100


def func():
    num = 200
    print("函数体中num的值为：", num)


func()
print("函数外num的值为：", num)
print("-------------------------")
"""
函数体中num的值为： 200
函数外num的值为： 100
"""

# 在局部中怎么使用全局变量呢？
num2 = 100
print("函数调用前num的值为:", num2)


def func2():
    global num2
    num2 = 200
    print("函数体中num的值为：", num2)


func2()
print("函数调用结束后num的值为：", num2)
print("------------------------------")
"""
函数调用前num的值为: 100
函数体中num的值为： 200
函数调用结束后num的值为： 200
"""


# 全局变量放在定义的函数后，函数中使用全局变量会怎么样呢？
def func3():
    print("num3的值为：", num3)


func3()  # NameError: name 'num3' is not defined
num3 = 11
print("----------------------------")

# 函数中先声名一个局部变量，使用这个变量，再global一个全局变量，再使用这个同名字的变量，两次使用的是相同的吗？
num4 = 15


def func4():
    num4 = 20
    print("num4的值为：", num4)
    global num4
    print("global后的num4的值为：", num4)
    return


func4()  # 出错：SyntaxError: name 'num4' is used prior to global declaration
