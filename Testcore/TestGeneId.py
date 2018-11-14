#encoding:utf-8
import uuid
class TestGeneid:
    id=0
    def getuuid(self):
        self.id=uuid.uuid1()
        return self.id
    def resetid(self):
        self.id=0
    