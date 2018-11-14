#encoding:utf-8
import ConfigParser,os
cf=ConfigParser.ConfigParser()
confile=os.path.abspath("..")+"\\Testcore\\baseconfig.ini"
cf.read(confile)
class GetTestConfig:
    @staticmethod
    def geturl():
        url=cf.get("url","TEST_ENV_URL")
        return url
    @staticmethod
    def getdb():
        host=cf.get("db", "DB_HOST")
        port=cf.get("db", "DB_PORT")
        user=cf.get("db", "DB_USERNAME")
        passwd=cf.get("db", "DB_PASSWORD")
        db=cf.get("db", "DB_BASEDATA")
        return host,port,user,passwd,db
    
        