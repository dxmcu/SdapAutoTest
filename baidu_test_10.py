#!/usr/local/bin/python3.7
#chrom derier https://npm.taobao.org/mirrors/chromedriver/70.0.3538.67/
#coding:utf-8
from lib2to3.pgen2 import driver

from selenium import webdriver
import time,os
#import thread
url="https://www.baidu.com"
#deiver.maximize_window()

def open_10_baidu():
	count = 1
	while ( count < 11 ):
		count = count + 1
		deiver = webdriver.Chrome()
		deiver.implicitly_wait(8)
		deiver.get(url)
		deiver.find_element_by_name("wd").send_keys("python")
		deiver.find_element_by_id("su").click()
		time.sleep(5)
		deiver.quit()
		time.sleep(2)
'''
def open_10_baidu_seting():
	count_1 = 1
	while ( count_1 < 11 ):
		count = count_1 + 1
		deiver = webdriver.Chrome()
		deiver.implicitly_wait(8)
		deiver.get(url)
		#link = driver.find_element_by_link_text("设置")
		link = deiver.find_element_by_class_name("bdpfmenu")
		ActionChains(driver).move_to_element(link).perform()
		driver.find_element_by_class_name("setpref").click()
		time.sleep(2)
		deiver.quit()
		time.sleep(2)
'''
'''
try:
	thread.start_new_thread(open_10_baidu,("thread-1",2))
	thread.start_new_thread(open_10_baidu_seting,("thread-2",4))
except:
	print ("Error: open_false")	
'''		
if __name__ == '__main__':
	open_10_baidu()
'''
import webbrowser
import time,os
url='www.baidu.com/s?wd=python'

chromePath = r'C:\Program Files (x86)\Google\Chrome\Application'
webbrowser.open(url, new=0, autoraise=True)
time.sleep(5)
webbrowser.open('https://www.baidu.com/s?wd=python',0 , False)
os.system('taskkill /F /IM chrome.exe')

#webbrowser.open(url, new=0, autoraise=True)
#webbrowser.open_new(url)
#webbrowser.open_new_tab(url)
'''