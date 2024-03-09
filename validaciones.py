import re


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
def loadFile(file_name):
    with open(file_name, 'r') as file:
        return file.read()
    
def loadJSONMonthlyPayment():
    #Estas lineas manejan el acceso a archivos sin importar el sistema operativo(Usa ruta absoluta, no relativa)
    script_dir = os.path.dirname(os.path.abspath(__file__))#
    script_path = os.path.join(script_dir, 'files', 'mensualidad.json') 
    #Ya sabes que en windows la ruta de un archivo es tipo: Users/Johan/archivo.py, pero en mac no es asi
    file = loadFile(script_path)
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
        return None
    match type_of_payment:
        case 'month':
            return mensualidad[0]
        case 'fortknight':
            return mensualidad[1]
        case 'week':
            return mensualidad[2]
        case 'day':
            return mensualidad[3]
        case _:
            return None
'''
def libraProteina(valor, cantidad_libras):
    return valor * cantidad_libras
'''

   