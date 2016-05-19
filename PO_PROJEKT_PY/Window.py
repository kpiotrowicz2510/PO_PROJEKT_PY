import wpf
from System.Windows import Application, Window, Thickness
from System.Windows.Controls import Button, Grid, Label

class MyWindow(Window):
    def __init__(self):
         wpf.LoadComponent(self, 'PO_PROJEKT_PY.xaml')
    def Button_Click(self, sender, e):
        name = sender.Name
        self.lab.Content += name
        #id 
        #self.Content.Children[1].Text += sender.Name
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
                self.myButton.Name = "a".Insert(1,str(12345))
                #self.myButton.Name = str(j*self.sizeY + self.sizeX)
                self.myButton.Height = 20
                self.myButton.Width = 20
                self.myButton.Margin = Thickness(0,0,i*40,j*40)
                #self.myButton.Padding=new Thickness(
                self.myButton.AddText("Boniacz")
                self.mgrid.AddChild(self.myButton)