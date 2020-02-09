import wx


class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Hello Bre!")
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        btn = wx.Button(panel, label="PRESS ME", pos=(5, 55))

        self.Show()


if __name__ == "__main__":
    app = wx.App()
    frame = MainWindow()
    app.MainLoop()
