#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import common
import subprocess

host_ip = "10.7.5.66"
host_ip = "8080"

false = False
true = True

def run(log_path):
    test_project = "key"
    log_content = test_project + " test start"
    common.write_log(log_path, test_project, "info", log_content)
    state = True
    count_num = 10
    pass_num = 0
    fail_num = 0
    url = "http://" + host_ip + ":" + host_ip + "/gs-robot/cmd/operate_device"
    open_value = str(int("01010110", 2))
    close_value = str(int("01011010", 2))
    for i in range(count_num):
        value = [{"name" : "relay","type" : "int","value" : open_value,"delayTime" : 0}]
        common.write_log(log_path, test_project, "info", url)
        common.write_log(log_path, test_project, "info", value)
        commond = "ping -c 1 10.7.5.88"
        data = common.postUrlData(url, value)
        time.sleep(1)
        if data["successed"]:
            common.write_log(log_path, test_project, "info", data)
            try:
                common.write_log(log_path, test_project, "info", commond)
                backinfo =  subprocess.check_output([commond],shell=True)
                common.write_log(log_path, test_project, "info", backinfo)
                value = [{"name" : "relay","type" : "int","value" : close_value,"delayTime" : 0}]
                common.write_log(log_path, test_project, "info", url)
                common.write_log(log_path, test_project, "info", value)
                data = common.postUrlData(url, value)
                time.sleep(5)
                if data["successed"]:
                    common.write_log(log_path, test_project, "info", data)
                    try:
                        common.write_log(log_path, test_project, "info", commond)
                        backinfo =  subprocess.check_output([commond],shell=True)
                        if backinfo:
                            common.write_log(log_path, test_project, "error", str(backinfo))
                            state = False
                            fail_num += 1
                    except:
                        common.write_log(log_path, test_project, "info", "No Data...")
                        value = [{"name" : "relay","type" : "int","value" : open_value,"delayTime" : 0}]
                        common.write_log(log_path, test_project, "info", url)
                        common.write_log(log_path, test_project, "info", value)
                        data = common.postUrlData(url, value)
                        time.sleep(60)
                        if data["successed"]:
                            common.write_log(log_path, test_project, "info", data)
                            try:
                                common.write_log(log_path, test_project, "info", commond)
                                backinfo =  subprocess.check_output([commond],shell=True)
                                common.write_log(log_path, test_project, "info", backinfo)
                                pass_num += 1
                            except:
                                common.write_log(log_path, test_project, "error", "No Data...")
                                state = False
                                fail_num += 1
                        else:
                            common.write_log(log_path, test_project, "error", "No Data...")
                            state = False
                            fail_num += 1
                else:
                    common.write_log(log_path, test_project, "error", "No Data...")
                    state = False
                    fail_num += 1
            except:
                common.write_log(log_path, test_project, "error", "No Data...")
                state = False
                fail_num += 1
        else:
            common.write_log(log_path, test_project, "error", str(data))
            state = False
            fail_num += 1
    return {test_project:{"state":state, "count_num":count_num, "pass_num":pass_num, "fail_num":fail_num}}