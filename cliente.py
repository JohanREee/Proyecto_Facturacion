import validaciones as v

NAME = 'nombre'
AGE = 'edad'
ID = 'cedula'
conteo_cliente = 0
lista_clientes = []
def modificarListaEmpleado(cliente_update, id_cliente):
    for x, cliente in enumerate(lista_clientes):
        if id_cliente == cliente.getIdClient():
            lista_clientes[x] = cliente_update
class Cliente:
    def __init__(self):
        self.nombre_completo = v.validarCadena('Digite el nombre del cliente: ')
        self.edad = v.validarNumero('Digite la edad del cliente: ')
        self.__cedula = v.validarCedula('Digite la cedula del cliente: ')
        self.__servicios = {'Servicios activos': None, 'Asesoramientos activos': None}        
        self.__id_cliente = conteo_cliente
        self.__band = True
        conteo_cliente +=1
    def getBand(self):
        return self.__band
    def getId(self):
        return self.__cedula
    def getIdClient(self):
        return self.__id_cliente
    def getName(self):
        return self.nombre_completo
    
    def showClient(self):
        print(f'\nNombre: {self.nombre_completo}')
        print(f'Edad: {self.edad}')
        print(f'Cedula: {self.__cedula}\n')
        #add services

    def editName(self):
        nombre = v.validarCadena('Digite el nuevo nombre del cliente: ')
        print(f'El nombre {self.nombre_completo} ha sido modificado por {nombre}')
        return nombre
    def editAge(self):
        edad = v.validarNumero('Digite la nueva edad del cliente: ')
        print(f'La edad {self.edad} ha sido modificada por {edad}')
        return edad
    def editId(self):
        id = v.validarCedula('Digite la nueva cedula del cliente: ', lista_clientes)
        print(f'La cedula {self.getId()} ha sido modificada por {id}')
        return id
    
    def editClient(self, edit):
        if edit == 1:
            self.nombre_completo = self.editName()
        elif edit == 2:
            self.edad = self.editAge()
        elif edit == 3:
            self.__cedula = self.editId()
        modificarListaEmpleado(self,self.getIdClient())
    def offBand(self):
        self.__band = False
    def onBand(self):
        self.__band = True

def digitarCedula():
    cedula = str(input('Digite la cedula que desea buscar: '))
    return cedula

def setId():
    return {cliente.getId() for cliente in lista_clientes}

def buscarCliente(lista_cliente, set, cedula = True):
    if cedula:
        cedula = digitarCedula()
    if not (cedula in set):
        print('Cliente no encontrado en el sistema')
        return None
    for cliente in lista_cliente:
        if cedula == cliente.getId():
            return cliente

def editarCliente():
    cliente = buscarCliente(lista_clientes, setId(lista_clientes))
    if  cliente is None:
        print('Cliente no encontrado. Volviendo al menu anterior')
        return
    print(f'Opciones a editar para el cliente{cliente.nombre_completo}:')
    print('1.Nombre\n2.Edad\nCedula')
    op = v.validarNumero('Seleccione una opcion valida: ')
    cliente.editClient(op)
    print('Cliente editado exitosamente')

def ask(message):
    print(message)
    print('1. Si\n2. No')
    op = v.validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            return True
        case 2:
            return False
        case _:
            print('Valor invalido. Volviendo al menu anterior')

def triggerEliminarCliente():
    cliente = buscarCliente(lista_clientes, setId(lista_clientes))
    if cliente is None:
        print('Cliente no encontrado. Volviendo al menu anterior')
        return
    if not(ask(f'Estas seguro de querer eliminar al usuario {cliente.getName()}?')):
        return
    for x, client in enumerate(lista_clientes):
        if client.getId() == cliente.getId():
            lista_clientes[x].offBand()
            break
    print('Cliente eliminado del sistema.')
    
def triggerActivarCliente():
    cliente = buscarCliente(lista_clientes, setId(lista_clientes))
    if cliente is None:
        print('Cliente no encontrado. Volviendo al menu anterior')
        return
    if not(ask(f'Estas seguro de querer activar al usuario {cliente.getName()}?')):
        return
    for x, client in enumerate(lista_clientes):
        if client.getId() == cliente.getId():
            lista_clientes[x].onBand()
            break
    print('Cliente reactivado.')
    

    