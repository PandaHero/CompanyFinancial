from multiprocessing import Process, JoinableQueue
import time, os

# 生产者
def producer(q, name):
    for i in range(3):
        time.sleep(1)
        res = '%s%s' % (name, i)
        q.put(res)
        print('\033[45m<%s> 生产了 [%s]\033[0m' % (os.getpid(), res))
    q.join()  # 等消费者取完就结束

# 消费者
def consumer(q):
    while True:
        res = q.get()
        time.sleep(1.5)
        print('\033[34m<%s> 吃了 [%s]\033[0m' % (os.getpid(), res))
        q.task_done()  # 每取走一个就记一次


if __name__ == '__main__':
    q = JoinableQueue()

    # 生产者们：即厨师们
    p1 = Process(target=producer, args=(q, '包子'))
    # p2 = Process(target=producer, args=(q, '饺子'))
    # p3 = Process(target=producer, args=(q, '馄饨'))

    # 消费者们：即吃货们
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))

    c1.daemon = True  # 设为守护进程，当主进程结束，消费者进程也随之结束
    c2.daemon = True  # 设为守护进程，当主进程结束，消费者进程也随之结束
    p1.start()
    # p2.start()
    # p3.start()
    c1.start()
    c2.start()

    p1.join()  # 主进程等生产者结束

    print('主')
