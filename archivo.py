import os
import json as j

def decoratorFile(function):
    def wrap(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except FileNotFoundError:
            print('Archivo no encontrado')
            return None
        else:
            return result
    return wrap

@decoratorFile
def readFile(file_name):
    return open(file_name, 'r')

def scriptPath(*dirs):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, *dirs) 
    
def loadJSONProduct(producto_clasificacion): 
    script_path = scriptPath('files','nombre_productos.json')
    file = readFile(script_path) 
    if file is None:
        createFilesDirectory()
        dict_product_loaded = loadJSONProduct(producto_clasificacion)
        return dict_product_loaded
    j_file = j.load(file)
    file.close()
    producto_clasificacion_cargado = j_file[producto_clasificacion] 
    dict_producto_cargado = {producto : producto_clasificacion_cargado[producto] for producto in producto_clasificacion_cargado}
    return dict_producto_cargado###

def loadJSONMonthlyPayment():####
    script_path = scriptPath('files', 'mensualidad.json')
    file = readFile(script_path)
    if file is None:
        return None
    j_file = j.load(file)
    month = j_file["Monthly"]
    fortknight = j_file["Fortknight"]
    week = j_file["Week"]
    day = j_file["Daily"]
    file.close()
    return [month,fortknight,week,day]###

def fileMonthlyPayment(type_of_payment):
    mensualidad = loadJSONMonthlyPayment()
    if mensualidad is None:
        return None, None
    match type_of_payment:
        case 'month':
            return mensualidad[0], 'month'
        case 'fortknight':
            return mensualidad[1], 'fortknight'
        case 'week':
            return mensualidad[2], 'week'
        case 'day':
            return mensualidad[3], 'day'

def generateSet(data, dict_key = False):
    if dict_key:
        return (dat for dat in data) # Nombre y valor monetario
    return (dat for dat in data.keys()) #Nombre de producto

def createFilesDirectory():
    if not(os.path.exists('files')):
        os.makedirs(scriptPath('files'))
    crearArchivoMensualidad(scriptPath('files','mensualidad.json'))
    crearArchivoProductos(scriptPath('files','nombre_productos.json'))
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


if __name__ == "__main__":
    pass