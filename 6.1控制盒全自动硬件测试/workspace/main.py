#!/usr/bin/env python
# -*- coding:utf-8 -*-

import common
import threading, time, os, sys
from importlib import import_module


reload(sys)
sys.setdefaultencoding('utf-8')

path = sys.path[0]
cases_path = path + "/cases/"
report_path = path + "/report/"
sys.path.append(cases_path)

list = os.listdir(cases_path)
case_files = []
for case in list:
    if case[:2] == "IF" and case[-1:] != "c":
        case_files.append(case.split(".")[0])

for case in case_files:
    locals()[case] = import_module(case)



def main():
    box_num = raw_input("input box number:")
    over_time = float(raw_input("input work time:"))
    report_datas = common.report()
    log_path = path + "/log/" + box_num
    cases_run = []
    for case in case_files:
        cases_run.append(case + ".run(log_path)")
    threads = []
    threads.append(threading.Thread(target=common.heart_beat, args=(over_time,)))
    
    for t in threads:
        t.setDaemon(True)
        t.start()

    time_flag = 0
    while 1:
        for t in threads:
            if t.is_alive():
                for case_run in cases_run:
                    response = eval(case_run)
                    if response[response.keys()[0]]["state"]:
                        print ".",
                    else:
                        print "F",
                    report_datas.append_data(response)
            else:
                common.get_report_html(box_num, report_datas, report_path)
                time_flag = 1
        print ""
        if time_flag:
            break

    print 99999
            

if __name__ == '__main__':
    main()