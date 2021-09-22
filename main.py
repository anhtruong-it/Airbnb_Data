import wx


class Gu(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(1200, 800))
        self.lists = ['Suburb', 'Chart', 'Reviews', 'Dashboard'] # title name
        self.gui_design()

    # add images to each button
    def getIconButton(self, width, height, path):
        bitmap = wx.Bitmap(path)
        iconButtons = wx.ImageFromBitmap(bitmap)
        iconButtons = iconButtons.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(iconButtons)
        return result

    def gui_design(self):
        # add icon to application
        self.icon = wx.Icon('airbnb.png', wx.BITMAP_TYPE_PNG)
        self.SetIcon(self.icon)

        # create Title
        self.pnl = wx.Panel(self, size=(1200, 800))
        self.row = wx.BoxSizer(wx.VERTICAL)
        self.title = wx.StaticText(self.pnl, label="Welcome to Airbnb Sydney Data")
        self.font = self.title.GetFont()
        self.font.PointSize += 16
        self.font = self.font.Bold()
        self.title.SetFont(self.font)
        self.row.Add(self.title, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=0)

        # create Menu
        self.menu = wx.Menu()
        self.helpMenu = wx.Menu()
        self.aboutItem = self.helpMenu.Append(wx.ID_ABOUT)
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.helpMenu, "&Help")
        self.SetMenuBar(self.menuBar)

        # create Buttons
        self.sizer = wx.GridBagSizer(wx.VERTICAL)

        self.buttonHome = wx.Button(self.pnl, label="", size=(50, 50))
        self.iconButton = self.getIconButton(45, 45, 'home.png')
        self.buttonHome.SetBitmap(self.iconButton)

        self.buttonPLot = wx.Button(self.pnl, label="", size=(50, 50))
        self.iconButton = self.getIconButton(45, 45, 'plot.jpg')
        self.buttonPLot.SetBitmap((self.iconButton))

        self.buttonFind = wx.Button(self.pnl, label="", size=(50, 50))
        self.iconButton = self.getIconButton(45, 45, 'find.jpg')
        self.buttonFind.SetBitmap((self.iconButton))

        self.buttonListing = wx.Button(self.pnl, label="", size=(50, 50))
        self.iconButton = self.getIconButton(45, 45, 'location.png')
        self.buttonListing.SetBitmap((self.iconButton))

        self.labelDate1 = wx.StaticText(self.pnl, label="Date start:")
        self.font = self.labelDate1.GetFont()
        self.font = self.font.Bold()
        self.labelDate1.SetFont(self.font)
        self.boxDate1 = wx.TextCtrl(self.pnl, size=(100, 20))

        self.labelDate2 = wx.StaticText(self.pnl, label="Date finish:")
        self.font = self.labelDate2.GetFont()
        self.font = self.font.Bold()
        self.labelDate2.SetFont(self.font)
        self.boxDate2 = wx.TextCtrl(self.pnl, size=(100, 20))

        self.labelKeyword = wx.StaticText(self.pnl, label="Enter keywords:")
        self.font = self.labelKeyword.GetFont()
        self.font = self.font.Bold()
        self.labelKeyword.SetFont(self.font)
        self.boxKeywords = wx.TextCtrl(self.pnl, size=(100, 20))

        self.contentTitle = wx.StaticText(self.pnl, label='Dashboard')
        self.font = self.contentTitle.GetFont()
        self.font.PointSize += 16
        self.font = self.font.Bold()
        self.contentTitle.SetFont(self.font)

        self.sizer.Add(self.buttonHome, pos=(1, 0), flag=wx.EXPAND | wx.RIGHT, border=0)
        self.sizer.Add(self.labelDate1, pos=(0, 3), flag=wx.EXPAND | wx.RIGHT, border=10)
        self.sizer.Add(self.boxDate1, pos=(0, 4), flag=wx.EXPAND | wx.RIGHT, border=10)
        self.sizer.Add(self.labelDate2, pos=(0, 6), flag=wx.EXPAND | wx.RIGHT, border=10)
        self.sizer.Add(self.boxDate2, pos=(0, 7), flag=wx.EXPAND | wx.RIGHT, border=10)
        self.sizer.Add(self.labelKeyword, pos=(0, 9), flag=wx.EXPAND | wx.RIGHT, border=10)
        self.sizer.Add(self.boxKeywords, pos=(0, 10), flag=wx.EXPAND | wx.RIGHT, border=10)
        self.sizer.Add(self.buttonPLot, pos=(2, 0), flag=wx.EXPAND | wx.RIGHT, border=0)
        self.sizer.Add(self.contentTitle, pos=(1, 3), flag=wx.EXPAND | wx.RIGHT, border=0)
        self.sizer.Add(self.buttonListing, pos=(3, 0), flag=wx.EXPAND | wx.RIGHT, border=0)
        self.sizer.Add(self.buttonFind, pos=(4, 0), flag=wx.EXPAND | wx.RIGHT, border=0)
        self.row.Add(self.sizer, 12, wx.ALIGN_LEFT | wx.TOP)

        self.Bind(wx.EVT_BUTTON, self.pressPlot, self.buttonPLot)
        self.Bind(wx.EVT_BUTTON, self.pressHome, self.buttonHome)
        self.Bind(wx.EVT_BUTTON, self.pressSuburb, self.buttonListing)
        self.Bind(wx.EVT_BUTTON, self.pressComment, self.buttonFind)

        self.pnl.SetSizerAndFit(self.row)
        self.Show(True)

    def pressPlot(self, event):
        self.contentTitle.Label = str(self.lists[1])

    def pressHome(self, event):
        self.contentTitle.Label = str(self.lists[3])

    def pressSuburb(self, event):
        self.contentTitle.Label = str(self.lists[0])

    def pressComment(self, event):
        self.contentTitle.Label = str(self.lists[2])


app = wx.App()
frame = Gu(None, -1, 'Airbnb Sydney Data')

app.MainLoop()
