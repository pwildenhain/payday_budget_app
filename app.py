import wx


class BudgetFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Payday Budget")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.account_name = wx.StaticText(panel, label="Transportation")
        sizer.Add(self.account_name, 0, wx.ALL, 5)

        self.tx_amount = wx.TextCtrl(panel)
        sizer.Add(self.tx_amount, 0, wx.ALL, 5)

        self.tx_comment = wx.TextCtrl(panel)
        sizer.Add(self.tx_comment, 0, wx.ALL, 5)

        btn = wx.Button(panel, label="Add Transaction")
        btn.Bind(wx.EVT_BUTTON, self.on_press)
        sizer.Add(btn, 0, wx.ALL, 5)

        panel.SetSizer(sizer)

        self.Show()

    def on_press(self, event):
        amount = self.tx_amount.GetValue()
        comment = self.tx_comment.GetValue()
        print(f"${amount} on {comment}") if amount else print(
            "You didn't type anything..."
        )


if __name__ == "__main__":
    app = wx.App()
    frame = BudgetFrame()
    app.MainLoop()
