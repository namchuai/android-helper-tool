import Tkinter as tk
import subprocess

# DEFINE CONSTANTS HERE
version = 0.1
versionTitle = "v" + str(version)
winTitle = "Android helper tool " + versionTitle

CONST_LOG_SRC_DIR = "/logging/HARS_Reports"
CONST_HOME_DIR = "~/"

# FUNCTION GOES HERE
def decreaseVolume():
    subprocess.call(['adb','shell','input','keyevent','25'])

def increaseVolume():
    subprocess.call(['adb','shell','input','keyevent','24'])

def dumpLog():
    subprocess.call(['adb','shell','am','broadcast', '-a','com.honda.auto.diagnostics.SCREENSHOT'])

def triggerDiagnostic():
    subprocess.call(['adb','shell','am','start', '-n','com.honda.auto.diagnostics/.dealer.MainActivity'])

def pullAllLog():
    subprocess.call(['adb', 'pull', CONST_LOG_SRC_DIR, CONST_HOME_DIR])

def clearLogCatBuffer():
    subprocess.call(['adb', 'logcat', '-c'])

root = tk.Tk()

root.title(winTitle)

btnDecreaseVolume = tk.Button(root, text="Decrease volume", width=25, command=decreaseVolume)
btnIncreaseVolume = tk.Button(root, text="Increase volume", width=25, command=increaseVolume)
btnOpenDiagnostic = tk.Button(root, text="Open diagnostics", width=25, command=triggerDiagnostic)
btnDumpLog = tk.Button(root, text="Dump log", width=25, command=dumpLog)
btnPullLog = tk.Button(root, text="Pull log", width=25, command=pullAllLog)
btnClearLogcatBuffer = tk.Button(root, text="Clear logcat buffer", width=25, command=clearLogCatBuffer)

btnDecreaseVolume.pack()
btnIncreaseVolume.pack()
btnOpenDiagnostic.pack()
btnDumpLog.pack()
btnPullLog.pack()
btnClearLogcatBuffer.pack()

root.mainloop()