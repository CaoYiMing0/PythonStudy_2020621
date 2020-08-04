import threading
from time import sleep
from datetime import datetime

"""
从Thread派生一个子类，创建这个子类的实例。
"""
loops = [4, 2]
date_time_format = "%y-%M-%d %H:%M:%S"


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print(f"starting {self.name} at {date_time_str(datetime.now())}")
        self.func(*self.args)
        print(f"{self.name} finished at:{date_time_str(datetime.now())}")


def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)


def loop(n_loop, n_sec):
    print(f"线程（{n_loop}）开始执行：{date_time_str(datetime.now())}，先休眠（{n_sec}）秒")
    sleep(n_sec)
    print(f"线程（ {n_loop}）休眠结束，结束于：{date_time_str(datetime.now())}")


def main():
    print(f"---所有线程开始执行：{date_time_str(datetime.now())}")
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    for i in n_loops:
        threads[i].start()
    for i in n_loops:
        threads[i].join()
    print(f"---所有线程执行结束于：{date_time_str(datetime.now())}")


if __name__ == "__main__":
    main()
"""
    由代码片段和执行函数我们看到，子类化Thread类，MyThread子类的构造函数一定要先
调用基类的构造函数，特殊函数__call__()在子类中，名字要改为run()。在MyThread类中，
加入一些用于调试的输出信息，把代码保存到MyThread模块中，并导入这个类。使用self.func()
函数运行这些函数，并把结果保存在实现的self.res属性中，创建一个新函数getResult()得到
结果。
"""
