import random
class Swiat:
    pressedKey = -1
    turaNumer = 0
    sRX = 30
    sRY = 30
    newId = 0

    def __init__(self, x , y):
        self.sRX = x
        self.sRY = y
        self.organizmy = []
        self.info = []
        return True
    def SetR(self,x,y):
        self.sRX = x
        self.sRY = y
    def SetWindow(self, wind):
        self.window = wind

    def AddOrganizm(self,org):
        x = random.randint(0,self.sRX)
        y = random.randint(0,self.sRY)
    def FreeSpace(self,x,y):
        ret = True
        for i in range(self.organizmy.count):
            if(self.organizmy[i].x==x and self.organizmy[i].y==y):
                ret=False
        return ret
    def UpdateLoop(self, key):
        self.WykonajTure(1)
        self.UpdateLog()
        self.RysujSwiat()
    def WykonajTure(self, key):
        return True
    def RysujSwiat(self):
        for i in range(self.organizmy.count):
            return True
        return True
    def UpdateLog(self):
        return True

