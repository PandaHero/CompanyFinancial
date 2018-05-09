# multiprocessing
# 在mulprocessing中，每一个进程都用process表示，
import multiprocessing
from multiprocessing import Process, Lock
import time


# def process(num):
#     print("the num of process is ", num)
# if __name__ == '__main__':
#     for i in range(12):
#         p = multiprocessing.Process(target=process, args=(i,))
#         p.start()
#     print("cpu number" + str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print("child process name" + p.name + "id:" + str(p.pid))


# 自定义process类,实现run方法
class MyProcess(Process):
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.01)
            self.lock.acquire()
            print("pid:" + str(self.pid) + "loopCount:" + str(count))
            self.lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(10, 20):
        p = MyProcess(i,lock)
        # # 保证父进程结束的同时子进程也结束
        # p.daemon = True
        p.start()
    #     # 保证父进程等待子进程执行完毕
    #     p.join()
    # print("main process ended")
