#!/usr/bin/env python3
import wx

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(HelloFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)

        txt = wx.StaticText(panel, label='Hello, wxPython!')
        font = txt.GetFont()
        font.PointSize += 10
        font = font.Bold()
        txt.SetFont(font)

        txt2 = wx.StaticText(panel, label='Default')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txt, 0, wx.TOP | wx.CENTER, 25)
        sizer.Add(txt2, 0, wx.TOP | wx.CENTER, 15)
        panel.SetSizer(sizer)

        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText('Welcome to wxPython!')

    def makeMenuBar(self):
        file_menu = wx.Menu()
        hello_item = file_menu.Append(
            -1, '&Hello...\tCtrl+H',
            'Help string shown in status bar for this menu item'
        )
        file_menu.AppendSeparator()
        exit_item = file_menu.Append(wx.ID_EXIT)

        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT)

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, '&File')
        menu_bar.Append(help_menu, '&Help')

        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self.OnHello, hello_item)
        self.Bind(wx.EVT_MENU, self.OnExit, exit_item)
        self.Bind(wx.EVT_MENU, self.OnAbout, about_item)

    def OnExit(self, e):
        print('Hello, OnExit!')
        self.Close(True)

    def OnHello(self, e):
        wx.MessageBox('Hello again from wxPython!')

    def OnAbout(self, e):
        wx.MessageBox(
            'This is a wxPython hello world example',
            'About Hello World 2',
            wx.OK|wx.ICON_INFORMATION
        )

def main():
    app = wx.App()
    frame = HelloFrame(None, title='Hello World 2')
    frame.Show()
    app.MainLoop()
    print('Bye!')

if __name__ == "__main__":
    main()
