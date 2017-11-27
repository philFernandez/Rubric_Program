import wx

class Mframe(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(Mframe, self).__init__(parent, *args, **kwargs)

        self.MakeMenu()

        # make sizer
        sizer = wx.BoxSizer()
        # make panel ; assign frame as parent
        self.panel = wx.Panel(self)

        wx.StaticText(self.panel, label='How Many Weighted Sections',
                               pos=(5, 10))

        # add panel to sizer
        sizer.Add(self.panel)
        # add text area to panel
        self.textArea = wx.TextCtrl(self.panel, value='',
                                    pos=(5, 30),
                                    size=(100, 30),
                                   style=wx.TE_PROCESS_ENTER)
        # go to function when user pressed enter in text box
        self.textArea.Bind(wx.EVT_TEXT_ENTER,self.OnEnterTextArea)

    def MakeMenu(self):
        # Menu bar =============================================
        menubar = wx.MenuBar()
        menu = wx.Menu()
        quit = menu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
        menubar.Append(menu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, quit)
        # ======================================================

    def OnQuit(self, event):
        self.Close()

    def OnEnterTextArea(self, event):
        # get number of sections from data in text box
        numberOfSections = self.textArea.GetValue()
        wx.StaticText(self.panel, label='Enter Section Names',
                     pos=(8, 85))

        pos = 120
        for n in range(int(numberOfSections)):
            wx.TextCtrl(self.panel, value='',
                       pos=(5, pos))
            pos+=35

app = wx.App()
frame = Mframe(None, title='Rubric Calculator', size=(700, 500))
frame.Show()
app.MainLoop()
