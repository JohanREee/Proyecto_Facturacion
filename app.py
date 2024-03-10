from menu1 import menuPrincipal
from cliente import updateAllClients
import threading as thr
import time

def updating():
    while True:
        updateAllClients()
        time.sleep(300)

def mainMenuCode():
    while True:
        menuPrincipal()

th_update = thr.Thread(target=updating)
th_menu = thr.Thread(target=mainMenuCode)

th_update.start()
th_menu.start()





