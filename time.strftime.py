#!/usr/bin/python
## -*- coding: UTF-8 -*-
import time,datetime
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
time.sleep(1)
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
TIME = datetime.datetime.now()
print (TIME.strftime('%H:%M:%S'))
print (TIME.strftime('%Y-%d-%d'))