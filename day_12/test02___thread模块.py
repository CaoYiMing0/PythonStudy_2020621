"""
Python中调用_thread模块中的start_new_thread()函数产生新线程。_thread的语法如下：
    _thread.start_new_thread(function,args[,kwargs])
    其中，function为线程函数；args为传递给线程函数的参数，必须是tuple类型；kwargs
为可选参数。
    _thread模块除了产生线程外，还提供基本同步数据结构锁对象（lock object，也叫原语锁、
简单锁、互斥锁、互斥量、二值化信号量）。同步原语与线程管理是密不可分的。
"""
import _thread
from time import sleep
from datetime import datetime

date_time_format = "%y-%M-%d %H:%M:%S"


def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)


def loop_one():
    print("+++线程一开始于：", date_time_str(datetime.now()))
    print("+++线程一休眠4秒")
    sleep(4)
    print("+++线程一休眠结束，结束于：", date_time_str(datetime.now()))


def loop_two():
    print("***线程二开始于：", date_time_str(datetime.now()))
    print("***线程二休眠2秒")
    sleep(2)
    print("***线程二休眠结束，结束于：", date_time_str(datetime.now()))


def main():
    print("------所有线程开始时间：", date_time_str(datetime.now()))
    _thread.start_new_thread(loop_one, ())
    _thread.start_new_thread(loop_two, ())
    sleep(6)
    print("------所有线程结束时间：", date_time_str(datetime.now()))


if __name__ == '__main__':
    main()
