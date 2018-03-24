import os
import time

print("只有主进程执行此语句")
#调用fork函数后，会产生2个值：子进程的pid和父进程的pid，
#其中子进程的pid为0，父进程的pid为子进程的pid，其实就相当于返回了2个子进程号
#以下为os模块中fork函数的结束
#1.For a child process.
#2.Return 0 to child process and PID of child to parent process

pid = os.fork() #调用os模块的fork函数创建进程
print("主进程和子进程都能执行此语句,进程id={}".format(os.getpid()))


if pid == 0:
    #子进程执行代码块
    print("我是子进程,子进程id是{},父进程id是{}".format(os.getpid(),os.getppid()))

elif pid > 0:
    #父进程执行的代码块
    #下句语句中的pid容易跟if判断中的pid混淆
    print("我是父进程,父进程id是{},子进程id是{}".format(os.getpid(),pid))
