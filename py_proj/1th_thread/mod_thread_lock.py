#!/usr/bin/python
#-*-coding:UTF-8-*-

import _thread
from time import sleep
from datetime import datetime

thd_dly = [4, 2]
date_time_format = '%y-%M-%d %H:%M:%S'

def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)

def loop(n_loop, n_sec, lock):
    print('thread (', n_loop,') start:', date_time_str(datetime.now()), ', sleep (', n_sec,') sec')
    sleep(n_sec)
    print('thread (', n_loop,') end, end time:', date_time_str(datetime.now()))
    lock.release()

def main():
    print('all threads start...')
    locks = []
    n_loops = range(len(thd_dly))

    for i in n_loops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    
    for i in n_loops:
        _thread.start_new_thread(loop, (i, thd_dly[i], locks[i]))
    
    for i in n_loops:
        while locks[i].locked():pass
    
    print('====all threads end:', date_time_str(datetime.now()))

if __name__ == "__main__":
    main()
