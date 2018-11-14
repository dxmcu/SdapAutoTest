#encoding:utf-8
from selenium import webdriver
from Testcore.GetTestConfig import GetTestConfig
class TestWebDriver:
    getconf=GetTestConfig()
    url=getconf.geturl()
    driver=webdriver.Firefox()
    def startFirefoxDriver(self):
        try:
            self.driver.get(self.url)
        except Exception:
            print "webdriver start Error!"
    def closeFirefoxDriver(self):
        
        try:
            self.driver.quit()
        except Exception:
            print "webdriver end Error!"