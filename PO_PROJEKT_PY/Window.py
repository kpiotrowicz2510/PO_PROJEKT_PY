import wpf
from System.Windows import Application, Window, Thickness
from System.Windows.Controls import Button, Grid, Label
from System.Windows.Media import SolidColorBrush, Color

class MyWindow(Window):
    def __init__(self):
         wpf.LoadComponent(self, 'PO_PROJEKT_PY.xaml')
    def ChangeButton(self, id, r,g,b):
        m = self.mgrid.Children[id]
        m.Background = SolidColorBrush(Color.FromRgb(r,g,b))
    def Button_Click(self, sender, e):
        #name = sender.Name
        #self.lab.Content += name
        #m = self.mgrid.Children[0]
        #m.Background = SolidColorBrush(Color.FromRgb(255,0,0))
        #ajjj
        return True
    def AddOrgMonit(self):
        return True
    def AddButton(self):
        self.sizeX = 10
        self.sizeY = 10
        self.bgrid = Grid()
        self.lab = Label()
        self.lab.Content = "Hello"
        self.bgrid.AddChild(self.lab)
        self.mgrid = Grid()
        self.MyGrid.AddChild(self.bgrid)
        self.MyGrid.AddChild(self.mgrid)
        for j in range(self.sizeY):
            for i in range(self.sizeX):
                self.myButton = Button()
                self.myButton.Click += self.Button_Click
                self.myButton.Name = "a".Insert(1,str((self.sizeX*self.sizeY)-(j*self.sizeX + i)))
                #self.myButton.Name = str(j*self.sizeY + self.sizeX)
                self.myButton.Height = 20
                self.myButton.Width = 20
                self.myButton.Background = SolidColorBrush(Color.FromRgb(0,0,0))
                self.myButton.Margin = Thickness(0,0,i*40,j*40)
                #self.myButton.Padding=new Thickness(
                self.myButton.AddText("Boniacz")
                self.mgrid.AddChild(self.myButton)