import wx
import subprocess
from speak import *
import time

filenames = ["faculty.png"]

class TestFrame(wx.Frame):
    def __init__(self): 
        wx.Frame.__init__(self, None, -1, 'My Python App',size=(1500, 760))

        image = wx.Image('faculty.png', wx.BITMAP_TYPE_ANY)
        w = image.GetWidth()
        h = image.GetHeight()
        image = image.Scale(w/1.4, h/1.4)#2 缩小图像

        panel = wx.Panel(self, -1)
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        self.bmp = wx.StaticBitmap(panel,-1,temp,pos=(0, 0),size=size)

        self.button = wx.Button(panel, -1, "1", pos=(50, 700))
        self.Bind(wx.EVT_BUTTON, self.OnClickFemale, self.button)
        self.button.SetDefault()

        self.button2 = wx.Button(panel, -1, "1", pos=(100, 700))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button2)
        self.button3 = wx.Button(panel, -1, "1", pos=(300, 700))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button3)
        self.button4 = wx.Button(panel, -1, "1", pos=(500, 700))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button4)
        self.button5 = wx.Button(panel, -1, "1", pos=(700, 700))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button5)
        self.button6 = wx.Button(panel, -1, "1", pos=(900, 700))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button6)

    def OnClick(self, event):
        content = "How to you spell your name?"
        try:
            subprocess.call(["python", "speak.py"])
        except:
            self.button2.SetLabel("Error")

        self.button3.SetLabel("Clicked")

    def OnClickFemale(self, event):
        self.button.SetLabel("Clicked")

if __name__ == '__main__':

    app = wx.App()
    frm = TestFrame()
    frm.Show()


    app.MainLoop()
