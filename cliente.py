import validaciones as v
import mensualidad as m
import time_form as t
from Asesoramientos import generarAsesoramiento
NAME = 'nombre'
AGE = 'edad'
ID = 'cedula'
conteo_cliente = 1
lista_clientes = []
def modificarListaEmpleado(cliente_update, id_cliente):
    for x, cliente in enumerate(lista_clientes):
        if id_cliente == cliente.getIdClient():
            lista_clientes[x] = cliente_update
class Cliente:
    def __init__(self):
        global conteo_cliente
        self.nombre_completo = v.validarCadena('Digite el nombre del cliente: ')
        self.edad = v.validarNumero('Digite la edad del cliente: ')
        self.__cedula = v.validarCedula('Digite la cedula del cliente: ', lista_clientes)
        self.__servicios = {"Servicios_activos": [], "Asesoramientos_activos": []}        
        self.__id_cliente = conteo_cliente
        self.__band = True
        self.mensualidad_dias = 0
        self.asesoramiento_dias = 0
        conteo_cliente +=1
        print(f'Usuario {self.nombre_completo} agregado con exito.\n\n')

    def getBand(self):
        return self.__band
    
    def getId(self):
        return self.__cedula
    
    def getIdClient(self):
        return self.__id_cliente
    
    def getName(self):
        return self.nombre_completo
    
    def updateServices(self):
        for mensualidad in self.__servicios["Servicios_activos"]:
            if t.validateTime(mensualidad[2]):
                match mensualidad[0]:
                    case 'Mensual':
                        self.mensualidad_dias -=30
                    case 'Quincenal':
                        self.mensualidad_dias -=15
                    case 'Semanal':
                        self.mensualidad_dias -=7
                    case 'Diario':
                        self.mensualidad_dias -=1
                del mensualidad
        for asesoramiento in self.__servicios["Asesoramientos_activos"]:
            if t.validateTime(asesoramiento[2]):
                self.asesoramiento_dias -=30
                del asesoramiento
    def showClient(self, bypass = False):#bypass = True for showing ALL clients without asking
        if not bypass or not self.getBand():
            if not(v.ask('Este usuario ha sido eliminado del sistema. Desea mostrarlo?')):
                return
        print(f'\nNombre: {self.nombre_completo}')
        print(f'Edad: {self.edad}')
        print(f'Cedula: {self.getId()}')
        print(f'ID del cliente: {self.getIdClient()}\n')
        print('Servicios activos: ')
        self.showMonthlyPayment()
        self.showConsultancies()
    def showMonthlyPayment(self):
        for mensualidad in self.__servicios["Servicios_activos"]:
            print(f'Tipo de pago: {mensualidad[0]}')
            print(f'Cantidad a pagar: C${mensualidad[1]}')
            print(f'Fecha de expiracion: {v.showDate(mensualidad[2])}\n')
    def showConsultancies(self):
        for asesoramiento in self.__servicios["Asesoramientos_activos"]:
            print(f'Tipo de asesoramiento: {asesoramiento[0]}')
            print(f"Cantidad a pagar: ${asesoramiento[1]}")
            print(f"Fecha de expiracion: {v.showDate(asesoramiento[2])}\n")
    def editName(self):
        nombre = v.validarCadena('Digite el nuevo nombre del cliente: ')
        print(f'El nombre {self.nombre_completo} ha sido modificado por {nombre}')
        return nombre
    def editAge(self):
        edad = v.validarNumero('Digite la nueva edad del cliente: ', age=True)
        print(f'La edad {self.edad} ha sido modificada por {edad}')
        return edad
    def editMonthlyPayment(self):
        pass
    def editServices(self):
        print("1. Servicios")
        print("2. Asesoramientos")
        op = v.validarNumero("Digite la opcion que desea modificar: ")
        match op:
            case 1:
                pass
    def editClient(self, edit):
        match edit:
            case  1:
                self.nombre_completo = self.editName()
            case  2:
                self.edad = self.editAge()
            case  3:
                pass
            case 4:
                pass
    def offBand(self):
        self.__band = False
    def onBand(self):
        self.__band = True
    def addService(self, type_of_payment):
        list_payment, self.mensualidad_dias = m.generarMembresia(type_of_payment,self.mensualidad_dias)
        self.__servicios['Servicios_activos'].append(list_payment)
    def addConsultancy(self, type_of_consultancy):
        list_consultancy, self.asesoramiento_dias = generarAsesoramiento(type_of_consultancy, self.asesoramiento_dias)
        self.__servicios['Asesoramientos_activos'].append(list_consultancy)
        
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
    cliente = buscarCliente(lista_clientes, setId())
    if  cliente is None:
        print('Cliente no encontrado. Volviendo al menu anterior')
        return
    print(f'Opciones a editar para el cliente{cliente.nombre_completo}:')
    print('1.Nombre\n2.Edad\n3. Cedula')
    op = v.validarNumero('Seleccione una opcion valida: ')
    cliente.editClient(op)
    print('Cliente editado exitosamente')

def triggerClientState(action):
    found_client = buscarCliente(lista_clientes, setId())
    if found_client is None:
        print('Cliente no encontrado. Volviendo al menu anterior')
        return
    if found_client.getBand() == False and action == 'off':
        print('No puedes eliminar a un cliente ya eliminado.')
        return
    if found_client.getBand() == True and action == 'on':
        print('No puedes reactivar a un cliente ya activado.')
        return
    eliminate_or_activate = 'eliminar' if action == 'off' else 'activar'
    if not(v.ask(f'Estas seguro de querer {eliminate_or_activate} al usuario {found_client.getName()}?')):
        return
    for x, current_client in enumerate(lista_clientes):
        if current_client.getId() == found_client.getId():
            if eliminate_or_activate == 'eliminar':
                lista_clientes[x].offBand()
                print('Cliente eliminado del sistema satisfactoriamente')
            else:
                lista_clientes[x].onBand()
                print('Cliente reactivado satisfactoriamente')
            return
def updateAllClients():
    for cliente in lista_clientes:
        cliente.updateServices()
        0
def addService(type_of_payment):
    cliente = buscarCliente(lista_clientes, setId())
    if cliente is None:
        return
    for x, current_client in enumerate(lista_clientes):
        if current_client.getId() == cliente.getId():
            lista_clientes[x].addService(type_of_payment)
            print(f'Servicio agregado con exito al usuario {cliente.getName()}')
            return

def addConsultancy(type_of_consultancy):
    cliente = buscarCliente(lista_clientes, setId())
    if cliente is None:
        return
    for x, current_client in enumerate(lista_clientes):
        if current_client.getId() == cliente.getId():
            lista_clientes[x].addConsultancy(type_of_consultancy)
            print(f'Asesoramiento agregado con exito al usuario {cliente.getName()}')
            return
def showAllClients():
    for cliente in lista_clientes:
        cliente.showClient(bypass = True)