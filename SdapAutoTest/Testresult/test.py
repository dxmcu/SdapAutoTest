#encoding:utf-8
import os
from Testresult.TestReport import TestReport
from Testcore.TestPlan import TestPlan
if __name__ == '__main__':
    p=os.path.abspath("..")+u"\\Testplan\\测试执行计划.xls"
    testplan=TestPlan()
    testplan.__TestPlan__(p)
    TestReport().__createTestReport__(testplan)