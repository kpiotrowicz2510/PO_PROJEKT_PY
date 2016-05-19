from Window import *
from Swiat import Swiat
from Organizm import *

if __name__ == '__main__':
    mySwiat = Swiat(1,1)
    o = Organizm(mySwiat)
    o.posX = 1
    mySwiat.AddOrganizm(o)
    myWin = MyWindow()
    myWin.AddButton()
    Application().Run(myWin)
