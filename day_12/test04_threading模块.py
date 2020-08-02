"""
    更高级别的threading模块不仅提供了Thread类，还提供了各种非常好用的同步机制。
    _thread模块不支持守护线程，当主线程退出时，所有子线程无论是否在工作，都会被
强行退出。threading模块支持守护线程，守护线程一般是一个等待客户请求的服务器，如果
没有客户提出请求，就一直等着。如果设定一个线程为守护线程，就表示这个线程不重要，在
进程退出时，不用等待这个线程退出。如果主线程退出时不用等待子线程完成，就要设定这些
线程的daemon属性，即在线程Thread.start()开始前，调用setDaemon()函数设定线程的daemon
标志(Thread,setDaemon(True))，表示这个线程“不重要”。如果一定要等待子线程执行完成
再退出主线程，就什么都不用做或显式调用Thread.setDaemon(False)以保证daemon标志位False，
可以调用Thread.isDaemon()函数判断daemon标志的值。新的子线程会继承父线程的daemon标志，
整个Python在所有非守护线程退出后才会结束，即进程中没有非守护线程存在时才结束。
"""
import threading
from time import sleep
from datetime import datetime

loops = [4, 2]
date_time_format = "%y-%M-%d %H:%M:%S"


def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)


def loop(n_loop, n_sec):
    print("线程（", n_loop, "）开始执行：", date_time_str(datetime.now()), "，先休眠（", n_sec, "）秒")
    sleep(n_sec)
    print("线程（",n_loop,"）休眠结束，结束于：",date_time_str(datetime.now()))


def main():
    print("---所有线程开始执行：",date_time_str(datetime.now()))
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        t
