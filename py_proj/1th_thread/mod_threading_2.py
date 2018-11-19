#!/usr/bin/python
#-*-coding:UTF-8-*-

import threading
from time import sleep
from datetime import datetime

loops = [4, 2]
date_time_format = '%y-%M-%d %H:%M:%S'

class thread_func(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        # pass
        self.func(*self.args)

def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)

def loop(n_loop, n_sec):
    print('thread (', n_loop,') start:', date_time_str(datetime.now()), 'sleep (', n_sec, ') secs')
    sleep(n_sec)
    print('thread (', n_loop,') end, end time:', date_time_str(datetime.now()))

def main():
    print("all threads start:", date_time_str(datetime.now()))
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=thread_func(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all threads in end, end time: ', date_time_str(datetime.now()))

if __name__ == "__main__":
    main()