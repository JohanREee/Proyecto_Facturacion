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
    #xxx-xxxxxx-xxxxd
    patron = r"\d{3}-\d{6}-\d{4}[A-Za-z]"
    if not(re.fullmatch(patron, cedula)):
        return False
    return True
def
@decoratorvalidate
def validarCedula(message):
    cedula = str(input(message))
    if not(cedulaFormat(cedula)):
        raise ValueError
    return cedula

def libraProteina(valor, cantidad_libras):
    return valor * cantidad_libras
    

   