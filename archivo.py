import validaciones as v
import os
import json as j

def createFileDir():
    script_path = v.scriptPath()
    if not(os.path.exists('files')):
        os.makedirs(script_path)
    crearArchivoMensualidad(script_path)
    #later create clientes.json

def crearArchivoMensualidad(script_path):
    type_of_payment = {
    "Monthly": 430, 
    "Fortknight": 250, 
    "Week" : 130, 
    "Daily": 35
    }
    with open(script_path('files','mensualidad.json'), 'w') as file:
        file.write(j.dumps(type_of_payment))
    file.close()



