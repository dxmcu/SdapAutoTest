from Testcore.TestWebDriver import TestWebDriver
class Sdaplogin:
    def SysClientLogin(self):
        TestWebDriver.driver.find_element_by_id("kw").send_keys("selenium")
        TestWebDriver.driver.find_element_by_id("su").click()