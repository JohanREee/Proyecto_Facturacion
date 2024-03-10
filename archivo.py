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
        file.write(j.dumps(type_of_payment))
    file.close()

def crearArchivoProductos(script_path):
    datos_productos = {
    "Productos_libreados" : {
        "WheyProteinELV" : 460,
        "IsolateProteinRule1" : 440,
        "WheyProteinRN" : 455,
        "Rule1MassGainer" : 255,
        "KingMassRN" : 240,
        "DymatizeMassGainer" : 250
        
    },
    "Productos_pastilla": {
        "TribulusRN" : 10, 
        "AnimalPak" : 40,
        "Tribulus MyProtein" : 11,
        "ONCreatineCapsules" : 40,
        "EVLCreatine1000" : 40
    },

    "Productos_scoops" : {
        "C4" : 45,
        "Psychotic" : 50,
        "MicronozedLGlutamine" : 45,
        "CreatinaRN" : 23,
        "CreatinaMuscleTech" : 25,
        "CreatinaRightNutrition" : 20,
        "CreatineaRule1" : 22
    },
    "Productos_Tarros_Total" : {
        "C4_Tarro" : 1500,
        "Psychotic_Tarro" : 1600,
        "MicronizedLGlutamine_Tarro" : 1550,
        "TribulusRN_Tarro" : 720,
        "TribulusMyProtein_Tarro" : 800,
        "Barra_Magnesio" : 200,
        "AnimalPak_Tarro" : 1950,
        "CreatinaRN_Tarro" : 1100,
        "CreatinaMuscleTech_Tarro" : 1200,
        "CreatinaRightNutrition_Tarro" : 950,
        "CreatinaRule1_Tarro" : 1000
    }
}
    with open(script_path, 'w') as file:
        file.write(j.dumps(datos_productos))
    file.close()


