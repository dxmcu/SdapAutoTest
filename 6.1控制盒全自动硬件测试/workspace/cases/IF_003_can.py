#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time, datetime
import common

false = False
true = True

def run(log_path):
    test_project = "can"
    log_content = test_project + " test start"
    common.write_log(log_path, test_project, "info", log_content)
    url = common.get_url("/gs-robot/real_time_data/ultrasonic_raw?frame_id=ultrasonic0")
    state = True
    count_num = 600
    pass_num = 0
    fail_num = 0
    for i in range(count_num):
        data = common.getUrlData(url)
        if data == 1:
            state = False
            fail_num += 1
            common.write_log(log_path, test_project, "error", str(data))
        else:
            pass_num += 1
            common.write_log(log_path, test_project, "info", str(data))
        time.sleep(1)
    return {test_project:{"state":state, "count_num":count_num, "pass_num":pass_num, "fail_num":fail_num}}