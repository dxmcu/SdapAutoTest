#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time, os, urllib2, json, inspect, ctypes, datetime

test_ip = "10.7.5.88"
test_name = "gaussian"
test_port = "8080"

class Template_mixin(object):
    """html报告"""
    HTML_TMPL = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title> %(box_num0)s测试报告</title>
            <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
            <h1 style="font-family: Microsoft YaHei">%(box_num1)s测试报告</h1>
            <p class='attribute'><strong>测试结果 : </strong> %(value)s</p>
            <style type="text/css" media="screen">
        body  { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px;}
        </style>
        </head>
        <body>
            <table id='result_table' class="table table-condensed table-bordered table-hover">
                <colgroup>
                    <col align='left' />
                    <col align='right' />
                    <col align='right' />
                    <col align='right' />
                </colgroup>
                <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
                    <th>序列号</th>
                    <th>项目名称</th>
                    <th>测试结果</th>
                    <th>测试详情</th>
                </tr>
                %(table_tr)s
            </table>
        </body>
        </html>"""
    
    TABLE_TMPL = """
        <tr class='failClass warning'>
            <td>%(num)s</td>
            <td>%(name)s</td>
            <td>%(runresult)s</td>
            <td>%(reason)s</td>
        </tr>"""

def get_report_html(box_num, report_datas, report_path):
    table_tr0 = ''
    fail_n = 0
    pass_n = 0
    html = Template_mixin()
    datas = report_datas.report_datas
    for data in datas.keys():
        if datas[data]["state"]:
            pass_n = pass_n + 1
        else:
            fail_n = fail_n + 1
    test_count = pass_n + fail_n
    for i in range(len(datas.keys())):
        runresult0 = ""
        if datas[datas.keys()[i]]["state"]:
            runresult0 = "Pass"
        else:
            runresult0 = "Fail"
        reason0 = "count:" + str(datas[datas.keys()[i]]["count_num"]) + " pass:" + str(datas[datas.keys()[i]]["pass_num"]) + " fail:" + str(datas[datas.keys()[i]]["fail_num"])
        table_td = html.TABLE_TMPL % dict(num=str(i + 1),name=str(datas.keys()[i]),runresult=runresult0,reason=reason0,)
        table_tr0 += table_td
    total_str = '共 %s，通过 %s，失败 %s' % (test_count, pass_n, fail_n)
    output = html.HTML_TMPL % dict(box_num0 = box_num,box_num1 = box_num,value = total_str,table_tr = table_tr0,)
    report_name = box_num + "测试报告.html"
    with open(report_path + report_name,'wb') as f:
        f.write(output.encode('utf-8'))

class report():
    def __init__(self):
        self.report_data = {}
        self.report_datas = {}
    
    def append_data(self, response):
        self.report_data[response.keys()[0]] = response[response.keys()[0]]
        if response.keys()[0] in self.report_datas.keys():
            if not self.report_data[response.keys()[0]]["state"]:
                self.report_datas[response.keys()[0]]["state"] = False
            self.report_datas[response.keys()[0]]["count_num"] = self.report_datas[response.keys()[0]]["count_num"] + response[response.keys()[0]]["count_num"]
            self.report_datas[response.keys()[0]]["pass_num"] = self.report_datas[response.keys()[0]]["pass_num"] + response[response.keys()[0]]["pass_num"]
            self.report_datas[response.keys()[0]]["fail_num"] = self.report_datas[response.keys()[0]]["fail_num"] + response[response.keys()[0]]["fail_num"]
        else:
            self.report_datas[response.keys()[0]] = response[response.keys()[0]]

def log_content_info(text):
    return str(datetime.datetime.now()).split(".")[0] + " [INFO] " + text

def log_content_error(text):
    return str(datetime.datetime.now()).split(".")[0] + " [ERROR] " + text

def write_log(log_path, test_project, state, text):
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    fd = open(log_path + "/" + test_project + ".log", "a+")
    if state == "info":
        fd.write(log_content_info(text))
    else:
        fd.write(log_content_error(text))
    fd.write("\n")
    fd.close()
    
def heart_beat(over_time):
    secs = over_time * 3600
    for i in range(int(secs)):
        time.sleep(1)

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

def json2dict(urlData):
	try:
		urlData = json.loads(urlData)
		return urlData
	except Exception, e:
		print e
		print Exception

def getUrlData(url):
	response = urllib2.urlopen(url)
	urlDataJson = response.read()
	urlData = json2dict(urlDataJson)
	return urlData

def postUrlData(url,value):
	values = json.dumps(value)
	req = urllib2.Request(url, values)
	response = urllib2.urlopen(req)
	urlDataJson = response.read()
	urlData = json2dict(urlDataJson)
	return urlData

def get_url(commond):
    url = "http://" + test_ip + ":" + test_port + commond
    return url

def check_value(value, value_list, max_one = 16):
    if value < 2**(max_one) and value > 2**(max_one - 1):
        value_list.append(max_one)
        value -= 2**(max_one - 1)
        check_value(value, value_list, max_one - 1)
    elif value == 2**(max_one - 1):
        value_list.append(max_one)
        return 0
    else:
        check_value(value, value_list, max_one - 1)

