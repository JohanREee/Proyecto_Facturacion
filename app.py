from menu1 import menuPrincipal
from cliente import *
from archivo import createFilesDirectory
from producto import n_factura_iterate
from colorama import Fore
import time
import threading as thr

update = thr.Event()

loadAllClients()
def updating(): 
    value = 0
    while True:
        value +=1
        if value == 20:
            updateAllClients(lista_clientes)
            value = 0
        if update.is_set():
            break
        time.sleep(1) 
    
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

print(Fore.RESET)

th_update.join()
th_menu.join()





