from pywinauto import application
from pywinauto import timings
import time
import os, sys
import win32com.shell.shell as shell
import subprocess


app = application.Application()
app.start("C:/KiwoomFlash3/bin/nkministarter.exe")

title = "번개3 Login"
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys('xxxx') # password1

cert_ctrl = dlg.Edit3
cert_ctrl.SetFocus()
cert_ctrl.TypeKeys('yyyy!!') # password2

btn_ctrl = dlg.Button0
btn_ctrl.Click()

time.sleep(50)
os.system("taskkill /im khmini.exe")