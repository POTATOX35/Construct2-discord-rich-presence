import time
import psutil
from pypresence import Presence
import pyautogui
from functions import *

  


client_id ="1074262494740230164"
RPC = Presence(client_id)
RPC.connect()
lastname = ''

    
while True:
    
    if ("Construct2.exe" in (i.name() for i in psutil.process_iter())) == True:
        if (lastname != project_name):
            RPC.connect()
            lastname = project_name
            RPC.update(
            state="Editing " + project_name,
            large_image="construct",
            large_text="Playing Construct 2",
            start=int(time.time())
              )
    else:
        RPC.clear()
