from multiprocessing import Process
import time
import os

def profile(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print('耗时:{}'.format(end-start))
    return wrapper

@profile
def test1(interval):
    time.sleep(interval)
    print("我是test1,我的进程号是{},我的父进程id是{}".format(os.getpid(),os.getppid()))
@profile
def test2(interval):
    time.sleep(interval)
    print("我是test2,我的进程号是{},我的父进程id是{}".format(os.getpid(),os.getppid()))

p1 = Process(target = test1, args = (5,))
p1.start()
print("p1.pid = {}".format(p1.pid))
p1.join()

p2 = Process(target = test2, args = (5,))
p2.start()
print("p2.pid = {}".format(p2.pid))
