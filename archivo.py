import validaciones as v
import os
import json as j

def createFilesDirectory():
    if not(os.path.exists('files')):
        os.makedirs(v.scriptPath('files'))
    crearArchivoMensualidad(v.scriptPath('files','mensualidad.json'))
    crearArchivoProductos(v.scriptPath('files','nombre_productos.json'))
    #later create clientes.json

def crearArchivoMensualidad(script_path):
    type_of_payment = {
    "Monthly": 430, 
    "Fortknight": 250, 
    "Week" : 130, 
    "Daily": 35
    }
    with open(script_path, 'w') as file:
        file.write(j.dumps(type_of_payment,indent=4))
    file.close()

def crearArchivoProductos(script_path):
    datos_productos = {
    "Libreados": {
        "Whey Protein ELV": 460,
        "Isolate Protein Rule 1": 440,
        "Whey Protein RN": 455,
        "Rule 1 Mass Gainer": 255,
        "King Mass RN": 240,
        "Dymatize Mass Gainer": 250
    },
    "Pastilla": {
        "Tribulus RN": 10,
        "Animal Pak": 40,
        "Tribulus My Protein": 11,
        "ON Creatine Capsules": 40,
        "EVL Creatine 1000": 40
    },
    "Scoops": {
        "C4": 45,
        "Psychotic": 50,
        "Micronozed L Glutamine": 45,
        "Creatina RN": 23,
        "Creatina Muscle Tech": 25,
        "Creatina Right Nutrition": 20,
        "Creatinea Rule 1": 22
    },
    "Tarros": {
        "C4": 1500,
        "Psychotic": 1600,
        "Micronized L Glutamine": 1550,
        "Tribulus RN": 720,
        "Tribulus My Protein": 800,
        "Barra Magnesio": 200,
        "Animal Pak": 1950,
        "Creatina RN": 1100,
        "Creatina Muscle Tech": 1200,
        "Creatina Right Nutrition": 950,
        "Creatina Rule 1": 1000
    }
}
    with open(script_path, 'w') as file:
        file.write(j.dumps(datos_productos,indent=4))
    file.close()


