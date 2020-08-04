"""
    Queue模块可以用来进行线程间的通信，让各个线程之间共享数据。
    Python的Queue模块提供了同步、线程安全的队列类，包括FIFO（先进先出）队列Queue、
LIFO（后入先出）队列LifoQueue和优先级队列PriorityQueue。这些队列都实现了锁原语，能
够在多线程中直接使用。可以使用队列实现线程间的同步。
                        Queue模块中的常用方法
方法名                 描述
qsize()               返回队列的大小
empty()               如果队列为空，返回True，反之返回False
full()                 如果队列满了，返回True，反之返回False
full                    与MaxSize大小对应
get(block[,timeout]])   获取队列，timeout等待时间
get_nowait()            相当于Queue.get(False)
put(timeout)            写入队列，timeout等待时间
put_nowait(item)        相当于Queue.put(item, False)
task_done()             在完成一项工作后，函数向已经完成的队列发送一个信号
join()                  实际上意味着等到队列为空，再执行别的操作
"""

import threading
import queue
from time import sleep


class MyThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print(f"开启线程：{self.name}")
        process_data(self.name, self.q)
        print(f"退出线程：{self.name}")


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print(f"%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        sleep(1)


def main():
    global exitFlag
    exitFlag = 0
    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    nameList = ["One", "Two", "Three", "Four", "Five"]

    threads = []
    threadID = 1

    # 创建新线程
    for tName in threadList:
        thread = MyThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1
    # 填充队列
    queueLock.acquire()
    for word in nameList:
        workQueue.put(word)
    queueLock.release()
    # 等待队列清空
    while not workQueue.empty():
        pass
    # 通知线程是退出的时候了
    exitFlag = 1
    # 等待所有线程完成
    for t in threads:
        t.join()
    print(f"退出主线程")


if __name__ == "__main__":
    queueLock = threading.Lock()
    workQueue = queue.Queue(10)
    main()
