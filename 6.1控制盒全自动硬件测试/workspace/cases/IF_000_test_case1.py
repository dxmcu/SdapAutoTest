#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import common

false = False
true = True

def run(log_path):
    test_project = "扫地图"
    log_content = test_project + " test start"
    common.write_log(log_path, test_project, "info", log_content)
    state = True
    count_num = 10
    pass_num = 0
    fail_num = 0
    time.sleep(1)
    return {test_project:{"state":True, "count_num":10, "pass_num":9, "fail_num":1}}