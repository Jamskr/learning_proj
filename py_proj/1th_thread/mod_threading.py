#!/us/bin/python
#-*-coding:UTF-8-*-

import threading
from time import sleep
from datetime import datetime

thd_dly = [4, 2]
date_time_format = "%y-%M-%d %H:%M:%S"

def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)

def loop(n_loop, n_sec):
    print('thread (', n_loop, ') start: ', date_time_str(datetime.now()), 'sleep (', n_sec, ') sec')
    sleep(n_sec)
    print('thread (', n_loop, ') end, end time: ', date_time_str(datetime.now()))

def main():
    print('all thread start: ', date_time_str(datetime.now()))
    threads = []
    n_loops = range(len(thd_dly))

    for i in n_loops:
        t = threading.Thread(target=loop, args=(i, thd_dly[i]))
        threads.append(t)

    for i in n_loops:
        threads[i].start()

    for i in n_loops:
        threads[i].join()

    print('===all threads end, end time: ', date_time_str(datetime.now()))

if __name__ == "__main__":
    main()