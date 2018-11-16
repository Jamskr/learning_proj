#!/usr/bin/python
#-*-coding:UTF-8-*-

import _thread
from time import sleep
from datetime import datetime

date_time_format = '%y-%M-%d %H:%M:%S'

def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)

def loop_one():
    print('===thread 1 start: ', date_time_str(datetime.now()))
    print('===sleep 4 sec')
    sleep(4)
    print('===thread 1 end: ', date_time_str(datetime.now()))

def loop_two():
    print('***thread 2 start: ', date_time_str(datetime.now()))
    print('***sleep 2 sec')
    sleep(2)
    print('***thread 2 end: ', date_time_str(datetime.now()))

def main():
    print('@@@all thread start: ',date_time_str(datetime.now()))
    _thread.start_new_thread(loop_one, ())
    _thread.start_new_thread(loop_two, ())
    sleep(6)
    print('@@@all thread end: ', date_time_str(datetime.now()))

if __name__ == "__main__":
    main()