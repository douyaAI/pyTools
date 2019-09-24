import wx

app = wx.App(False)

frame = wx.Frame(None, wx.ID_ANY, "Hello, World!")  #这是一个顶层的window
frame.Show(True)    #显示这个frame
app.MainLoop()
