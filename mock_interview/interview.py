import wx
import subprocess
from speak import *
import time

filenames = ["faculty.png"]
figure_path = "./pic/"
figures = [
        figure_path+"faculty.png",
        figure_path+"Jessica_talk.png",
        figure_path+"Alan_talk.png",
        figure_path+"Lucas_talk.png",
        figure_path+"John_talk.png",
        figure_path+"Stefan_talk.png",
        figure_path+"Robert_talk.png"
        ]
w_scale = 1.45
h_scale = 1.4

class TestFrame(wx.Frame):
    def __init__(self): 
        self.index = 0
        wx.Frame.__init__(self, None, -1, 'My Python App',size=(1400, 760))

        image = wx.Image(figures[0], wx.BITMAP_TYPE_ANY)
        w = image.GetWidth()
        h = image.GetHeight()
        image = image.Scale(w/w_scale, h/h_scale) # Scale Image 

        panel = wx.Panel(self, -1)
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        self.bmp = wx.StaticBitmap(panel,-1,temp,pos=(0, 0),size=size)

        self.button = wx.Button(panel, -1, "1", pos=(50, 700))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

        panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

    def getVoice(self):
        # 0 for male voice, 1 for female voice
        return 1 if self.index == 1 else 0

    def changePerson(self, kc):
        self.index = int(chr(kc))
        image = wx.Image(figures[self.index], wx.BITMAP_TYPE_ANY)
        w = image.GetWidth()
        h = image.GetHeight()
        image = image.Scale(w/w_scale, h/h_scale) # Scale Image 
        self.bmp.SetBitmap(wx.BitmapFromImage(image))
        self.Show()

    def OnKeyDown(self, event):
        kc=event.GetKeyCode()
        if ord('0') <= kc <= ord('6'):
            self.changePerson(kc)
        elif ord('t') == kc or ord('T') == kc:
            self.askTeaching()
        elif ord('i') == kc or ord('I') == kc:
            self.introduction()

    def introduction(self):
        content = "Hello ChongNon, thank you for applying to our program!"
        self.speak(content)

    def askTeaching(self):
        content = "Hello, ChongNon! Thank you for applying to our program. How to you spell your name?"
        subprocess.call(["python", "speak.py", content, str(self.getVoice())])

    def OnClick(self, event):
        content = "How to you spell your name?"
        subprocess.call(["python", "speak.py"])

    def speak(self, content):
        subprocess.call(["python", "speak.py", content, str(self.getVoice())])

if __name__ == '__main__':

    app = wx.App()
    frm = TestFrame()
    frm.Show()


    app.MainLoop()
