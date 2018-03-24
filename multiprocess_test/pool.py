from multiprocessing import Pool
import time
import os
import random

def profile(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('耗时:{}'.format(end - start))
    return wrapper

def work(num):
    time.sleep(random.random() * 2)
    print("{}执行的进程id是{},父进程id是{}.".format(num,os.getpid(),os.getppid()))


if __name__ == '__main__':
    print('start...............')
    pool = Pool(3)
    for i in range(0,10):
        pool.apply_async(work,args=(i,)) #非阻塞式

    pool.close()
    pool.join()
    print('end................')
#使用非阻塞式时打开下面for循环
#for i in range(0,12):
#    time.sleep(random.random() * 2)
#    print("主进程的pid是{},i=={}".format(os.getpid(),i))

