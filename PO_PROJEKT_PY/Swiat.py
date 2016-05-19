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
    def UpdateLoop(self, key):
        self.WykonajTure(1)
        self.UpdateLog()
        self.RysujSwiat()
    def WykonajTure(self, key):
        return True
    def RysujSwiat(self):
        return True
    def UpdateLog(self):
        return True

