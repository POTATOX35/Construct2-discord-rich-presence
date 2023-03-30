import time
import psutil
from pypresence import Presence
import pyautogui
from functions import *

import wmi
  

f = wmi.WMI()
  


client_id ="1074262494740230164"
RPC = Presence(client_id)
RPC.connect()
lastname = ''
flag =0    
    
for process in f.Win32_Process():
    if "Construct2.exe" == process.Name:
        if (lastname != project_name):
            RPC.connect()
            lastname = project_name
            RPC.update(
            state="Editing " + project_name,
            large_image="construct",
            large_text="Playing Construct 2",
            start=int(time.time())
        )
        break
  
if flag == 0:
    RPC.clear()
