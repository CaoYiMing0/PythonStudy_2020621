class MyClass(object):
    i = 123

    def f(self):
        return "Hello world!"
"""
由上面的示例可知，类定义的语法格式如下：
class ClassName(object):
    <statement-1>
    .
    .
    .
    <statement-N>
Python中使用class关键字定义类，class后面紧跟着类名，如MyClass，类名通常是大写字母开头的单词；
紧接着是(object)，表示该类是从哪个类继承下来的。通常没有合适的继承类，就使用object类，这是所有类最终
都会继承的类。
"""