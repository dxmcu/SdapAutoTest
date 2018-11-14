#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import common
import os

false = False
true = True

def combination_k(s, k):
    '''
    字符串 s 中选取 k(0 <= k <= len(s)) 个元素，进行组合，以列表的形式返回所有可能的组合
    s --> 输入的字符串
    k --> 选取的元素的个数
    
    测试结果如下：
    combination_k('abc', 2) >>> ['ab', 'ac', 'bc']
    
    combination_k('c', 2)   >>> []
        combination_k('c', 2) 的递归内部解释如下：
            --> combination_k('c', 2)
                --> for i in combination_k('', 1):
                        c + i
                    # 由于 combination_k('', 1) 的返回结果是一个空列表，这 for 循环遍历不会被执行，所以返回初始设定的值 []
    '''
    # recursive basis
    if k == 0: return ['']
    # recursive chain
    subletters = []
    # 此处涉及到一个 python 遍历循环的特点：当遍历的对象为空（列表，字符串...）时，循环不会被执行，range(0) 也是一样
    for i in range(len(s)):
        for letter in combination_k(s[i+1:], k-1):
            subletters += [s[i] + letter]
    return subletters

def combination_all(s):
    '''
    本函数配合 combination_k 函数实现全组合
    s --> 组合元素的样本
    以列表的形式返回所有长度可能的组合
    
    测试如下：
    combination_all('abc') >>> ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
    '''
    comb_list = []
    # 通过 for 循环调用 combination_k(s, k) 获取不同 k 值下的所有组合
    for i in range(1, len(s)+1):
        comb_list += combination_k(s, i)
    return comb_list

def run(log_path):
    test_project = "input"
    log_content = test_project + " test start"
    common.write_log(log_path, test_project, "info", log_content)
    url = common.get_url("/gs-robot/data/device_status")
    state = True
    count_num = 10
    pass_num = 0
    fail_num = 0
    do_value_dict = {}
    for i in range(8):
        do_value = pow(2, i)
        do_value_key = "do" + str(i + 1)
        do_value_dict[do_value_key] = do_value

    all_do_value_comb = combination_all(do_value_dict.keys())
    all_do_value_comb_list = []
    for i in all_do_value_comb:
        value = 0
        for j in do_value_dict.keys():
            if j in i:
                value += do_value_dict[j]
        all_do_value_comb_list.append(value)
    all_do_value_comb_list.append(0)
    all_do_value_comb_list = sorted(all_do_value_comb_list)
    count_num = len(all_do_value_comb_list) * 2
    for j in range(2):
        for i in all_do_value_comb_list:
            do_commond = 'rosservice call /device/operate_device \"operation:\n- key: \'do\'\n  value: \'%d\'\"' % i
            common.write_log(log_path, test_project, "info", do_commond)
            res = os.popen(do_commond).read()
            if "True" in res:
                common.write_log(log_path, test_project, "info", res)
            else:
                common.write_log(log_path, test_project, "error", res)
            time.sleep(1)
            data = common.getUrlData(url)
            di_value = int(data["data"]["detailedDi"])
            if di_value != i:
                state = False
                common.write_log(log_path, test_project, "error", str(data))
                fail_num += 1
            else:
                common.write_log(log_path, test_project, "info", str(data))
                pass_num += 1
    return {test_project:{"state":state, "count_num":count_num, "pass_num":pass_num, "fail_num":fail_num}}