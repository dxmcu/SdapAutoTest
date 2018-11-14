#encoding:utf-8
#encoding:utf-8
import xlwt
import time
from Testcore.TestCase import TestCase
from Testcore.TestStep import TestStep
from Testcore.TestSuite import TestSuite
from Testcore.TestGeneId import TestGeneid
'''
Created on 2016-11-28

@author: xianqingchen
'''
class TestReport:
    t=time.strftime('%Y%m%d',time.localtime(time.time()))
    #设置单元格样式 
    def set_style(self,name,height,bold=False):
        # 初始化样式
        style = xlwt.XFStyle() 
        # 为样式创建字体
        font = xlwt.Font() 
        font.name = name 
        font.bold = bold
        font.color_index = 4
        font.height = height
        # borders= xlwt.Borders()
        # borders.left= 6
        # borders.right= 6
        # borders.top= 6
        # borders.bottom= 6
        style.font = font
        # style.borders = borders
        return style
    #根据测试执行计划批次编号（code,20161017-01） 生成对应测试报告数据文件 编号相同则覆盖文件
    def __createTestReport__(self,testplan):
        #创建测试报告文件
        PlanRunNo=str(testplan.__gettestplanrunNo__())
        if PlanRunNo=='':
            print "测试计划执行编号为空"
            PlanRunNo=self.t+'001'
        reportname=PlanRunNo+'.xls'
        ReportFile=xlwt.Workbook()
        #创建多个测试报告sheet页名称
        ReportFile.add_sheet(u'测试节点树',cell_overwrite_ok=True)
        ReportFile.add_sheet(u'测试计划', cell_overwrite_ok=True)
        ReportFile.add_sheet(u'测试场景', cell_overwrite_ok=True)
        ReportFile.add_sheet(u'测试用例', cell_overwrite_ok=True)
        ReportFile.add_sheet(u'测试步骤', cell_overwrite_ok=True)
        #写入测试节点树表头
        wr_tree = ReportFile.get_sheet(0)
        row0=[u'节点ID',u'父节点ID',u'名称',u'类型']
        #生成测试节点树的表头
        for i in range(0,len(row0)):
            wr_tree.write(0,i,row0[i],TestReport().set_style('Times New Roman',220,True))
        #写入测试计划表头
        wr_plan=ReportFile.get_sheet(1)
        row1=[u"编号", u"名称", u"描述", u"执行开始时间", u"执行结束时间", u"执行结果"]
        #生成测试计划的表头
        for i in range(0,len(row1)):
            wr_plan.write(0,i,row1[i],TestReport().set_style('Times New Roman',220,True))
        #写入测试场景表头
        wr_suite=ReportFile.get_sheet(2)
        row2=[u"ID", u"名称", u"描述", u"前置条件", u"执行开始时间", u"执行结束时间", u"执行结果"]
        #生成测试场景的表头
        for i in range(0,len(row2)):
            wr_suite.write(0,i,row2[i],TestReport().set_style('Times New Roman',220,True))
        #写入测试用例表头
        wr_case=ReportFile.get_sheet(3)
        row3=[u"ID", u"所属测试场景ID", u"名称", u"描述", u"前置条件", u"执行开始时间",u"执行结束时间", u"执行结果"]
        #生成测试用例的表头
        for i in range(0,len(row3)):
            wr_case.write(0,i,row3[i],TestReport().set_style('Times New Roman',220,True))
        #写入测试步骤表头
        wr_step=ReportFile.get_sheet(4)
        row4=[u"ID", u"所属测试用例ID", u"步骤名称", u"调用业务组件名称", u"输入数据",u"预期数据", u"执行开始时间", u"执行结束时间", u"执行结果", u"异常信息", u"错误截图"]
        #生成测试步骤的表头
        for i in range(0,len(row4)):
            wr_step.write(0,i,row4[i],TestReport().set_style('Times New Roman',220,True))
        #测试节点树，写入测试计划节点
        p=1
        wr_tree.write(p,0,"0")
        wr_tree.write(p,1,"-1")
        wr_tree.write(p,2,testplan.__gettestplanname__())
        wr_tree.write(p,3,"0")
        p=p+1

        #写入测试计划执行信息
        #编号
        wr_plan.write(1,0,testplan.__gettestplanrunNo__())
        #名称
        wr_plan.write(1,1,testplan.__gettestplanname__())
        #描述
        wr_plan.write(1,2,testplan.__gettestplanname__())
        #执行开始时间
        wr_plan.write(1,3,testplan.__gettestplanstarttime__())
        #执行结束时间
        wr_plan.write(1,4,testplan.__gettestplanendtime__())
        #执行结果
        wr_plan.write(1,5,testplan.__getresult__())
        #写入测试场景、测试用例、测试步骤执行信息
        testsuiteList=testplan.__gettestsuiteList__()
        testsuite=TestSuite()
        testcase=TestCase()
        teststep=TestStep()
        j=0
        k=0
        for i in range(0,len(testsuiteList)):
            #获取测试场景
            testsuite=testsuiteList[i]
            #测试节点树，写入测试场景节点信息
            wr_tree.write(p,0,str(testsuite.__getuid__()))
            wr_tree.write(p,1,"0")
            wr_tree.write(p,2,testsuite.__gettestsuitename__())
            wr_tree.write(p,3,"1")
            p=p+1
            #写入测试场景执行信息
            #ID
            wr_suite.write(i+1,0,str(testsuite.__getuid__()))
            #名称
            wr_suite.write(i+1,1,testsuite.__gettestsuitename__())
            #描述
            wr_suite.write(i+1,2,testsuite.__gettestsuitedesc__())
            #前置条件
            wr_suite.write(i+1,3,testsuite.__getrequirement__())
            #执行开始时间
            wr_suite.write(i+1,4,testsuite.__getstarttime__())
            #执行结束时间
            wr_suite.write(i+1,5,testsuite.__getendtime__())
            #执行结果
            wr_suite.write(i+1,6,testsuite.__getresult__())
            #写入测试场景下的测试用例执行信息
            testcaseList=testsuite.__gettestcaseList__()
            for n in range(0,len(testcaseList)):
                #获取测试用例
                testcase=testcaseList[n]
                #测试节点树，写入测试用例节点信息
                wr_tree.write(p,0,str(testcase.__getId__()))
                wr_tree.write(p,1,"1")
                wr_tree.write(p,2,testcase.__gettestcasename__())
                wr_tree.write(p,3,"2")
                p=p+1
                #写入测试用例执行信息
                #ID", "所属测试场景ID", "名称", "描述", "前置条件", "执行开始时间","执行结束时间", "执行结果"
                wr_case.write(n+1,0,str(testcase.__getId__()))
                wr_case.write(n+1,1,str(testcase.__gettestsuiteId__()))
                wr_case.write(n+1,2,testcase.__gettestcasename__())
                wr_case.write(n+1,3,testcase.__getdec__())
                wr_case.write(n+1,4,testcase.__getrequirement__())
                wr_case.write(n+1,5,testcase.__getstarttime__())
                wr_case.write(n+1,6,testcase.__getendtime__())
                wr_case.write(n+1,7,testcase.__getresult__())
                #写入测试用例下测试步骤执行信息
                teststepList=testcase.__gettestcaseStepList__()
                for m in range(0,len(teststepList)):
                    #获取测试步骤
                    teststep=teststepList[m]
                    #测试步骤执行信息
                    '''ID, 所属测试用例ID, 步骤名称, 调用业务组件名称, 输入数据,预期数据, 
                                                 执行开始时间, 执行结束时间, 执行结果, 异常信息, 错误截图'''
                    wr_step.write(m+1,0,str(teststep.__getId__()))
                    wr_step.write(m+1,1,str(teststep.__gettestcaseId__()))
                    wr_step.write(m+1,2,teststep.__gettestcasename__())
                    wr_step.write(m+1,3,teststep.__getcomponentName__())
                    wr_step.write(m+1,4,teststep.__getinputdata__())
                    wr_step.write(m+1,5,teststep.__getexpectData__())
                    wr_step.write(m+1,6,teststep.__gettestcasestepstarttime__())
                    wr_step.write(m+1,7,teststep.__gettestcasestependtime__())
                    wr_step.write(m+1,8,teststep.__getresult__())
                    wr_step.write(m+1,9,teststep.__getErrorMessage__())
                    wr_step.write(m+1,10,teststep.__getErrorpic__())
        #保存文件
        ReportFile.save(reportname)
        