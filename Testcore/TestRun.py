#encoding:utf-8
import os,time
#from AutoTestSdap.TestComponent.SdapLogin import SdapLogin
from Testcore.TestCaseComponent import TestCaseComponent
from Testcore.TestCase import TestCase
from Testcore.TestStep import TestStep
from Testcore.TestSuite import TestSuite
from Testcore.TestPlan import TestPlan
from Testcore.TestGeneId import TestGeneid
from Testcore.TestWebDriver import TestWebDriver
#测试用例执行器
'''
@author: xianqingchen
@date:2016-11-06
'''
class TestRun:
    #定义测试组件列表
    testcomponentlist=TestCaseComponent().__getcomponentList__()
    #定义测试流程步骤
    #按照测试执行流程配置进行测试
    def TestRun(self):
        #获取当前时间
        t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        #对测试流程各个步骤初始化对象
        testplan=TestPlan()
        testsuite=TestSuite()
        testcase=TestCase()
        teststep=TestStep()
        #id生成执行计数器清零
        TestGeneid().resetid()
        #创建（获取）测试计划
        fpath=os.path.abspath("..")+u"\\TestPlan\\测试执行计划.xls"
        testplan.__TestPlan__(fpath)
        #获取测试计划下的测试场景列表
        testsuiteList=testplan.__gettestsuiteList__()
        #设置测试执行开始时间
        testplan.__settestplanstarttime__(t)
        #设置默认测试执行结果
        testplan.__setresult__("1")
        #第一层循环，循环执行测试计划配置的所有测试场景
        for i in range(0,len(testsuiteList)):
            #启动测试
            TestWebDriver().startFirefoxDriver()
            try:
                #获取测试场景
                testsuite=testsuiteList[i]
                #获取测试场景下测试用例列表
                testcaseList=testsuite.__gettestcaseList__()
                #设置测试场景开始执行时间
                testsuite.__setstarttime__(t)
                #第二层循环，循环执行测试场景中配置的所有用例
                for j in range(0,len(testcaseList)):
                    #获取测试用例
                    testcase=testcaseList[j]
                    #获取测试用例下测试步骤列表
                    testcaseStepList=testcase.__gettestcaseStepList__()
                    #设置测试用例开始执行时间
                    testcase.__setstarttime__(t)
                    #第三层循环，循环执行用例步骤
                    for k in range(0,len(testcaseStepList)):
                        #执行用例步骤
                        teststep=testcaseStepList[k]
                        if teststep.__getisrun__()==1:
                            #设置测试步骤开始执行时间
                            teststep.__settestcasestepstarttime__(t)
                            #执行测试步骤
                            self.executeTestStep(testsuite,testcase,teststep)
                            #设置测试步骤结束执行时间
                            teststep.__settestcasestependtime__(t)
                            #设置测试步骤运行结果为"1"成功
                            teststep.__setresult__("1")
                        else:
                            print "Test case execution failed !"
                    #设置测试用例执行结束时间
                    testcase.__setendtime__(t)
                    #设置测试用例运行结果为"1"成功
                    testcase.__setresult__("1")
                #设置测试场景执行结束时间
                testsuite.__setendtime__(t)
                #设置测试场景运行结果为"1"成功
                testsuite.__setresult__("1")
            finally:
                time.sleep(20)
                TestWebDriver().closeFirefoxDriver()
        #设置测试计划执行结束时间
        testplan.__settestplanendtime__(t)
    #执行测试步骤，结合业务组件中的类和方法
    def executeTestStep(self,TestSuite,TestCase,TestStep):
        t=TestCaseComponent()
        t.__TestCaseComponent__()
        testcomponentlist=t.__getcomponentList__()
        testcomp=testcomponentlist.get(TestStep.__getcomponentName__()).split('->')
        moduleName=testcomp[0]
        className=testcomp[1]
        methodName=testcomp[2]
        #利用python的反射机制
        m=__import__(moduleName)
        s=getattr(m, className) 
        k=getattr(s(), methodName) 
        k()
        
        