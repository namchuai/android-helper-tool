from Tkinter import *
import subprocess

class Application(Frame):
    def decreaseVolume(self):
        subprocess.call(['adb','shell','input','keyevent','25'])

    def increaseVolume(self):
        subprocess.call(['adb','shell','input','keyevent','24'])

    def dumpLog(self):
        subprocess.call(['adb','shell','am','broadcast', '-a','com.honda.auto.diagnostics.SCREENSHOT'])

    def triggerDiagnostic(self):
        subprocess.call(['adb','shell','am','start', '-n','com.honda.auto.diagnostics/.dealer.MainActivity'])

    def createWidgets(self):
        self.increase_volume = Button(self)
        self.increase_volume["text"] = "Volume up",
        self.increase_volume["command"] = self.increaseVolume

        self.increase_volume.pack(padx=10, ipady=10, side=LEFT)

        self.triger_diagnostic = Button(self)
        self.triger_diagnostic["text"] = "Open Diagnostic",
        self.triger_diagnostic["command"] = self.triggerDiagnostic

        self.triger_diagnostic.pack(padx=10, ipady=10, side=LEFT)

        self.decrease_volume = Button(self)
        self.decrease_volume["text"] = "Volume down",
        self.decrease_volume["command"] = self.decreaseVolume

        self.decrease_volume.pack(padx=10, ipady=10, side=RIGHT)

        self.dump_log = Button(self)
        self.dump_log["text"] = "Dump HARS log",
        self.dump_log["command"] = self.dumpLog

        self.dump_log.pack(padx=10, ipady=10, side=RIGHT)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title("Android helper tool")
app = Application(master=root)
app.mainloop()
root.destroy()
