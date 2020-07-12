"""
什么是匿名函数？
匿名函数就是不再使用def语句这样的标准形式定义一个函数。
Python使用lambda创建匿名函数
lambda只是一个表达式，函数体比def简单很多。
lambda的主体是一个表达式，而不是一个代码块，仅能在lambda表达式中封装有限的逻辑。lambda
函数拥有自己的命名空间，不能访问自有参数列表之外或全局命名空间的参数。
lambda函数的语法只包含一个语句：
    lambda [arg1[,arg2,......argn]]:expression
"""

"""
def func(x, y):
    return x + y


# 使用lambda
lambda x, y: x + y
# lambda表达编写的代码比使用def语句少，这里不太明显

# 求一个列表中大于3的元素，通过过程式编程实现
L1 = [1, 2, 3, 4, 5]
L2 = []
for i in L1:
    if i > 3:
        L2.append(i)
print("列表中大于3的元素有：", L2)  # 列表中大于3的元素有： [4, 5]
# 通过函数式编程实现，运用filter，给出一个判断条件：
def func(x):
    return x>3
f_list=filter(func,[1,2,3,4,5])
print("列表中大于3的元素有：",[item for in f_list])
"""

"""
在表达式中：
    x为lambda函数的一个参数。
    :为分割符。
    x>3则是返回值，在lambda函数中不能有return，其实冒号(:)后面就是返回值。
"""
