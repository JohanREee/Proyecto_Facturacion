import re
from archivo import createFilesDirectory
MONTH = 'month'
FORTKNIGHT = 'fortknight'
WEEK = 'week'
DAY = 'day'

def ask(message):
    print(message)
    print('1. Si\n2. No')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            return True
        case 2:
            return False
        case _:
            print('Valor invalido. Volviendo al menu anterior')

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
def validarNumero(message, age = False, services = False):
    numero = int(input(message))
    if age:
        if not (15<numero<100):
            raise ValueError
        return numero
    if services:
        if numero == 1 or numero == 2:
            return numero
        else:
            raise ValueError
    return numero

@decoratorvalidate
def validarFloat(message):
    numero = float(input(message))
    return numero
@decoratorvalidate
def validarCadena(message):
    cadena = str(input(message))
    val = any((char.isdigit() or char.isspace())for char in cadena)
    if not val:
        raise ValueError
    return cadena

def cedulaFormat(cedula):
    #xxx-xxxxxx-xxxx[A-Z]
    n_id = r"\d{3}-\d{6}-\d{4}[A-Z]"
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

if __name__ == "__main__":
    pass