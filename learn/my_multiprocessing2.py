from multiprocessing import Pool, Lock
import time


def function(index):
    print("Start process:", index)
    time.sleep(1)
    print("End process:", index)
    return index

if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in range(4):
        result=pool.apply_async(function, (i,))
        print(result.get())
        # pool.apply(function, (i,))
    print("start process")
    pool.close()
    pool.join()
    print("subprocess done")
