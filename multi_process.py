#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    print('Parrent process id is %s ...' % os.getppid())

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))

    p1 = Process()
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
