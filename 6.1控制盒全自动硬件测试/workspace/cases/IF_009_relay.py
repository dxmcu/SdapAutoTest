#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import common

host_ip = "10.7.5.66"
host_ip = "8080"

false = False
true = True

def run(log_path):
    test_project = "relay"
    log_content = test_project + " test start"
    common.write_log(log_path, test_project, "info", log_content)
    state = True
    count_num = 75
    pass_num = 0
    fail_num = 0
    url_relay = common.get_url("/gs-robot/cmd/operate_device")
    url_di = "http://" + host_ip + ":" + host_ip + "/gs-robot/data/device_status"
    for i in range(count_num):
        value = [{"name" : "do","type" : "int","value" : "0","delayTime" : 0}]
        common.write_log(log_path, test_project, "info", url_relay)
        common.write_log(log_path, test_project, "info", str(value))
        data = common.postUrlData(url_relay, value)
        time.sleep(1)
        if data["successed"]:
            common.write_log(log_path, test_project, "info", str(data))
            common.write_log(log_path, test_project, "info", url_di)
            data = common.getUrlData(url_di)
            time.sleep(1)
            di_value = int(data["data"]["detailedDi"])
            one_list = []
            common.check_value(di_value, one_list)
            if 4 not in one_list and 5 not in one_list:
                common.write_log(log_path, test_project, "info", str(data))
                value = [{"name" : "do","type" : "int","value" : "1","delayTime" : 0}]
                common.write_log(log_path, test_project, "info", url_relay)
                data = common.postUrlData(url_relay, value)
                time.sleep(1)
                if data["successed"]:
                    common.write_log(log_path, test_project, "info", str(data))
                    common.write_log(log_path, test_project, "info", url_di)
                    data = common.getUrlData(url_di)
                    time.sleep(1)
                    di_value = int(data["data"]["detailedDi"])
                    one_list = []
                    common.check_value(di_value, one_list)
                    if 4 in one_list and 5 not in one_list:
                        common.write_log(log_path, test_project, "info", str(data))
                        value = [{"name" : "do","type" : "int","value" : "2","delayTime" : 0}]
                        common.write_log(log_path, test_project, "info", url_relay)
                        data = common.postUrlData(url_relay, value)
                        time.sleep(1)
                        if data["successed"]:
                            common.write_log(log_path, test_project, "info", str(data))
                            common.write_log(log_path, test_project, "info", url_di)
                            data = common.getUrlData(url_di)
                            time.sleep(1)
                            di_value = int(data["data"]["detailedDi"])
                            one_list = []
                            common.check_value(di_value, one_list)
                            if 4 not in one_list and 5 in one_list:
                                common.write_log(log_path, test_project, "info", str(data))
                                value = [{"name" : "do","type" : "int","value" : "3","delayTime" : 0}]
                                common.write_log(log_path, test_project, "info", url_relay)
                                data = common.postUrlData(url_relay, value)
                                time.sleep(1)
                                if data["successed"]:
                                    common.write_log(log_path, test_project, "info", str(data))
                                    common.write_log(log_path, test_project, "info", url_di)
                                    data = common.getUrlData(url_di)
                                    time.sleep(1)
                                    di_value = int(data["data"]["detailedDi"])
                                    one_list = []
                                    common.check_value(di_value, one_list)
                                    if 4 in one_list and 5 in one_list:
                                        common.write_log(log_path, test_project, "info", str(data))
                                        pass_num += 1
                                    else:
                                        common.write_log(log_path, test_project, "error", str(data))
                                        state = False
                                        fail_num += 1
                                else:
                                    common.write_log(log_path, test_project, "error", str(data))
                                    state = False
                                    fail_num += 1
                            else:
                                common.write_log(log_path, test_project, "error", str(data))
                                state = False
                                fail_num += 1
                        else:
                            common.write_log(log_path, test_project, "error", str(data))
                            state = False
                            fail_num += 1
                    else:
                        common.write_log(log_path, test_project, "error", str(data))
                        state = False
                        fail_num += 1
                else:
                    common.write_log(log_path, test_project, "error", str(data))
                    state = False
                    fail_num += 1
            else:
                common.write_log(log_path, test_project, "error", str(data))
                state = False
                fail_num += 1
        else:
            common.write_log(log_path, test_project, "error", str(data))
            state = False
            fail_num += 1

    time.sleep(1)
    return {test_project:{"state":state, "count_num":count_num, "pass_num":pass_num, "fail_num":fail_num}}