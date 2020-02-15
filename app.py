import wx


class BudgetPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        top_options_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.add_account_btn = wx.Button(self, label="Add Account")
        self.add_account_btn.Bind(wx.EVT_BUTTON, self.handle_add_account)
        top_options_sizer.Add(self.add_account_btn, 0, wx.ALL, 5)

        self.record_payday_btn = wx.Button(self, label="Record Payday")
        self.record_payday_btn.Bind(wx.EVT_BUTTON, self.handle_record_payday)
        top_options_sizer.Add(self.record_payday_btn, 0, wx.ALL, 5)

        self.view_tx_history_btn = wx.Button(self, label="View Transaction History")
        self.view_tx_history_btn.Bind(wx.EVT_BUTTON, self.handle_view_tx_history)
        top_options_sizer.Add(self.view_tx_history_btn, 0, wx.ALL, 5)

        self.list_ctrl = wx.ListCtrl(
            self, size=(-1, 100), style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )

        self.list_ctrl.InsertColumn(0, "Category", width=150)
        self.list_ctrl.InsertColumn(1, "Name", width=150)
        self.list_ctrl.InsertColumn(2, "Budgeted Amount", width=150)
        self.list_ctrl.InsertColumn(3, "Curent Amount", width=150)
        self.list_ctrl.InsertColumn(4, "Transaction Amount", width=150)
        self.list_ctrl.InsertColumn(5, "Transaction Comment", width=150)
        self.list_ctrl.InsertColumn(6, "Add Transaction", width=150)
        self.list_ctrl.InsertColumn(7, "Modify Account", width=150)

        main_sizer.Add(top_options_sizer, 0, wx.ALL | wx.EXPAND)
        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND)

        self.SetSizer(main_sizer)

    def handle_add_account(self, event):
        print("New account added!")

    def handle_record_payday(self, event):
        print("$$ Cha-Ching $$")

    def handle_view_tx_history(self, event):
        print("Viewing Transactions")


class AppFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Payday Budget")
        panel = BudgetPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App()
    frame = AppFrame()
    app.MainLoop()
