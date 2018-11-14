#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time, threading, subprocess
import common

class MyThread(threading.Thread):

    def __init__(self,func,args=()):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None

def ping_ip(ip):
    count = 600
    error = 0
    commond = "ping -c %d %s" % (count, ip)
    try:
        backinfo =  subprocess.check_output([commond],shell=True)
        for i in backinfo.split(" "):
            if "%" in i:
                loss = int(i.split("%")[0])
        error = error + loss * count / 100
        for i in backinfo.split("\n"):
            if "64 bytes" in i:
                for j in i.split(" "):
                    if "time" in j:
                        w_time = j.split("=")[1]
                        if float(w_time) > 10:
                            error = error + 1
    except:
            error = count

    return count, error, backinfo

def run(log_path):
    test_project = "lan_wan"
    log_content = test_project + " test start"
    common.write_log(log_path, test_project, "info", log_content)
    ips = ["10.7.5.1", "10.7.5.88", "10.7.5.199", "10.7.5.100", "www.baidu.com"]
    ip_t = []
    respons = []
    for ip in ips:
        t = MyThread(ping_ip, args=(ip))
        ip_t.append(t)
        t.start()

    for t in ip_t:
        t.join()
        respons.append(t.get_result())

    count_num = 0
    fail_num = 0
    for i in respons:
        count_num = count_num + i[0]
        fail_num = fail_num + i[1]
        if not i[1]:
            common.write_log(log_path, test_project, "info", str(i[2]))
        else:
            common.write_log(log_path, test_project, "error", str(i[2]))
    pass_num = count_num - fail_num
    state = None
    if fail_num == 0:
        state = True
    else:
        state = False
    return {test_project:{"state":state, "count_num":count_num, "pass_num":pass_num, "fail_num":fail_num}}