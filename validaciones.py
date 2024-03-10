import re
MONTH = 'month'
FORTKNIGHT = 'fortknight'
WEEK = 'week'
DAY = 'day'

def decoratorvalidate(function):
    def wrap(*args, **kwargs):
        while True:
            try:
                result = function(*args, **kwargs)
            except ValueError:
                print('Valor invalido. Volver a intentarlo')
                continue
            return result
    return wrap

@decoratorvalidate
def validarNumero(message):
    numero = int(input(message))
    return numero

@decoratorvalidate
def validarCadena(message):
    cadena = str(input(message))
    val = any((char.isdigit() or char.isspace())for char in cadena)
    if val:
        raise ValueError
    return cadena

def cedulaFormat(cedula):
    #xxx-xxxxxx-xxxx[A-z]
    n_id = r"\d{3}-\d{6}-\d{4}[A-Za-z]"
    if not(re.fullmatch(n_id, cedula)):
        return False
    return True

def buscarIdEmpleado(lista_cliente, cedula):
    lista_cliente_id = {cliente.getId() for cliente in lista_cliente}
    if cedula in lista_cliente_id:
        return False
    return True

@decoratorvalidate
def validarCedula(message, lista_cliente):
    cedula = str(input(message))
    if not(cedulaFormat(cedula)):
        raise ValueError
    if not (buscarIdEmpleado(lista_cliente,cedula)):
        raise ValueError
    return cedula

#files
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
    with open(file_name, 'r') as file:
        return file.read()

def scriptPath(dir = None, file = None):
    #Estas lineas manejan el acceso a archivos sin importar el sistema operativo(Usa ruta absoluta, no relativa)
    script_dir = os.path.dirname(os.path.abspath(__file__))#
    return os.path.join(script_dir, dir, file) 
    #Ya sabes que en windows la ruta de un archivo es tipo: Users/Johan/archivo.py, pero en mac no es asi

def loadJSONProduct(producto_clasificacion):
    script_path = scriptPath('files','nombre_productos.json')
    file = readFile(script_path) 
    j_file = j.load(file)
    #Entonces en esta parte estoy cargando UNICAMENTE una clasificacion
    producto_clasificacion_cargado = j_file[producto_clasificacion] 
    #Se supone que los valores son otras colecciones de datos tipo: {llave: valor}
    set_producto_cargado = (producto for producto in producto_clasificacion_cargado.keys())###
    
    return set_producto_cargado###

def solicitarProducto():
    set_producto = loadJSONProduct('Productos_Tarros_Total')
    for producto in set_producto:
        print(producto, end=',')
    print('\n')

    producto = str(input('Digite un producto de la lista: '))
    if not(producto in set_producto):
        print('Producto no encontrado. Volviendo al menu anterior')
        return
    libra = str(input(f'Digite la cantidad de libras para el producto {producto}: '))

def loadJSONMonthlyPayment():
    script_path = scriptPath('files', 'mensualidad.json')
    file = readFile(script_path)
    if file is None:
        return None
    j_file = j.load(file)
    month = j_file["Monthly"]
    fortknight = j_file["Fortknight"]
    week = j_file["Week"]
    day = j_file["Daily"]
    return [month,fortknight,week,day]

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
        case _:
            print('Error. No se ha encontrado el archivo "mensualidad.json". Desea añadirlo?')



'''
def libraProteina(valor, cantidad_libras):
    return valor * cantidad_libras
'''

   