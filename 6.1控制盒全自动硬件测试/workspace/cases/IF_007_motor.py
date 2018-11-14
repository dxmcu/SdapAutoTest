#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import common

false = False
true = True

def run(log_path):
    test_project = "motor"
    log_content = test_project + " test start"
    common.write_log(log_path, test_project, "info", log_content)
    state = True
    count_num = 600
    pass_num = 0
    fail_num = 0
    url = common.get_url("/gs-robot/data/health_status")
    for i in range(count_num):
        common.write_log(log_path, test_project, "info", url)
        data = common.getUrlData(url)
        time.sleep(1)
        if data["rightMotor"] and data["leftMotor"]:
            common.write_log(log_path, test_project, "info", str(data))
            pass_num += 1
        else:
            common.write_log(log_path, test_project, "error", str(data))
            fail_num += 1
    return {test_project:{"state":state, "count_num":count_num, "pass_num":pass_num, "fail_num":fail_num}}