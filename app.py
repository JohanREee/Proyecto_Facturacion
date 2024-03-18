from menu1 import menuPrincipal
from cliente import updateAllClients, loadAllClients
from archivo import createFilesDirectory
import time
import threading as thr

update = thr.Event()

loadAllClients()

def updating(): #Using tkinter for count 5 minutes before updating
    value = 0
    while True:
        value +=1
        if value == 30:
            updateAllClients()
            value = 0
        if update.is_set():
            break
        time.sleep(2) 
    
def mainMenuCode():####
    createFilesDirectory()
    while True:
        number = menuPrincipal()
        if number == 11:break
    update.set()

th_update = thr.Thread(target=updating)
th_menu = thr.Thread(target=mainMenuCode)

th_update.start()
th_menu.start()

th_update.join()
th_menu.join()





