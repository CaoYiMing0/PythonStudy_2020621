"""
    使用Thread对象的lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方
法和release方法。对于每次只允许一个线程操作的数据，可以将操作放到acquire和release
方法之间。
"""
import threading
from time import sleep
from datetime import datetime

"""
    考虑到这样一种情况：一个列表里所有元素都是0，线程set从后向前把所有元素改成1，
而线程print负责从前往后读取列表并输出。
    线程set开始改的时候，线程print可能就来输出列表了，输出就成了一半0一半1，这就
是数据不同步的问题。为了避免这种情况，引入了锁的概念。
    锁有两种状态————锁定和未锁定。当一个线程（如set）要访问共享数据时，必须先获得
锁定；如果已经有别的线程（如print）获得锁定了，就让线程set暂停，也就是同步阻塞；等
到线程print访问完毕，释放锁以后，再让线程set继续。
    经过这样的处理，输出列表时要么全部输出0，要么全部输出1，不会出现一半0一半1的
尴尬场面。
"""

date_time_format = "%y-%M-%d %H:%M:%S"


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print(f"开启线程：{self.name}")
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()


def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)


def print_time(threadName, delay, counter):
    while counter:
        sleep(delay)
        print(f"%s:%s" % (threadName, date_time_str(datetime.now())))
        counter -= 1


def main():
    # 创建新线程
    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)
    # 开启新线程
    thread1.start()
    thread2.start()
    # 添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)
    # 等待所有线程完成
    for i in threads:
        i.join()
    print("退出主线程")


if __name__ == "__main__":
    threadLock = threading.Lock()
    threads = []
    main()
