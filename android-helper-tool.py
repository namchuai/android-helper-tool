from Tkinter import *
import subprocess

class Application(Frame):
    def decreaseVolume(self):
        subprocess.call(['adb','shell','input','keyevent','25'])

    def increaseVolume(self):
        subprocess.call(['adb','shell','input','keyevent','24'])

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.decrease_volume = Button(self)
        self.decrease_volume["text"] = "Decrease Volume",
        self.decrease_volume["command"] = self.decreaseVolume

        self.decrease_volume.pack({"side": "left"})

        self.increase_volume = Button(self)
        self.increase_volume["text"] = "Increase Volume",
        self.increase_volume["command"] = self.increaseVolume

        self.increase_volume.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title("Android helper tool")
app = Application(master=root)
app.mainloop()
root.destroy()
