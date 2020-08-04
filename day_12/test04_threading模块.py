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

"""
    Thread有很多_thread模块里没有的函数，Thread对象的函数很丰富。下面将创建一个Thread的
实例，传给它一个函数。示例如下：
"""
loops = [4, 2]
date_time_format = "%y-%M-%d %H:%M:%S"


def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)


def loop(n_loop, n_sec):
    print("线程（", n_loop, "）开始执行：", date_time_str(datetime.now()), "，先休眠（", n_sec, "）秒")
    sleep(n_sec)
    print("线程（", n_loop, "）休眠结束，结束于：", date_time_str(datetime.now()))


def main():
    print("---所有线程开始执行：", date_time_str(datetime.now()))
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in n_loops:  # start threads
        threads[i].start()

    for i in n_loops:  # wait for all
        threads[i].join()  # threads to finish
    print(f"---所有线程执行结束于：{date_time_str(datetime.now())}")


if __name__ == "__main__":
    main()
"""
---所有线程开始执行： 20-23-03 01:23:29
线程（ 0 ）开始执行： 20-23-03 01:23:29 ，先休眠（ 4 ）秒
线程（ 1 ）开始执行： 20-23-03 01:23:29 ，先休眠（ 2 ）秒
线程（ 1 ）休眠结束，结束于： 20-23-03 01:23:31
线程（ 0 ）休眠结束，结束于： 20-23-03 01:23:33
---所有线程执行结束于：20-23-03 01:23:33
    由执行结果我们可看到，实例化一个Thread（调用Thread()）与调用_thread.start_new_thread()
最大的区别是新的线程不会立即开始。创建线程对象却不想马上开始运行线程时，Thread是一个很有用的同
步特性。所有线程都创建之后，再一起调用start()函数启动，而不是每创建一个线程就启动。而且不用管理
一堆锁的状态（分配锁、获得锁、释放锁、检查锁的状态等），只要简单对每个线程调用join()主线程，等待
子线程结束即可。join()还可以设置timeout参数，即主线程的超时时间。
    join()另一个比较重要的方面是可以完全不用调用。一旦线程启动，就会一直运行，直到线程的函数结束
并退出为止。如果主线程除了等线程结束外，还有其他事情要做，就不要调用join()，只有在等待线程结束时
才调用。
"""
