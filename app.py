import time 
import validaciones
lista_clientes = []

def busqueda(cedula = None):
    if cedula is None:
        cedula = validaciones.validarCadena('Digite la cedula del cliente: ')
    for clientes in lista_clientes:
        if clientes.returnId() == cedula:
            return clientes
    return False

class Servicio:
    def __init__ (self, mensualidad, quincena, semana, dia):
        self.mensualidad = mensualidad
        self.quincena = quincena
        
        self.semana = semana
        self.dia = dia
    def mensualidad():pass

class Clientes:
    def __init__(self):
        self.servicios = {'Servicios': [], 'Asesoramientos':[]}
    def agregarCliente(self):
        self.nombre_completo = validaciones.validarCadena('Digite el nombre del cliente: ')
        self.edad = validaciones.validarNumero('Digite la edad del cliente: ')
        self.cedula = validaciones.validarCedula('Digite la cedula del cliente: ')
    
    def returnId(self):
        return self.cedula

def editarNombre():
    nombre = validaciones.validarCadena('Digite el nombre del cliente: ')
    return nombre
def editarEdad():
    edad = validaciones.validarNumero('Digite la edad del cliente: ')
    return edad
def editarCedula():
    cedula = validaciones.validarCedula('Digite la cedula del cliente: ')
    return cedula

def editarCliente():
    cliente = busqueda()
    if not cliente:
        print('Usuario no encontrado. Volviendo al menu anterior.')
        return
    print('Seleccione una opcion valida: ')
    print('1. Editar nombre')
    print('2. Editar edad')
    print('3. Editar cedula')
    op = validaciones.validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case _:
            print('Opcion invalida. Volviendo al menu anterior')
class Producto():pass
class Asesoramiento:
    pass



