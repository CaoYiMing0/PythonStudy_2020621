"""
如果需要一个函数能够处理的参数声明时更多，这些参数叫做可变参数。
和前边所述两种参数不同，可变参数声明时不会命名。基本语法如下：
    def functionname([formal_args,]*var_args_tuple):
        "函数_文档字符串"
        function_suite
        return [exception]
加了星号（*）的变量名会存放所有未命名的变量参数。如果变量参数在函数调用时没有
指定参数，就是一个空元组。也可以不向可变函数传递未命名的变量。
"""


def personinfo(arg, *vartuple):
    print(arg)
    for var in vartuple:
        print('我属于不定长参数部分:', var)
    return


print('------不带可变参数------')
personinfo('小萌')
print('------带两个可变参数------')
personinfo('小萌', 21, 'beijing')
print('------带5个可变参数------')
personinfo('小萌', 21, 'beijing', 123, 'jiaozuo', 'happy')
"""
执行结果如下：
------不带可变参数------
小萌
------带两个可变参数------
小萌
我属于不定长参数部分: 21
我属于不定长参数部分: beijing
------带5个可变参数------
小萌
我属于不定长参数部分: 21
我属于不定长参数部分: beijing
我属于不定长参数部分: 123
我属于不定长参数部分: jiaozuo
我属于不定长参数部分: happy
"""
"""
在函数内部，参数前的星号将所有值放在同一个元组中，通过这种方式收集起来，然后使用。
"""


# 关于可变参数的补充
# a,b为必选参数；c为默认参数；args为可变参数；kw为关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)


# 参数定义的顺序必须是：必选参数、默认参数、可选参数、命名关键字参数、关键字参数
def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)


f1(1, 2)
f1(1, 2, 3)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99, y=88, z=77, t='100')  # 重点***********
f2(1, 2, city='Shanghai', ext=None)
"""
调用结果：
a= 1 b= 2 c= 0 args= () kw= {}
a= 1 b= 2 c= 3 args= () kw= {}
a= 1 b= 2 c= 3 args= () kw= {}
a= 1 b= 2 c= 3 args= ('a', 'b') kw= {}
a= 1 b= 2 c= 3 args= ('a', 'b') kw= {'x': 99, 'y': 88, 'z': 77, 't': '100'}
f2(1, 2, city='Shanghai', ext=None)语句出现如下错误：
TypeError: f2() missing 1 required keyword-only argument: 'd'
"""
