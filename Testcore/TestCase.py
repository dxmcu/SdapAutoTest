#encoding:utf-8
import xlrd 
from Testcore.TestGeneId import TestGeneid
from Testcore.TestStep import TestStep
from Testcore.TestCaseComponent import TestCaseComponent
class TestCase:        
    id1=TestGeneid().getuuid()
    #所属测试场景ID
    testsuiteId=0
    #测试用例名称
    testcasename=""
    #测试用例描述
    dec=""
    #前置条件
    requirement=""
    #作者
    createuser=""
    #创建时间
    createtime=""
    #执行开始时间
    starttime=""
    #执行结束时间
    endtime=""
    #执行结果
    result=0
    #定义用例执行步骤列表
    testcaseStepList= []
    #定义用例业务组件运行时返回值字典
    componentList=TestCaseComponent().__getcomponentList__()
    #加载测试用例配置文件
    def __TestCase__(self,filePath,testsuiteId):
        bk=xlrd.open_workbook(filePath)
        #获取测试用例描述的基本信息
        sh=bk.sheet_by_name(u'用例描述')
        try:
            self.__settestsuiteId__(testsuiteId)
            self.__setcreateuser__(sh.row_values(0)[1])
            self.__setcreatetime__(sh.row_values(0)[3])
            self.__settestcasename__(sh.row_values(1)[1])
            self.__setdec__(sh.row_values(2)[1])
            self.__setrequirement__(sh.row_values(3)[1])
        except xlrd.error_text_from_code:
            print "error_text_from_code"
        #获取用例执行步骤的sheet页
        sh=bk.sheet_by_name(u'用例执行步骤')
        ts=TestStep()
        try:
            ts.__settestcaseId__(sh.row_values(1)[0])
            ts.__settestcasename__(sh.row_values(1)[1])
            ts.__setcomponentName__(sh.row_values(1)[2])
            ts.__setinputdata__(sh.row_values(1)[3])
            ts.__setexpectData__(sh.row_values(1)[4])
            ts.__setisrun__(sh.row_values(1)[5])
        except xlrd.error_text_from_code:
            print "error_text_from_code"
        self.testcaseStepList.append(ts)
#定义所有属性的获取设置方法
    def __setId1__(self,id1):
        self.id1=id1
    def __getId__(self):
        return self.id1
    def __settestsuiteId__(self,testsuiteId):
        self.testsuiteId=testsuiteId
    def __gettestsuiteId__(self):
        return self.testsuiteId
    def __settestcasename__(self,testcasename):
        self.testcasename=testcasename
    def __gettestcasename__(self):
        return self.testcasename
    def __setdec__(self,dec):
        self.dec=dec
    def __getdec__(self):
        return self.dec
    def __setcreateuser__(self,createuser):
        self.createuser=createuser
    def __getcreateuser__(self):
        return self.createuser            
    def __setcreatetime__(self,createtime):
        self.createtime=createtime
    def __getcreatetime__(self):
        return self.createtime  
    def __setstarttime__(self,starttime):
        self.starttime=starttime
    def __getstarttime__(self):
        return self.starttime       
    def __setendtime__(self,endtime):
        self.endtime=endtime
    def __getendtime__(self):
        return self.endtime  
    def __setresult__(self,result):
        self.result=result
    def __getresult__(self):
        return self.result 
    def __settestcaseStepList__(self,testcaseStepList):
        self.testcaseStepList=testcaseStepList
    def __gettestcaseStepList__(self):
        return self.testcaseStepList
    def __setcomponentList__(self,componentList):
        self.componentList=componentList
    def __getcomponentList__(self):
        return self.componentList  
    def __setrequirement__(self,requirement):
        self.requirement=requirement
    def __getrequirement__(self):
        return self.requirement   
         
    
    