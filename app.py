from menu1 import menuPrincipal
from cliente import updateAllClients
from archivo import createFilesDirectory
import threading as thr
import time

createFilesDirectory()
def updating(): #Using tkinter for count 5 minutes before updating
    while True:
        updateAllClients()
        time.sleep(300)

def mainMenuCode():
    while True:
        menuPrincipal()

th_update = thr.Thread(target=updating,)
th_menu = thr.Thread(target=mainMenuCode)

th_update.start()
th_menu.start()





