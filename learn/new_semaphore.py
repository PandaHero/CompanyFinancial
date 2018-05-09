# from multiprocessing import Process, Semaphore, Lock, Queue
# import time
#
# buffer = Queue(10)
# empty = Semaphore(2)
# full = Semaphore(0)
# lock = Lock()
#
#
# # 消费者
# class Consumer(Process):
#     def run(self):
#         global buffer
#         while True:
#             full.acquire()
#             lock.acquire()
#             buffer.get()
#             print("Consumer pop an element")
#             # time.sleep(1)
#             lock.release()
#             empty.release()
#
# # 生产者
# class Producer(Process):
#     def run(self):
#         global buffer
#         while True:
#             empty.acquire()
#             lock.acquire()
#             buffer.put(1)
#             print("Product append an element")
#             # time.sleep(1)
#             lock.release()
#             full.release()
#
#
# if __name__ == '__main__':
#     p = Producer()
#     c = Consumer()
#     # p.daemon = True
#     # c.daemon = True
#     p.start()
#     c.start()
#     p.join()
#     c.join()
